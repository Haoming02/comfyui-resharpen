from functools import wraps

import execution

from .resharpen import ReSharpen, disable_resharpen

NODE_CLASS_MAPPINGS = {"ReSharpen": ReSharpen}
NODE_DISPLAY_NAME_MAPPINGS = {"ReSharpen": "ReSharpen"}


def find_node(prompt: dict) -> bool:
    return any(node.get("class_type", None) == "ReSharpen" for node in prompt.values())


original_validate = execution.validate_prompt


@wraps(original_validate)
async def hijack_validate(*args):
    for arg in args:
        if isinstance(arg, dict):
            prompt = arg
            break

    if not find_node(prompt):
        disable_resharpen()

    return await original_validate(*args)


execution.validate_prompt = hijack_validate
