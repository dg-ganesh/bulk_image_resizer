"""
main_window.py

Main application window for Bulk Image Resizer.

This module is responsible only for:
- Creating the root Tk window
- Configuring the application window
- Initializing GUI variables
- Creating widgets
- Laying out widgets
- Binding events
- Starting the application

Business logic is intentionally kept outside this module.
"""

import tkinter as tk

from settings import (
    WINDOW_TITLE,
    WINDOW_WIDTH,
    WINDOW_HEIGHT,
    WINDOW_MIN_WIDTH,
    WINDOW_MIN_HEIGHT,
)

from gui.create_widgets import create_widgets
from gui.layout_widgets import layout_widgets
from gui.event_handlers import bind_events


class BulkImageResizerApp:
    """
    Main application class.
    """

    def __init__(self) -> None:

        self.root = tk.Tk()

        self._configure_window()

        create_widgets(self)
        layout_widgets(self)
        bind_events(self)

    def _configure_window(self) -> None:
        """
        Configure the main application window.
        """

        self.root.title(WINDOW_TITLE)

        self.root.geometry(
            f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}"
        )

        self.root.minsize(
            WINDOW_MIN_WIDTH,
            WINDOW_MIN_HEIGHT,
        )

    def run(self) -> None:
        """
        Start the Tkinter event loop.
        """

        self.root.mainloop()