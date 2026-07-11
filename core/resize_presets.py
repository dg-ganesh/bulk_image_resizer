"""
resize_presets.py

Resize preset utilities for Bulk Image Resizer.
"""


RESIZE_METHODS = (
    "Width",
    "Height",
    "Fit Within",
    "Percentage",
)


def get_resize_methods() -> list[str]:
    """
    Return all available resize methods.
    """

    return list(RESIZE_METHODS)


def is_valid_resize_method(method: str) -> bool:
    """
    Check whether the resize method is supported.
    """

    return method in RESIZE_METHODS


def normalize_resize_method(method: str) -> str:
    """
    Normalize a resize method.
    """

    return method.strip().title()


def default_resize_method() -> str:
    """
    Return the default resize method.
    """

    return "Width"


def default_resize_value(method: str) -> int:
    """
    Return the recommended default value for a resize method.
    """

    defaults = {
        "Width": 800,
        "Height": 600,
        "Fit Within": 1024,
        "Percentage": 50,
    }

    return defaults.get(method, 800)


def get_method_description(method: str) -> str:
    """
    Return a description for a resize method.
    """

    descriptions = {
        "Width": (
            "Resize using the specified width while "
            "maintaining aspect ratio."
        ),
        "Height": (
            "Resize using the specified height while "
            "maintaining aspect ratio."
        ),
        "Fit Within": (
            "Resize so the image fits within the given "
            "maximum dimension."
        ),
        "Percentage": (
            "Resize using a percentage of the original size."
        ),
    }

    return descriptions.get(method, "")


def get_all_method_descriptions() -> dict[str, str]:
    """
    Return descriptions for all resize methods.
    """

    return {
        method: get_method_description(method)
        for method in RESIZE_METHODS
    }


def get_resize_preset(method: str) -> dict:
    """
    Return information for a resize preset.
    """

    return {
        "method": method,
        "default_value": default_resize_value(method),
        "description": get_method_description(method),
    }


def get_all_resize_presets() -> list[dict]:
    """
    Return all resize presets.
    """

    return [
        get_resize_preset(method)
        for method in RESIZE_METHODS
    ]