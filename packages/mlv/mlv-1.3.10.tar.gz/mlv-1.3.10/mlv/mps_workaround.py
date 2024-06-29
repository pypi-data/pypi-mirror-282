import importlib

import torch
from torch import Tensor
import platform
from packaging import version


class CondFunc:
    def __new__(cls, orig_func, sub_func, cond_func):
        self = super(CondFunc, cls).__new__(cls)
        if isinstance(orig_func, str):
            func_path = orig_func.split(".")
            for i in range(len(func_path) - 1, -1, -1):
                try:
                    resolved_obj = importlib.import_module(".".join(func_path[:i]))
                    break
                except ImportError:
                    pass
            for attr_name in func_path[i:-1]:
                resolved_obj = getattr(resolved_obj, attr_name)
            orig_func = getattr(resolved_obj, func_path[-1])
            setattr(
                resolved_obj,
                func_path[-1],
                lambda *args, **kwargs: self(*args, **kwargs),
            )
        self.__init__(orig_func, sub_func, cond_func)
        return lambda *args, **kwargs: self(*args, **kwargs)

    def __init__(self, orig_func, sub_func, cond_func):
        self.__orig_func = orig_func
        self.__sub_func = sub_func
        self.__cond_func = cond_func

    def __call__(self, *args, **kwargs):
        if not self.__cond_func or self.__cond_func(self.__orig_func, *args, **kwargs):
            return self.__sub_func(self.__orig_func, *args, **kwargs)
        else:
            return self.__orig_func(*args, **kwargs)


def check_for_mps() -> bool:
    if version.parse(torch.__version__) <= version.parse("2.0.1"):
        if not getattr(torch, "has_mps", False):
            return False
        try:
            torch.zeros(1).to(torch.device("mps"))
            return True
        except Exception:
            return False
    else:
        return torch.backends.mps.is_available() and torch.backends.mps.is_built()


has_mps = check_for_mps()


# MPS workaround for https://github.com/pytorch/pytorch/issues/89784
def cumsum_fix(input, cumsum_func, *args, **kwargs):
    if input.device.type == "mps":
        output_dtype = kwargs.get("dtype", input.dtype)
        if output_dtype == torch.int64:
            return cumsum_func(input.cpu(), *args, **kwargs).to(input.device)
        elif (
            output_dtype == torch.bool
            or cumsum_needs_int_fix
            and (output_dtype == torch.int8 or output_dtype == torch.int16)
        ):
            return cumsum_func(input.to(torch.int32), *args, **kwargs).to(torch.int64)
    return cumsum_func(input, *args, **kwargs)


# MPS workaround for https://github.com/AUTOMATIC1111/stable-diffusion-webui/pull/14046
def interpolate_with_fp32_fallback(orig_func, *args, **kwargs) -> Tensor:
    try:
        return orig_func(*args, **kwargs)
    except RuntimeError as e:
        if "not implemented for" in str(e) and "Half" in str(e):
            input_tensor = args[0]
            return orig_func(input_tensor.to(torch.float32), *args[1:], **kwargs).to(
                input_tensor.dtype
            )
        else:
            print(f"An unexpected RuntimeError occurred: {str(e)}")
            raise e


if has_mps:
    if platform.mac_ver()[0].startswith("13.2."):
        # MPS workaround for https://github.com/pytorch/pytorch/issues/95188, thanks to danieldk (https://github.com/explosion/curated-transformers/pull/124)
        CondFunc(
            "torch.nn.functional.linear",
            lambda _, input, weight, bias: (
                (torch.matmul(input, weight.t()) + bias)
                if bias is not None
                else torch.matmul(input, weight.t())
            ),
            lambda _, input, weight, bias: input.numel() > 10485760,
        )

    if version.parse(torch.__version__) < version.parse("1.13"):
        # PyTorch 1.13 doesn't need these fixes but unfortunately is slower and has regressions that prevent training from working

        # MPS workaround for https://github.com/pytorch/pytorch/issues/79383
        CondFunc(
            "torch.Tensor.to",
            lambda orig_func, self, *args, **kwargs: orig_func(
                self.contiguous(), *args, **kwargs
            ),
            lambda _, self, *args, **kwargs: self.device.type != "mps"
            and (
                args
                and isinstance(args[0], torch.device)
                and args[0].type == "mps"
                or isinstance(kwargs.get("device"), torch.device)
                and kwargs["device"].type == "mps"
            ),
        )
        # MPS workaround for https://github.com/pytorch/pytorch/issues/80800
        CondFunc(
            "torch.nn.functional.layer_norm",
            lambda orig_func, *args, **kwargs: orig_func(
                *([args[0].contiguous()] + list(args[1:])), **kwargs
            ),
            lambda _, *args, **kwargs: args
            and isinstance(args[0], torch.Tensor)
            and args[0].device.type == "mps",
        )
        # MPS workaround for https://github.com/pytorch/pytorch/issues/90532
        CondFunc(
            "torch.Tensor.numpy",
            lambda orig_func, self, *args, **kwargs: orig_func(
                self.detach(), *args, **kwargs
            ),
            lambda _, self, *args, **kwargs: self.requires_grad,
        )
    elif version.parse(torch.__version__) > version.parse("1.13.1"):
        cumsum_needs_int_fix = (
            not torch.Tensor([1, 2])
            .to(torch.device("mps"))
            .equal(torch.ShortTensor([1, 1]).to(torch.device("mps")).cumsum(0))
        )
        cumsum_fix_func = lambda orig_func, input, *args, **kwargs: cumsum_fix(
            input, orig_func, *args, **kwargs
        )
        CondFunc("torch.cumsum", cumsum_fix_func, None)
        CondFunc("torch.Tensor.cumsum", cumsum_fix_func, None)
        CondFunc(
            "torch.narrow",
            lambda orig_func, *args, **kwargs: orig_func(*args, **kwargs).clone(),
            None,
        )

        # MPS workaround for https://github.com/pytorch/pytorch/issues/96113
        CondFunc(
            "torch.nn.functional.layer_norm",
            lambda orig_func, x, normalized_shape, weight, bias, eps, **kwargs: orig_func(
                x.float(),
                normalized_shape,
                weight.float() if weight is not None else None,
                bias.float() if bias is not None else bias,
                eps,
            ).to(
                x.dtype
            ),
            lambda _, input, *args, **kwargs: len(args) == 4
            and input.device.type == "mps",
        )

        # MPS workaround for https://github.com/AUTOMATIC1111/stable-diffusion-webui/pull/14046
        CondFunc(
            "torch.nn.functional.interpolate", interpolate_with_fp32_fallback, None
        )
        CondFunc("torch.nn.functional.layer_norm", interpolate_with_fp32_fallback, None)

        # MPS workaround for https://github.com/pytorch/pytorch/issues/92311
        if platform.processor() == "i386":
            for funcName in ["torch.argmax", "torch.Tensor.argmax"]:
                CondFunc(
                    funcName,
                    lambda _, input, *args, **kwargs: torch.max(
                        input.float() if input.dtype == torch.int64 else input,
                        *args,
                        **kwargs,
                    )[1],
                    lambda _, input, *args, **kwargs: input.device.type == "mps",
                )
