from .resharpen import HookCallback, UnhookCallback

NODE_CLASS_MAPPINGS = {
	"HookResharpen": HookCallback,
	"UnhookResharpen": UnhookCallback,
}

NODE_DISPLAY_NAME_MAPPINGS = {
	"HookResharpen": "Hook ReSharpen",
	"UnhookResharpen": "Unhook ReSharpen",
}
