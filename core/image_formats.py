"""
image_formats.py

Image format utilities for Bulk Image Resizer.
"""

from pathlib import Path

from settings import SUPPORTED_IMAGE_FORMATS


def get_supported_formats() -> list[str]:
    """
    Return the supported image format patterns.
    """

    return sorted(SUPPORTED_IMAGE_FORMATS)


def get_supported_extensions() -> list[str]:
    """
    Return supported file extensions.
    """

    extensions = []

    for pattern in SUPPORTED_IMAGE_FORMATS:
        extension = pattern.replace("*", "").lower()
        extensions.append(extension)

    return sorted(extensions)


def is_supported_extension(extension: str) -> bool:
    """
    Check whether an extension is supported.
    """

    extension = extension.lower()

    if not extension.startswith("."):
        extension = f".{extension}"

    return extension in get_supported_extensions()


def is_supported_image(image_path: Path) -> bool:
    """
    Check whether an image file is supported.
    """

    return is_supported_extension(
        image_path.suffix
    )


def filter_supported_images(
    image_paths: list[Path],
) -> list[Path]:
    """
    Return only supported image files.
    """

    return [
        image
        for image in image_paths
        if is_supported_image(image)
    ]


def filter_unsupported_images(
    image_paths: list[Path],
) -> list[Path]:
    """
    Return unsupported image files.
    """

    return [
        image
        for image in image_paths
        if not is_supported_image(image)
    ]


def count_supported_images(
    image_paths: list[Path],
) -> int:
    """
    Return the number of supported images.
    """

    return len(
        filter_supported_images(image_paths)
    )


def count_unsupported_images(
    image_paths: list[Path],
) -> int:
    """
    Return the number of unsupported images.
    """

    return len(
        filter_unsupported_images(image_paths)
    )


def group_images_by_extension(
    image_paths: list[Path],
) -> dict[str, list[Path]]:
    """
    Group images by file extension.
    """

    groups = {}

    for image in image_paths:

        extension = image.suffix.lower()

        if extension not in groups:
            groups[extension] = []

        groups[extension].append(image)

    return groups