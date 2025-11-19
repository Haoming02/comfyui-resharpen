from functools import wraps
from typing import Callable

import torch

import latent_preview

RESHARPEN_STRENGTH: float = 0.0
LATENT_CACHE: torch.Tensor = None


def disable_resharpen():
    global RESHARPEN_STRENGTH
    RESHARPEN_STRENGTH = 0.0


_prepare_callback: Callable = latent_preview.prepare_callback


@wraps(_prepare_callback)
def hijack_prepare(*args, **kwargs):
    original_callback: Callable = _prepare_callback(*args, **kwargs)

    @torch.inference_mode()
    @wraps(original_callback)
    def hijack_callback(step, x0, x, total_steps):
        original_callback(step, x0, x, total_steps)

        if not RESHARPEN_STRENGTH:
            return

        global LATENT_CACHE
        if LATENT_CACHE is not None:
            delta = x - LATENT_CACHE
            x += delta * RESHARPEN_STRENGTH

        LATENT_CACHE = x.detach().clone()

    return hijack_callback


latent_preview.prepare_callback = hijack_prepare


class ReSharpen:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "latent": ("LATENT",),
                "details": (
                    "FLOAT",
                    {"default": 0.0, "min": -2.0, "max": 2.0, "step": 0.1},
                ),
            }
        }

    RETURN_TYPES = ("LATENT",)
    FUNCTION = "hook"
    CATEGORY = "sampling"

    def hook(self, latent, details: float):
        global RESHARPEN_STRENGTH
        RESHARPEN_STRENGTH = details / -10.0
        return (latent,)
