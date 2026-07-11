"""
image_saver.py

Image saving utilities for Bulk Image Resizer.
"""

from pathlib import Path

from PIL import Image

from core.output_manager import generate_unique_output_path


JPEG_QUALITY = 95


def save_image(
    image: Image.Image,
    source_path: Path,
    output_folder: Path,
    suffix: str,
) -> Path:
    """
    Save an image.

    Parameters
    ----------
    image : Image.Image

    source_path : Path

    output_folder : Path

    suffix : str

    Returns
    -------
    Path
    """

    output_path = generate_unique_output_path(
        image_path=source_path,
        output_folder=output_folder,
        suffix=suffix,
    )

    save_options = get_save_options(
        output_path.suffix,
    )

    image.save(
        output_path,
        **save_options,
    )

    return output_path


def get_save_options(
    extension: str,
) -> dict:
    """
    Return Pillow save options.
    """

    extension = extension.lower()

    if extension in (".jpg", ".jpeg"):

        return {
            "quality": JPEG_QUALITY,
            "optimize": True,
        }

    if extension == ".png":

        return {
            "optimize": True,
        }

    if extension == ".webp":

        return {
            "quality": JPEG_QUALITY,
        }

    return {}


def save_resized_image(
    resized_image: Image.Image,
    source_path: Path,
    output_folder: Path,
    suffix: str,
) -> tuple[bool, Path | None, str]:
    """
    Save a resized image.

    Returns
    -------
    tuple
        (success, output_path, message)
    """

    try:

        output_path = save_image(
            image=resized_image,
            source_path=source_path,
            output_folder=output_folder,
            suffix=suffix,
        )

        return (
            True,
            output_path,
            "",
        )

    except Exception as ex:

        return (
            False,
            None,
            str(ex),
        )