"""
event_handlers.py

Binds GUI events to callback functions.

This module is responsible ONLY for event binding.
"""

from gui.callbacks import (
    on_add_images,
    on_remove_selected,
    on_browse_output,
    on_resize_images,
    on_close_application,
    update_resize_values,
)


def bind_events(app) -> None:
    """
    Bind all widget events.

    Parameters
    ----------
    app : BulkImageResizerApp
        Main application instance.
    """

    # ==========================================================
    # Buttons
    # ==========================================================

    app.btn_add_images.configure(
        command=lambda: on_add_images(app)
    )

    app.btn_remove_selected.configure(
        command=lambda: on_remove_selected(app)
    )

    app.btn_browse.configure(
        command=lambda: on_browse_output(app)
    )

    app.btn_resize.configure(
        command=lambda: on_resize_images(app)
    )

    # ==========================================================
    # Resize Mode
    # ==========================================================

    app.cmb_method.bind(
        "<<ComboboxSelected>>",
        lambda event: update_resize_values(app),
    )

    # Initialize the Value dropdown
    update_resize_values(app)

    # ==========================================================
    # Listbox Events
    # ==========================================================

    app.lst_images.bind(
        "<<ListboxSelect>>",
        lambda event: None,
    )

    app.lst_images.bind(
        "<Delete>",
        lambda event: on_remove_selected(app),
    )

    app.lst_images.bind(
        "<Double-Button-1>",
        lambda event: None,
    )

    # ==========================================================
    # Window Events
    # ==========================================================

    app.root.protocol(
        "WM_DELETE_WINDOW",
        lambda: on_close_application(app),
    )