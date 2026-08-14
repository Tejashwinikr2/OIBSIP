import string

# -----------------------------
# Window Settings
# -----------------------------

WINDOW_TITLE = "Secure Password Generator"
WINDOW_WIDTH = 700
WINDOW_HEIGHT = 700


# -----------------------------
# Fonts
# -----------------------------

TITLE_FONT = ("Segoe UI", 22, "bold")
LABEL_FONT = ("Segoe UI", 11)
BUTTON_FONT = ("Segoe UI", 10, "bold")
ENTRY_FONT = ("Consolas", 14)


# -----------------------------
# Colors
# -----------------------------

BG_COLOR = "#1E1E1E"
FG_COLOR = "#FFFFFF"

GREEN = "#4CAF50"
BLUE = "#2196F3"
RED = "#F44336"
ORANGE = "#FF9800"


# -----------------------------
# Character Sets
# -----------------------------

UPPERCASE = string.ascii_uppercase
LOWERCASE = string.ascii_lowercase
NUMBERS = string.digits
SYMBOLS = string.punctuation


# -----------------------------
# Similar Characters
# -----------------------------

SIMILAR = "O0oIl1|"


# -----------------------------
# Password Limits
# -----------------------------

MIN_LENGTH = 8
MAX_LENGTH = 64


# -----------------------------
# Password History
# -----------------------------

MAX_HISTORY = 5