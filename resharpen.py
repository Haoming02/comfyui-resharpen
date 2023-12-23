import comfy

ORIGINAL_SAMPLE = comfy.sample.sample
ORIGINAL_SAMPLE_CUSTOM = comfy.sample.sample_custom

traj_cache = None

def hijack(SAMPLE, strength:float):

    def sample_center(*args, **kwargs):
        original_callback = kwargs['callback']

        def hijack_callback(step, x0, x, total_steps):
            global traj_cache

            if traj_cache is not None:
                delta = x.detach().clone() - traj_cache
                x += delta * strength

            traj_cache = x.detach().clone()
            return original_callback(step, x0, x, total_steps)

        kwargs['callback'] = hijack_callback
        return SAMPLE(*args, **kwargs)

    return sample_center


class HookCallback:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "prompt": ("CONDITIONING",),
                "details": ("FLOAT", {"default": 0.0, "min": -1.0, "max": 1.0, "step": 0.1})
            }
        }

    RETURN_TYPES = ("CONDITIONING",)
    FUNCTION = "hook"
    CATEGORY = "latent"

    def hook(self, prompt, details):
        global traj_cache
        traj_cache = None
        comfy.sample.sample_custom = hijack(ORIGINAL_SAMPLE_CUSTOM, details / -10.0)
        comfy.sample.sample = hijack(ORIGINAL_SAMPLE, details / -10.0)

        return (prompt,)

class UnhookCallback:
    @classmethod
    def INPUT_TYPES(s):
        return { "required": { "latent": ("LATENT", ) } }

    RETURN_TYPES = ("LATENT", )
    FUNCTION = "unhook"
    CATEGORY = "latent"

    def unhook(self, latent):
        global traj_cache
        traj_cache = None
        comfy.sample.sample_custom = ORIGINAL_SAMPLE_CUSTOM
        comfy.sample.sample = ORIGINAL_SAMPLE

        return (latent,)
