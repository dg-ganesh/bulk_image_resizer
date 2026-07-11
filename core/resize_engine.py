"""
resize_engine.py

Image resizing engine for Bulk Image Resizer.
"""

from pathlib import Path

from PIL import Image

from settings import STANDARD_IMAGE_SIZES


RESAMPLE_FILTER = Image.Resampling.LANCZOS


def calculate_new_size(
    original_width: int,
    original_height: int,
    method: str,
    value: str,
) -> tuple[int, int]:
    """
    Calculate new image dimensions while maintaining aspect ratio.
    """

    if method == "Percentage":

        scale = int(value) / 100

        new_width = int(original_width * scale)
        new_height = int(original_height * scale)

    elif method == "Standard Size":

        max_width, max_height = STANDARD_IMAGE_SIZES[value]

        ratio = min(
            max_width / original_width,
            max_height / original_height,
        )

        new_width = int(original_width * ratio)
        new_height = int(original_height * ratio)

    else:

        raise ValueError(
            f"Unsupported resize method: {method}"
        )

    return (
        max(1, new_width),
        max(1, new_height),
    )


def build_output_filename(
    image_path: Path,
    output_folder: Path,
    suffix: str,
) -> Path:
    """
    Build the output file path.
    """

    filename = (
        f"{image_path.stem}"
        f"{suffix}"
        f"{image_path.suffix}"
    )

    return output_folder / filename


def resize_image(
    image_path: Path,
    output_folder: Path,
    resize_method: str,
    resize_value: str,
    suffix: str,
) -> tuple[bool, str]:
    """
    Resize a single image.
    """

    try:

        with Image.open(image_path) as image:

            width, height = image.size

            new_size = calculate_new_size(
                width,
                height,
                resize_method,
                resize_value,
            )

            resized = image.resize(
                new_size,
                RESAMPLE_FILTER,
            )

            output_path = build_output_filename(
                image_path,
                output_folder,
                suffix,
            )

            resized.save(output_path)

        return (
            True,
            str(output_path),
        )

    except Exception as ex:

        return (
            False,
            str(ex),
        )