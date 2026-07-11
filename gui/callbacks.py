"""
callbacks.py

GUI callback functions for Bulk Image Resizer.
"""

from pathlib import Path
from tkinter import filedialog

from settings import (
    PERCENTAGE_VALUES,
    STANDARD_IMAGE_SIZES,
)

from core.image_loader import prepare_image_list
from core.batch_processor import process_images
from core.validation import validate_resize_request

from gui.gui_helpers import (
    add_image_to_list,
    clear_image_list,
    get_selected_count,
    remove_selected_images,
    set_status,
    show_error,
    show_info,
    ask_yes_no,
)


def update_resize_values(app) -> None:
    """
    Update the Value dropdown based on the selected resize mode.
    """

    method = app.resize_method.get()

    if method == "Percentage":

        app.cmb_value["values"] = PERCENTAGE_VALUES
        app.resize_value.set(PERCENTAGE_VALUES[0])

    elif method == "Standard Size":

        sizes = list(STANDARD_IMAGE_SIZES.keys())

        app.cmb_value["values"] = sizes
        app.resize_value.set(sizes[0])


def on_add_images(app) -> None:
    """
    Add images to the application.
    """

    files = filedialog.askopenfilenames(
        title="Select Images",
        filetypes=[
            (
                "Image Files",
                "*.jpg *.jpeg *.png *.bmp *.gif *.webp",
            )
        ],
    )

    if not files:
        return

    image_paths = [
        Path(file)
        for file in files
    ]

    image_paths = prepare_image_list(
        image_paths
    )

    if not image_paths:

        show_error(
            "No Images",
            "No supported image files were selected.",
        )

        return

    app.image_paths = image_paths

    clear_image_list(app)

    for image in image_paths:

        add_image_to_list(
            app,
            image.name,
        )

    set_status(
        app,
        f"{len(image_paths)} image(s) loaded."
    )


def on_remove_selected(app) -> None:
    """
    Remove selected images.
    """

    count = get_selected_count(app)

    if count == 0:

        show_info(
            "Remove Images",
            "Please select one or more images.",
        )

        return

    selected = list(
        app.lst_images.curselection()
    )

    for index in reversed(selected):

        del app.image_paths[index]

    remove_selected_images(app)

    set_status(
        app,
        "Selected image(s) removed."
    )


def on_browse_output(app) -> None:
    """
    Browse for an output folder.
    """

    folder = filedialog.askdirectory(
        title="Select Output Folder"
    )

    if not folder:
        return

    app.output_folder.set(folder)

    set_status(
        app,
        "Output folder selected."
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
        images=images,
        resize_method=app.resize_method.get(),
        resize_value=app.resize_value.get(),
        output_folder=app.output_folder.get(),
        suffix=app.filename_suffix.get(),
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
            resize_value=app.resize_value.get(),
            suffix=app.filename_suffix.get(),
        )

        show_info(
            "Completed",
            (
                f"Total Images : {results['total']}\n"
                f"Successful : {results['successful']}\n"
                f"Failed : {results['failed']}"
            ),
        )

        set_status(
            app,
            (
                f"Completed Successfully "
                f"({results['successful']}/{results['total']})"
            ),
        )

    except Exception as ex:

        show_error(
            "Error",
            str(ex),
        )


def on_close_application(app) -> None:
    """
    Close the application.
    """

    close = ask_yes_no(
        "Exit",
        "Do you want to exit Bulk Image Resizer?",
    )

    if close:
        app.root.destroy()