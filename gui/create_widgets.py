"""
create_widgets.py

Creates all GUI widgets for the Bulk Image Resizer.

This module is responsible ONLY for creating widgets.
No layout and no event binding should be done here.
"""

import tkinter as tk
from tkinter import ttk

from settings import (
    DEFAULT_OUTPUT_FOLDER,
    DEFAULT_FILENAME_SUFFIX,
    DEFAULT_RESIZE_METHOD,
    DEFAULT_RESIZE_VALUE,
    RESIZE_METHODS,
    PERCENTAGE_VALUES,
)


def create_widgets(app) -> None:
    """
    Create all widgets used by the application.

    Parameters
    ----------
    app : BulkImageResizerApp
        Main application instance.
    """

    # ==========================================================
    # Variables
    # ==========================================================

    app.resize_method = tk.StringVar(
        value=DEFAULT_RESIZE_METHOD
    )

    app.resize_value = tk.StringVar(
        value=DEFAULT_RESIZE_VALUE
    )

    app.output_folder = tk.StringVar(
        value=DEFAULT_OUTPUT_FOLDER
    )

    app.filename_suffix = tk.StringVar(
        value=DEFAULT_FILENAME_SUFFIX
    )

    app.status_text = tk.StringVar(
        value="Ready"
    )

    # ==========================================================
    # Images Section
    # ==========================================================

    app.frm_images = ttk.LabelFrame(
        app.root,
        text="Images",
        padding=10,
    )

    app.btn_add_images = ttk.Button(
        app.frm_images,
        text="Add Images",
    )

    app.btn_remove_selected = ttk.Button(
        app.frm_images,
        text="Remove Selected",
    )

    app.lst_images = tk.Listbox(
        app.frm_images,
        selectmode=tk.EXTENDED,
        height=12,
    )

    app.scr_images = ttk.Scrollbar(
        app.frm_images,
        orient="vertical",
        command=app.lst_images.yview,
    )

    app.lst_images.configure(
        yscrollcommand=app.scr_images.set
    )

    # ==========================================================
    # Resize Section
    # ==========================================================

    app.frm_resize = ttk.LabelFrame(
        app.root,
        text="Resize Options",
        padding=10,
    )

    app.lbl_method = ttk.Label(
        app.frm_resize,
        text="Resize Mode",
    )

    app.cmb_method = ttk.Combobox(
        app.frm_resize,
        state="readonly",
        width=25,
        textvariable=app.resize_method,
        values=RESIZE_METHODS,
    )

    app.lbl_value = ttk.Label(
        app.frm_resize,
        text="Value",
    )

    app.cmb_value = ttk.Combobox(
        app.frm_resize,
        state="readonly",
        width=25,
        textvariable=app.resize_value,
        values=PERCENTAGE_VALUES,
    )

    # ==========================================================
    # Output Section
    # ==========================================================

    app.frm_output = ttk.LabelFrame(
        app.root,
        text="Output",
        padding=10,
    )

    app.lbl_output = ttk.Label(
        app.frm_output,
        text="Output Folder",
    )

    app.ent_output = ttk.Entry(
        app.frm_output,
        textvariable=app.output_folder,
    )

    app.btn_browse = ttk.Button(
        app.frm_output,
        text="Browse...",
    )

    app.lbl_suffix = ttk.Label(
        app.frm_output,
        text="Filename Suffix",
    )

    app.ent_suffix = ttk.Entry(
        app.frm_output,
        width=20,
        textvariable=app.filename_suffix,
    )

    # ==========================================================
    # Action Section
    # ==========================================================

    app.frm_actions = ttk.Frame(
        app.root,
        padding=10,
    )

    app.btn_resize = ttk.Button(
        app.frm_actions,
        text="Resize Images",
        width=22,
    )

    # ==========================================================
    # Status Bar
    # ==========================================================

    app.frm_status = ttk.Frame(
        app.root,
        padding=(5, 5),
    )

    app.lbl_status = ttk.Label(
        app.frm_status,
        textvariable=app.status_text,
        anchor="w",
    )