"""
aspect_ratio.py

Aspect ratio calculation utilities for Bulk Image Resizer.
"""


def resize_by_width(
    original_width: int,
    original_height: int,
    new_width: int,
) -> tuple[int, int]:
    """
    Calculate dimensions using a new width.
    """

    ratio = new_width / original_width

    width = new_width
    height = int(original_height * ratio)

    return max(1, width), max(1, height)


def resize_by_height(
    original_width: int,
    original_height: int,
    new_height: int,
) -> tuple[int, int]:
    """
    Calculate dimensions using a new height.
    """

    ratio = new_height / original_height

    width = int(original_width * ratio)
    height = new_height

    return max(1, width), max(1, height)


def resize_by_percentage(
    original_width: int,
    original_height: int,
    percentage: int,
) -> tuple[int, int]:
    """
    Calculate dimensions using a percentage.
    """

    scale = percentage / 100

    width = int(original_width * scale)
    height = int(original_height * scale)

    return max(1, width), max(1, height)


def fit_within(
    original_width: int,
    original_height: int,
    max_dimension: int,
) -> tuple[int, int]:
    """
    Calculate dimensions to fit within a square.
    """

    ratio = min(
        max_dimension / original_width,
        max_dimension / original_height,
    )

    width = int(original_width * ratio)
    height = int(original_height * ratio)

    return max(1, width), max(1, height)


def calculate_new_size(
    original_width: int,
    original_height: int,
    method: str,
    value: int,
) -> tuple[int, int]:
    """
    Calculate resized dimensions.
    """

    if method == "Width":
        return resize_by_width(
            original_width,
            original_height,
            value,
        )

    if method == "Height":
        return resize_by_height(
            original_width,
            original_height,
            value,
        )

    if method == "Percentage":
        return resize_by_percentage(
            original_width,
            original_height,
            value,
        )

    if method == "Fit Within":
        return fit_within(
            original_width,
            original_height,
            value,
        )

    raise ValueError(
        f"Unsupported resize method: {method}"
    )