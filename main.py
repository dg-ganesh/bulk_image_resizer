"""
main.py

Application entry point for Bulk Image Resizer.
"""

from gui.main_window import BulkImageResizerApp


def main() -> None:
    """
    Launch the application.
    """

    app = BulkImageResizerApp()
    app.run()


if __name__ == "__main__":
    main()