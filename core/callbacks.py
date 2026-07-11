"""
callbacks.py

GUI callback functions for Bulk Image Resizer.
"""

from pathlib import Path
from tkinter import filedialog

from core.image_loader import prepare_image_list
from core.batch_processor import process_images
from core.validation import validate_resize_request

from gui.gui_helpers import (
    set_status,
    show_info,
    show_error,
    add_image_to_list,
    clear_image_list,
)


def on_add_images(app) -> None:
    """
    Add images to the image list.
    """

    files = filedialog.askopenfilenames(
        title="Select Images",
        filetypes=[
            (
                "Image Files",
                "*.jpg *.jpeg *.png *.webp *.bmp *.gif",
            )
        ],
    )

    if not files:
        return

    image_paths = [
        Path(file)
        for file in files
    ]

    images = prepare_image_list(
        image_paths
    )

    if not images:

        show_error(
            "No Images",
            "No supported image files selected.",
        )

        return

    clear_image_list(app)

    app.image_paths = images

    for image in images:

        add_image_to_list(
            app,
            image.name,
        )

    set_status(
        app,
        f"{len(images)} image(s) loaded.",
    )


def on_remove_selected(app) -> None:
    """
    Remove selected images from the list.
    """

    selected = list(
        app.lst_images.curselection()
    )

    if not selected:
        return

    for index in reversed(selected):

        del app.image_paths[index]
        app.lst_images.delete(index)

    set_status(
        app,
        "Selected image(s) removed.",
    )


def on_browse_output(app) -> None:
    """
    Select output folder.
    """

    folder = filedialog.askdirectory(
        title="Select Output Folder"
    )

    if folder:

        app.output_folder.set(
            folder
        )

        set_status(
            app,
            "Output folder selected.",
        )


def on_resize_images(app) -> None:
    """
    Resize selected images.
    """

    images = getattr(
        app,
        "image_paths",
        [],
    )

    valid, message = validate_resize_request(
        images,
        app.resize_value.get(),
        app.output_folder.get(),
        app.filename_suffix.get(),
    )

    if not valid:

        show_error(
            "Validation Error",
            message,
        )

        return

    try:

        results = process_images(
            image_paths=images,
            output_folder=Path(
                app.output_folder.get()
            ),
            resize_method=app.resize_method.get(),
            resize_value=int(
                app.resize_value.get()
            ),
            suffix=app.filename_suffix.get(),
        )

        set_status(
            app,
            (
                f"Completed: "
                f"{results['successful']} successful, "
                f"{results['failed']} failed."
            ),
        )

        show_info(
            "Resize Complete",
            (
                f"Processed {results['total']} image(s).\n"
                f"Successful: {results['successful']}\n"
                f"Failed: {results['failed']}"
            ),
        )

    except Exception as ex:

        show_error(
            "Resize Error",
            str(ex),
        )


def on_close_application(app) -> None:
    """
    Close application.
    """

    app.root.destroy()