"""
image_metadata.py

Image metadata utilities for Bulk Image Resizer.
"""

from pathlib import Path

from PIL import Image


def get_image_size(image_path: Path) -> tuple[int, int]:
    """
    Return image width and height.
    """

    with Image.open(image_path) as image:
        return image.size


def get_image_width(image_path: Path) -> int:
    """
    Return image width.
    """

    width, _ = get_image_size(image_path)

    return width


def get_image_height(image_path: Path) -> int:
    """
    Return image height.
    """

    _, height = get_image_size(image_path)

    return height


def get_image_format(image_path: Path) -> str:
    """
    Return image format.
    """

    with Image.open(image_path) as image:
        return image.format or "Unknown"


def get_image_mode(image_path: Path) -> str:
    """
    Return image color mode.
    """

    with Image.open(image_path) as image:
        return image.mode


def get_file_size(image_path: Path) -> int:
    """
    Return file size in bytes.
    """

    return image_path.stat().st_size


def get_file_size_kb(image_path: Path) -> float:
    """
    Return file size in kilobytes.
    """

    return get_file_size(image_path) / 1024


def get_file_size_mb(image_path: Path) -> float:
    """
    Return file size in megabytes.
    """

    return get_file_size(image_path) / (1024 * 1024)


def get_metadata(image_path: Path) -> dict:
    """
    Return image metadata.
    """

    width, height = get_image_size(image_path)

    return {
        "path": image_path,
        "filename": image_path.name,
        "stem": image_path.stem,
        "extension": image_path.suffix.lower(),
        "width": width,
        "height": height,
        "format": get_image_format(image_path),
        "mode": get_image_mode(image_path),
        "size_bytes": get_file_size(image_path),
        "size_kb": round(get_file_size_kb(image_path), 2),
        "size_mb": round(get_file_size_mb(image_path), 2),
    }