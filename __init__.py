from functools import wraps
from typing import Callable

import execution

from .resharpen import ReSharpen, disable_resharpen

NODE_CLASS_MAPPINGS = {"Resharpen": ReSharpen}
NODE_DISPLAY_NAME_MAPPINGS = {"Resharpen": "ReSharpen"}


def find_node(prompt: dict) -> bool:
    """Find any ReSharpen Node"""
    return any(v.get("class_type") == "Resharpen" for v in prompt.values())


original_validate: Callable = execution.validate_prompt


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
