"""
processing_report.py

Processing report utilities for Bulk Image Resizer.
"""

from pathlib import Path


def create_report() -> dict:
    """
    Create an empty processing report.
    """

    return {
        "total": 0,
        "successful": 0,
        "failed": 0,
        "success_files": [],
        "failed_files": [],
    }


def add_success(
    report: dict,
    image_path: Path,
    output_path: Path,
) -> None:
    """
    Add a successful resize result.
    """

    report["total"] += 1
    report["successful"] += 1

    report["success_files"].append(
        {
            "input": image_path,
            "output": output_path,
        }
    )


def add_failure(
    report: dict,
    image_path: Path,
    error_message: str,
) -> None:
    """
    Add a failed resize result.
    """

    report["total"] += 1
    report["failed"] += 1

    report["failed_files"].append(
        {
            "input": image_path,
            "error": error_message,
        }
    )


def success_rate(
    report: dict,
) -> float:
    """
    Return the success percentage.
    """

    if report["total"] == 0:
        return 0.0

    return round(
        (report["successful"] / report["total"]) * 100,
        2,
    )


def failure_rate(
    report: dict,
) -> float:
    """
    Return the failure percentage.
    """

    if report["total"] == 0:
        return 0.0

    return round(
        (report["failed"] / report["total"]) * 100,
        2,
    )


def has_errors(
    report: dict,
) -> bool:
    """
    Return True if processing contains failures.
    """

    return report["failed"] > 0


def get_summary(
    report: dict,
) -> str:
    """
    Return a summary string.
    """

    return (
        f"Processed: {report['total']} | "
        f"Successful: {report['successful']} | "
        f"Failed: {report['failed']}"
    )


def clear_report(
    report: dict,
) -> None:
    """
    Reset an existing report.
    """

    report.clear()
    report.update(create_report())