"""
batch_processor.py

Batch image processing for Bulk Image Resizer.
"""

from pathlib import Path

from core.resize_engine import resize_image


def process_images(
    image_paths: list[Path],
    output_folder: Path,
    resize_method: str,
    resize_value: int,
    suffix: str,
) -> dict:
    """
    Resize all supplied images.

    Returns
    -------
    dict
        Processing summary.
    """

    results = {
        "total": len(image_paths),
        "successful": 0,
        "failed": 0,
        "success_files": [],
        "failed_files": [],
    }

    for image_path in image_paths:

        success, message = resize_image(
            image_path=image_path,
            output_folder=output_folder,
            resize_method=resize_method,
            resize_value=resize_value,
            suffix=suffix,
        )

        if success:

            results["successful"] += 1

            results["success_files"].append(
                Path(message)
            )

        else:

            results["failed"] += 1

            results["failed_files"].append(
                {
                    "file": image_path,
                    "error": message,
                }
            )

    return results


def has_failures(results: dict) -> bool:
    """
    Return True if any image failed.
    """

    return results["failed"] > 0


def has_success(results: dict) -> bool:
    """
    Return True if at least one image was resized.
    """

    return results["successful"] > 0


def success_rate(results: dict) -> float:
    """
    Return the success percentage.
    """

    if results["total"] == 0:
        return 0.0

    return (
        results["successful"] / results["total"]
    ) * 100.0


def failed_rate(results: dict) -> float:
    """
    Return the failure percentage.
    """

    if results["total"] == 0:
        return 0.0

    return (
        results["failed"] / results["total"]
    ) * 100.0