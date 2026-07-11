"""
image_loader.py

Image loading and filtering utilities.

This module contains functions for validating image files
and preparing them for processing.

No GUI code should exist in this module.
"""

from pathlib import Path

from settings import SUPPORTED_IMAGE_FORMATS


def get_supported_extensions() -> set[str]:
    """
    Return the supported file extensions.

    Returns
    -------
    set[str]
    """

    extensions = set()

    for pattern in SUPPORTED_IMAGE_FORMATS:
        extensions.add(
            pattern.replace("*", "").lower()
        )

    return extensions


def is_supported_image(image_path: Path) -> bool:
    """
    Determine whether the file is a supported image.

    Parameters
    ----------
    image_path : Path

    Returns
    -------
    bool
    """

    supported = get_supported_extensions()

    return image_path.suffix.lower() in supported


def filter_supported_images(
    image_paths: list[Path],
) -> list[Path]:
    """
    Filter unsupported files.

    Parameters
    ----------
    image_paths : list[Path]

    Returns
    -------
    list[Path]
    """

    valid_images = []

    for image in image_paths:

        if is_supported_image(image):

            valid_images.append(image)

    return valid_images


def remove_duplicate_images(
    image_paths: list[Path],
) -> list[Path]:
    """
    Remove duplicate image paths while preserving order.

    Parameters
    ----------
    image_paths : list[Path]

    Returns
    -------
    list[Path]
    """

    unique = []
    seen = set()

    for image in image_paths:

        resolved = image.resolve()

        if resolved in seen:
            continue

        seen.add(resolved)

        unique.append(image)

    return unique


def prepare_image_list(
    image_paths: list[Path],
) -> list[Path]:
    """
    Prepare images for processing.

    Steps
    -----
    1. Remove duplicates.
    2. Remove unsupported files.

    Parameters
    ----------
    image_paths : list[Path]

    Returns
    -------
    list[Path]
    """

    images = remove_duplicate_images(
        image_paths
    )

    images = filter_supported_images(
        images
    )

    return images