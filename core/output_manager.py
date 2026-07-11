"""
output_manager.py

Output file and folder management for Bulk Image Resizer.
"""

from pathlib import Path


def ensure_output_folder(output_folder: Path) -> Path:
    """
    Create the output folder if it does not already exist.

    Parameters
    ----------
    output_folder : Path

    Returns
    -------
    Path
    """

    output_folder.mkdir(
        parents=True,
        exist_ok=True,
    )

    return output_folder


def build_output_filename(
    image_path: Path,
    suffix: str,
) -> str:
    """
    Build the output filename.

    Parameters
    ----------
    image_path : Path

    suffix : str

    Returns
    -------
    str
    """

    return (
        f"{image_path.stem}"
        f"{suffix}"
        f"{image_path.suffix}"
    )


def build_output_path(
    image_path: Path,
    output_folder: Path,
    suffix: str,
) -> Path:
    """
    Build the complete output path.

    Parameters
    ----------
    image_path : Path

    output_folder : Path

    suffix : str

    Returns
    -------
    Path
    """

    ensure_output_folder(output_folder)

    filename = build_output_filename(
        image_path,
        suffix,
    )

    return output_folder / filename


def output_file_exists(
    output_path: Path,
) -> bool:
    """
    Check whether the output file already exists.
    """

    return output_path.exists()


def generate_unique_output_path(
    image_path: Path,
    output_folder: Path,
    suffix: str,
) -> Path:
    """
    Generate a unique output filename if one already exists.

    Example:
        photo_resized.jpg
        photo_resized_1.jpg
        photo_resized_2.jpg
    """

    output_path = build_output_path(
        image_path,
        output_folder,
        suffix,
    )

    if not output_file_exists(output_path):
        return output_path

    counter = 1

    while True:

        filename = (
            f"{image_path.stem}"
            f"{suffix}"
            f"_{counter}"
            f"{image_path.suffix}"
        )

        candidate = output_folder / filename

        if not candidate.exists():
            return candidate

        counter += 1


def get_output_directory(
    output_path: Path,
) -> Path:
    """
    Return the parent directory of an output file.
    """

    return output_path.parent


def get_output_filename(
    output_path: Path,
) -> str:
    """
    Return only the filename.
    """

    return output_path.name