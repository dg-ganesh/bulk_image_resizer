"""
validation.py

Validation utilities for Bulk Image Resizer.
"""

from pathlib import Path

from settings import (
    PERCENTAGE_VALUES,
    STANDARD_IMAGE_SIZES,
)


def validate_resize_value(
    method: str,
    value: str,
) -> tuple[bool, str]:
    """
    Validate the resize value based on the selected resize method.
    """

    value = value.strip()

    if not value:
        return False, "Resize value is required."

    if method == "Percentage":

        if value not in PERCENTAGE_VALUES:
            return False, "Please select a valid percentage."

        return True, ""

    if method == "Standard Size":

        if value not in STANDARD_IMAGE_SIZES:
            return False, "Please select a valid image size."

        return True, ""

    return False, "Invalid resize method."


def validate_output_folder(
    folder: str,
) -> tuple[bool, str]:
    """
    Validate the output folder.
    """

    folder = folder.strip()

    if not folder:
        return False, "Output folder is required."

    path = Path(folder)

    if not path.exists():
        return False, "Output folder does not exist."

    if not path.is_dir():
        return False, "Output path is not a folder."

    return True, ""


def validate_filename_suffix(
    suffix: str,
) -> tuple[bool, str]:
    """
    Validate filename suffix.
    """

    invalid_chars = '<>:"/\\|?*'

    for char in invalid_chars:

        if char in suffix:

            return (
                False,
                f"Filename suffix contains invalid character: {char}",
            )

    return True, ""


def validate_image_list(
    images: list[Path],
) -> tuple[bool, str]:
    """
    Validate the image list.
    """

    if not images:
        return False, "No images selected."

    return True, ""


def validate_resize_request(
    images: list[Path],
    resize_method: str,
    resize_value: str,
    output_folder: str,
    suffix: str,
) -> tuple[bool, str]:
    """
    Validate all user inputs.
    """

    valid, message = validate_image_list(images)

    if not valid:
        return valid, message

    valid, message = validate_resize_value(
        resize_method,
        resize_value,
    )

    if not valid:
        return valid, message

    valid, message = validate_output_folder(
        output_folder,
    )

    if not valid:
        return valid, message

    valid, message = validate_filename_suffix(
        suffix,
    )

    if not valid:
        return valid, message

    return True, ""