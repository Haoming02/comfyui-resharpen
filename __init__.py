from .resharpen import ReSharpen, disable
import execution

NODE_CLASS_MAPPINGS = {"Resharpen": ReSharpen}

NODE_DISPLAY_NAME_MAPPINGS = {"Resharpen": "ReSharpen"}


def find_node(prompt: dict) -> bool:
    """Find any ReSharpen Node"""

    for k, v in prompt.items():
        if v["class_type"] == "Resharpen":
            return True

    return False


original_validate = execution.validate_prompt


def hijack_validate(prompt):

    if not find_node(prompt):
        disable()

    return original_validate(prompt)


execution.validate_prompt = hijack_validate
