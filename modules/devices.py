import contextlib
import torch
import ldm_patched.modules.model_management as model_management


def has_xpu() -> bool:
    return model_management.xpu_available


def has_mps() -> bool:
    return model_management.mps_mode()


def cuda_no_autocast(device_id=None) -> bool:
    return False


def get_cuda_device_id():
    return model_management.get_torch_device().index


def get_cuda_device_string():
    return str(model_management.get_torch_device())


def get_optimal_device_name():
    return model_management.get_torch_device().type


def get_optimal_device():
    return model_management.get_torch_device()


def get_device_for(task):
    return model_management.get_torch_device()


def torch_gc():
    model_management.soft_empty_cache()

    if npu_specific.has_npu:
        torch_npu_set_device()
        npu_specific.torch_npu_gc()


def torch_npu_set_device():
    # Work around due to bug in torch_npu, revert me after fixed, @see https://gitee.com/ascend/pytorch/issues/I8KECW?from=project-issue
    if npu_specific.has_npu:
        torch.npu.set_device(0)


def enable_tf32():
    return


cpu: torch.device = torch.device("cpu")
fp8: bool = False
device: torch.device = model_management.get_torch_device()
device_interrogate: torch.device = cpu  # not used
device_gfpgan: torch.device = cpu
device_esrgan: torch.device = model_management.get_torch_device()  # will be managed in special way
device_codeformer: torch.device = cpu
dtype: torch.dtype = model_management.unet_dtype()
dtype_vae: torch.dtype = model_management.vae_dtype()
dtype_unet: torch.dtype = model_management.unet_dtype()
dtype_inference: torch.dtype = model_management.unet_dtype()
unet_needs_upcast = False


def cond_cast_unet(input):
    return input


def cond_cast_float(input):
    return input


nv_rng = None
patch_module_list = []


def manual_cast_forward(target_dtype):
    return


@contextlib.contextmanager
def manual_cast(target_dtype):
    return


def autocast(disable=False):
    return contextlib.nullcontext()


def without_autocast(disable=False):
    return contextlib.nullcontext()


class NansException(Exception):
    pass


def test_for_nans(x, where):
    return


def first_time_calculation():
    return
