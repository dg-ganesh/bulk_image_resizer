"""
settings.py

Application-wide configuration for the Bulk Image Resizer project.
Keep all configurable values here to avoid hardcoding them throughout
the application.
"""

from pathlib import Path

# ---------------------------------------------------------------------
# Application Information
# ---------------------------------------------------------------------

APP_NAME = "Bulk Image Resizer"
APP_VERSION = "1.0.0"
APP_AUTHOR = "DG Ganesh"

APP_DESCRIPTION = (
    "Resize single or multiple images while maintaining aspect ratio."
)

# ---------------------------------------------------------------------
# Window Settings
# ---------------------------------------------------------------------

WINDOW_TITLE = f"{APP_NAME} v{APP_VERSION}"

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

WINDOW_MIN_WIDTH = 700
WINDOW_MIN_HEIGHT = 500

# ---------------------------------------------------------------------
# Supported Image Formats
# ---------------------------------------------------------------------

SUPPORTED_IMAGE_FORMATS = (
    "*.jpg",
    "*.jpeg",
    "*.png",
    "*.bmp",
    "*.tif",
    "*.tiff",
    "*.webp",
)

FILE_DIALOG_FILTERS = [
    (
        "Image Files",
        "*.jpg *.jpeg *.png *.bmp *.tif *.tiff *.webp",
    ),
    ("JPEG Images", "*.jpg *.jpeg"),
    ("PNG Images", "*.png"),
    ("Bitmap Images", "*.bmp"),
    ("TIFF Images", "*.tif *.tiff"),
    ("WebP Images", "*.webp"),
    ("All Files", "*.*"),
]

# ---------------------------------------------------------------------
# Resize Methods
# ---------------------------------------------------------------------

RESIZE_METHODS = [
    "Percentage",
    "Standard Size",
]

DEFAULT_RESIZE_METHOD = "Percentage"

PERCENTAGE_VALUES = [
    "25",
    "50",
    "75",
    "80",
    "90",
    "100",
    "125",
    "150",
    "200",
]

DEFAULT_RESIZE_VALUE = "80"

STANDARD_IMAGE_SIZES = {
    "320 × 240 (QVGA)": (320, 240),
    "640 × 480 (VGA)": (640, 480),
    "800 × 600 (SVGA)": (800, 600),
    "1024 × 768 (XGA)": (1024, 768),
    "1280 × 720 (HD)": (1280, 720),
    "1366 × 768 (WXGA)": (1366, 768),
    "1600 × 900 (HD+)": (1600, 900),
    "1920 × 1080 (Full HD)": (1920, 1080),
    "2560 × 1440 (2K)": (2560, 1440),
    "3840 × 2160 (4K)": (3840, 2160),
}

DEFAULT_STANDARD_SIZE = "1920 × 1080 (Full HD)"

DEFAULT_FILENAME_SUFFIX = "_resized"

ALLOW_UPSCALING = False

# ---------------------------------------------------------------------
# Output Settings
# ---------------------------------------------------------------------

DEFAULT_OUTPUT_FOLDER = str(
    Path.home() / "Pictures"
)

# ---------------------------------------------------------------------
# Status Messages
# ---------------------------------------------------------------------

STATUS_READY = "Ready"

STATUS_PROCESSING = "Processing..."

STATUS_COMPLETED = "Completed Successfully"

STATUS_FAILED = "Operation Failed"

# ---------------------------------------------------------------------
# Future Feature Flags
# ---------------------------------------------------------------------

ENABLE_DRAG_DROP = False

ENABLE_DARK_THEME = False

ENABLE_IMAGE_PREVIEW = False

ENABLE_METADATA_OPTIONS = False