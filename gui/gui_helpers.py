"""
gui_helpers.py

Reusable helper functions for the Tkinter GUI.

These functions are GUI-specific and should not contain
business logic.
"""

from tkinter import messagebox

from settings import STATUS_READY


def set_status(app, message: str) -> None:
    """
    Update the application's status bar.

    Parameters
    ----------
    app : BulkImageResizerApp
        Main application instance.

    message : str
        Status message.
    """

    app.status_text.set(message)


def clear_status(app) -> None:
    """
    Reset the status bar.
    """

    app.status_text.set(STATUS_READY)


def show_info(title: str, message: str) -> None:
    """
    Display an information message.
    """

    messagebox.showinfo(
        title,
        message,
    )


def show_warning(title: str, message: str) -> None:
    """
    Display a warning message.
    """

    messagebox.showwarning(
        title,
        message,
    )


def show_error(title: str, message: str) -> None:
    """
    Display an error message.
    """

    messagebox.showerror(
        title,
        message,
    )


def ask_yes_no(title: str, message: str) -> bool:
    """
    Display a Yes/No confirmation dialog.

    Returns
    -------
    bool
        True if Yes was selected.
    """

    return messagebox.askyesno(
        title,
        message,
    )


def clear_image_list(app) -> None:
    """
    Remove all items from the image list.
    """

    app.lst_images.delete(0, "end")


def add_image_to_list(app, image_name: str) -> None:
    """
    Add an image to the list box.

    Parameters
    ----------
    image_name : str
        File name to display.
    """

    app.lst_images.insert(
        "end",
        image_name,
    )


def remove_selected_images(app) -> None:
    """
    Remove all selected items from the image list.
    """

    selected = list(
        app.lst_images.curselection()
    )

    selected.reverse()

    for index in selected:
        app.lst_images.delete(index)


def get_selected_count(app) -> int:
    """
    Return the number of selected images.
    """

    return len(
        app.lst_images.curselection()
    )


def get_total_images(app) -> int:
    """
    Return total number of images loaded.
    """

    return app.lst_images.size()


def update_window_title(app, title: str) -> None:
    """
    Update the application window title.
    """

    app.root.title(title)