"""
layout_widgets.py

Layout manager for the Bulk Image Resizer GUI.

This module is responsible ONLY for positioning widgets.
"""


def layout_widgets(app) -> None:
    """
    Arrange all widgets in the main window.
    """

    # ==========================================================
    # Root Window Layout
    # ==========================================================

    app.root.columnconfigure(0, weight=1)

    app.root.rowconfigure(0, weight=3)
    app.root.rowconfigure(1, weight=0)
    app.root.rowconfigure(2, weight=0)
    app.root.rowconfigure(3, weight=0)
    app.root.rowconfigure(4, weight=0)

    # ==========================================================
    # Images Section
    # ==========================================================

    app.frm_images.grid(
        row=0,
        column=0,
        sticky="nsew",
        padx=10,
        pady=(10, 5),
    )

    app.frm_images.columnconfigure(0, weight=1)
    app.frm_images.rowconfigure(1, weight=1)

    app.btn_add_images.grid(
        row=0,
        column=0,
        sticky="w",
        padx=(0, 5),
        pady=(0, 10),
    )

    app.btn_remove_selected.grid(
        row=0,
        column=1,
        sticky="w",
        pady=(0, 10),
    )

    app.lst_images.grid(
        row=1,
        column=0,
        columnspan=2,
        sticky="nsew",
    )

    app.scr_images.grid(
        row=1,
        column=2,
        sticky="ns",
    )

    # ==========================================================
    # Resize Section
    # ==========================================================

    app.frm_resize.grid(
        row=1,
        column=0,
        sticky="ew",
        padx=10,
        pady=5,
    )

    app.frm_resize.columnconfigure(1, weight=1)

    app.lbl_method.grid(
        row=0,
        column=0,
        sticky="w",
        padx=(0, 10),
        pady=5,
    )

    app.cmb_method.grid(
        row=0,
        column=1,
        sticky="ew",
        pady=5,
    )

    app.lbl_value.grid(
        row=1,
        column=0,
        sticky="w",
        padx=(0, 10),
        pady=5,
    )

    app.cmb_value.grid(
        row=1,
        column=1,
        sticky="ew",
        pady=5,
    )

    # ==========================================================
    # Output Section
    # ==========================================================

    app.frm_output.grid(
        row=2,
        column=0,
        sticky="ew",
        padx=10,
        pady=5,
    )

    app.frm_output.columnconfigure(1, weight=1)

    app.lbl_output.grid(
        row=0,
        column=0,
        sticky="w",
        padx=(0, 10),
        pady=5,
    )

    app.ent_output.grid(
        row=0,
        column=1,
        sticky="ew",
        pady=5,
    )

    app.btn_browse.grid(
        row=0,
        column=2,
        padx=(10, 0),
        pady=5,
    )

    app.lbl_suffix.grid(
        row=1,
        column=0,
        sticky="w",
        padx=(0, 10),
        pady=5,
    )

    app.ent_suffix.grid(
        row=1,
        column=1,
        sticky="ew",
        pady=5,
    )

    # ==========================================================
    # Action Section
    # ==========================================================

    app.frm_actions.grid(
        row=3,
        column=0,
        sticky="ew",
        padx=10,
        pady=5,
    )

    app.frm_actions.columnconfigure(0, weight=1)

    app.btn_resize.grid(
        row=0,
        column=0,
        pady=5,
    )

    # ==========================================================
    # Status Bar
    # ==========================================================

    app.frm_status.grid(
        row=4,
        column=0,
        sticky="ew",
        padx=10,
        pady=(5, 10),
    )

    app.frm_status.columnconfigure(0, weight=1)

    app.lbl_status.grid(
        row=0,
        column=0,
        sticky="w",
    )