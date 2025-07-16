from functools import wraps
from typing import Callable

import torch

import latent_preview

ORIGINAL_PREP: Callable = latent_preview.prepare_callback

RESHARPEN_STRENGTH: float = 0.0
LATENT_CACHE: torch.Tensor = None


def disable_resharpen():
    """Reset the ReSharpen Strength"""
    global RESHARPEN_STRENGTH
    RESHARPEN_STRENGTH = 0.0


def hijack(PREP) -> Callable:

    @wraps(PREP)
    def prep_callback(*args, **kwargs):
        global LATENT_CACHE
        LATENT_CACHE = None

        original_callback: Callable = PREP(*args, **kwargs)
        if not RESHARPEN_STRENGTH:
            return original_callback

        print("[ReSharpen] Enabled~")

        @torch.inference_mode()
        @wraps(original_callback)
        def hijack_callback(step, x0, x, total_steps):
            if not RESHARPEN_STRENGTH:
                return original_callback(step, x0, x, total_steps)

            global LATENT_CACHE
            if LATENT_CACHE is not None:
                delta = x.detach().clone() - LATENT_CACHE
                x += delta * RESHARPEN_STRENGTH

            LATENT_CACHE = x.detach().clone()
            return original_callback(step, x0, x, total_steps)

        return hijack_callback

    return prep_callback


latent_preview.prepare_callback = hijack(ORIGINAL_PREP)


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
    CATEGORY = "latent"

    def hook(self, latent, details: float):

        global RESHARPEN_STRENGTH
        RESHARPEN_STRENGTH = details / -10.0

        return (latent,)
