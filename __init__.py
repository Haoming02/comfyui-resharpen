from .resharpen import ReSharpen, disable_resharpen
from functools import wraps
from typing import Callable
import execution

NODE_CLASS_MAPPINGS = {"Resharpen": ReSharpen}
NODE_DISPLAY_NAME_MAPPINGS = {"Resharpen": "ReSharpen"}


def find_node(prompt: dict) -> bool:
    """Find any ReSharpen Node"""

    return any(v.get("class_type") == "Resharpen" for v in prompt.values())


original_validate: Callable = execution.validate_prompt


@wraps(original_validate)
def hijack_validate(prompt: dict) -> Callable:

    if not find_node(prompt):
        disable_resharpen()

    return original_validate(prompt)


execution.validate_prompt = hijack_validate
