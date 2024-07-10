import comfy

isEnabled = False
traj_cache = None
strength = 0.0

ORIGINAL_SAMPLE = comfy.sample.sample
ORIGINAL_SAMPLE_CUSTOM = comfy.sample.sample_custom


def disable():
    global isEnabled
    isEnabled = False


def hijack(SAMPLE):

    def sample_center(*args, **kwargs):
        original_callback = kwargs["callback"]

        def hijack_callback(step, x0, x, total_steps):
            global isEnabled
            global traj_cache
            global strength

            if not isEnabled:
                return original_callback(step, x0, x, total_steps)

            if traj_cache is not None:
                delta = x.detach().clone() - traj_cache
                x += delta * strength

            traj_cache = x.detach().clone()
            return original_callback(step, x0, x, total_steps)

        kwargs["callback"] = hijack_callback
        return SAMPLE(*args, **kwargs)

    return sample_center


comfy.sample.sample = hijack(ORIGINAL_SAMPLE)
comfy.sample.sample_custom = hijack(ORIGINAL_SAMPLE_CUSTOM)


class ReSharpen:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "latent": ("LATENT",),
                "enable": ("BOOLEAN", {"default": False}),
                "details": (
                    "FLOAT",
                    {"default": 0.0, "min": -1.0, "max": 1.0, "step": 0.1},
                ),
            }
        }

    RETURN_TYPES = ("LATENT",)
    FUNCTION = "hook"
    CATEGORY = "latent"

    def hook(self, latent, enable, details):
        global isEnabled
        isEnabled = enable

        if isEnabled:
            global traj_cache
            traj_cache = None
            global strength
            strength = details / -10.0

        return (latent,)
