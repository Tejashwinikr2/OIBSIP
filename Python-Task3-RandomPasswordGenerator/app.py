import tkinter as tk
from tkinter import ttk, messagebox
import pyperclip

from generator import generate_password
from strength import password_strength

from constants import (
    WINDOW_TITLE,
    WINDOW_WIDTH,
    WINDOW_HEIGHT,
    TITLE_FONT,
    LABEL_FONT,
    BUTTON_FONT,
    ENTRY_FONT,
    BG_COLOR,
    FG_COLOR,
    GREEN,
    BLUE,
    RED,
    MIN_LENGTH,
    MAX_LENGTH,
    MAX_HISTORY,
)


# ============================================================
# MAIN WINDOW
# ============================================================

root = tk.Tk()

root.title(WINDOW_TITLE)
root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
root.configure(bg=BG_COLOR)
root.resizable(False, False)


# Center window
root.update_idletasks()

x = (root.winfo_screenwidth() - WINDOW_WIDTH) // 2
y = (root.winfo_screenheight() - WINDOW_HEIGHT) // 2

root.geometry(
    f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}+{x}+{y}"
)


# ============================================================
# VARIABLES
# ============================================================

use_upper = tk.BooleanVar(value=True)
use_lower = tk.BooleanVar(value=True)
use_numbers = tk.BooleanVar(value=True)
use_symbols = tk.BooleanVar(value=True)

exclude_similar = tk.BooleanVar(value=False)

password_length = tk.IntVar(value=16)

password_history = []


# ============================================================
# TKINTER STYLES
# ============================================================

style = ttk.Style()

style.theme_use("clam")

style.configure(
    "TCheckbutton",
    background=BG_COLOR,
    foreground=FG_COLOR,
    font=("Segoe UI", 10),
)

style.map(
    "TCheckbutton",
    background=[
        ("active", BG_COLOR)
    ],
    foreground=[
        ("active", FG_COLOR)
    ],
)


# Strength bar styles

style.configure(
    "red.Horizontal.TProgressbar",
    troughcolor="#333333",
    background=RED,
)

style.configure(
    "orange.Horizontal.TProgressbar",
    troughcolor="#333333",
    background="#2196F3",
)

style.configure(
    "green.Horizontal.TProgressbar",
    troughcolor="#333333",
    background=GREEN,
)


# ============================================================
# TITLE
# ============================================================

title = tk.Label(
    root,
    text="🔐 Secure Password Generator",
    font=TITLE_FONT,
    bg=BG_COLOR,
    fg=FG_COLOR,
)

title.pack(pady=(25, 5))


subtitle = tk.Label(
    root,
    text="Generate strong and secure passwords",
    font=("Segoe UI", 10),
    bg=BG_COLOR,
    fg="#AAAAAA",
)

subtitle.pack(pady=(0, 15))


# ============================================================
# PASSWORD LENGTH
# ============================================================

length_label = tk.Label(
    root,
    text="Password Length",
    font=LABEL_FONT,
    bg=BG_COLOR,
    fg=FG_COLOR,
)

length_label.pack()


length_value = tk.Label(
    root,
    text="16 characters",
    font=("Segoe UI", 10, "bold"),
    bg=BG_COLOR,
    fg=GREEN,
)

length_value.pack(pady=2)


def update_length(value):
    length_value.config(
        text=f"{int(float(value))} characters"
    )


length_slider = tk.Scale(
    root,
    from_=MIN_LENGTH,
    to=MAX_LENGTH,
    orient="horizontal",
    variable=password_length,
    command=update_length,
    length=350,
    bg=BG_COLOR,
    fg=FG_COLOR,
    troughcolor="#444444",
    highlightthickness=0,
    activebackground=GREEN,
)

length_slider.pack()


# ============================================================
# CHARACTER OPTIONS
# ============================================================

options_label = tk.Label(
    root,
    text="Character Options",
    font=LABEL_FONT,
    bg=BG_COLOR,
    fg=FG_COLOR,
)

options_label.pack(pady=(12, 5))


options_frame = tk.Frame(
    root,
    bg=BG_COLOR,
)

options_frame.pack()


ttk.Checkbutton(
    options_frame,
    text="Uppercase (A-Z)",
    variable=use_upper,
).grid(
    row=0,
    column=0,
    padx=15,
    pady=3,
    sticky="w",
)


ttk.Checkbutton(
    options_frame,
    text="Lowercase (a-z)",
    variable=use_lower,
).grid(
    row=0,
    column=1,
    padx=15,
    pady=3,
    sticky="w",
)


ttk.Checkbutton(
    options_frame,
    text="Numbers (0-9)",
    variable=use_numbers,
).grid(
    row=1,
    column=0,
    padx=15,
    pady=3,
    sticky="w",
)


ttk.Checkbutton(
    options_frame,
    text="Symbols (!@#$)",
    variable=use_symbols,
).grid(
    row=1,
    column=1,
    padx=15,
    pady=3,
    sticky="w",
)


ttk.Checkbutton(
    options_frame,
    text="Exclude similar characters",
    variable=exclude_similar,
).grid(
    row=2,
    column=0,
    columnspan=2,
    pady=5,
)


# ============================================================
# PASSWORD OUTPUT
# ============================================================

password_label = tk.Label(
    root,
    text="Generated Password",
    font=LABEL_FONT,
    bg=BG_COLOR,
    fg=FG_COLOR,
)

password_label.pack(pady=(12, 4))


password_entry = tk.Entry(
    root,
    font=ENTRY_FONT,
    width=42,
    justify="center",
    bg="#2B2B2B",
    fg=FG_COLOR,
    insertbackground=FG_COLOR,
    relief="flat",
)

password_entry.pack(ipady=7)


# ============================================================
# STRENGTH
# ============================================================

strength_label = tk.Label(
    root,
    text="Strength: -",
    font=("Segoe UI", 11, "bold"),
    bg=BG_COLOR,
    fg=FG_COLOR,
)

strength_label.pack(pady=(10, 4))


strength_bar = ttk.Progressbar(
    root,
    length=320,
    maximum=100,
    value=0,
    style="red.Horizontal.TProgressbar",
)

strength_bar.pack()


entropy_label = tk.Label(
    root,
    text="Entropy: 0 bits",
    font=("Segoe UI", 9),
    bg=BG_COLOR,
    fg="#AAAAAA",
)

entropy_label.pack(pady=3)


# ============================================================
# HISTORY
# ============================================================

history_label = tk.Label(
    root,
    text="Recent Passwords",
    font=("Segoe UI", 11, "bold"),
    bg=BG_COLOR,
    fg=FG_COLOR,
)

history_label.pack(pady=(8, 3))


history_box = tk.Listbox(
    root,
    width=48,
    height=4,
    bg="#2B2B2B",
    fg=FG_COLOR,
    selectbackground="#555555",
    selectforeground=FG_COLOR,
    relief="flat",
    font=("Consolas", 10),
)

history_box.pack()


def update_history():

    history_box.delete(
        0,
        tk.END
    )

    for password in password_history:
        history_box.insert(
            tk.END,
            password
        )


def clear_history():

    password_history.clear()

    history_box.delete(
        0,
        tk.END
    )


# ============================================================
# GENERATE PASSWORD
# ============================================================

def generate():

    selected_types = sum(
        [
            use_upper.get(),
            use_lower.get(),
            use_numbers.get(),
            use_symbols.get(),
        ]
    )

    # Require at least two character types
    if selected_types < 2:

        messagebox.showwarning(
            "Character Selection",
            "Please select at least two character types.",
        )

        return

    try:

        password = generate_password(
            length=password_length.get(),
            use_upper=use_upper.get(),
            use_lower=use_lower.get(),
            use_numbers=use_numbers.get(),
            use_symbols=use_symbols.get(),
            exclude_similar=exclude_similar.get(),
        )

        if password is None:

            messagebox.showerror(
                "Error",
                "Unable to generate password.",
            )

            return

        # Display password
        password_entry.delete(
            0,
            tk.END
        )

        password_entry.insert(
            0,
            password
        )

        # Calculate strength
        score, level, color, entropy = password_strength(
            password
        )

        # Update strength
        strength_label.config(
            text=f"Strength: {level} ({score}/100)",
            fg=color,
        )

        strength_bar["value"] = score

        # Change progress bar color
        if score < 40:

            strength_bar.configure(
                style="red.Horizontal.TProgressbar"
            )

        elif score < 70:

            strength_bar.configure(
                style="orange.Horizontal.TProgressbar"
            )

        else:

            strength_bar.configure(
                style="green.Horizontal.TProgressbar"
            )

        # Entropy
        entropy_label.config(
            text=f"Entropy: {entropy:.2f} bits"
        )

        # Add to history
        password_history.insert(
            0,
            password
        )

        # Keep last 5
        if len(password_history) > MAX_HISTORY:
            password_history.pop()

        update_history()

    except Exception as error:

        messagebox.showerror(
            "Error",
            f"Something went wrong:\n{error}",
        )


# ============================================================
# COPY PASSWORD
# ============================================================

def copy_password():

    password = password_entry.get()

    if not password:

        messagebox.showwarning(
            "No Password",
            "Generate a password first.",
        )

        return

    try:

        pyperclip.copy(password)

        copy_button.config(
            text="✓ Copied!"
        )

        root.after(
            2000,
            lambda: copy_button.config(
                text="Copy Password"
            )
        )

    except Exception as error:

        messagebox.showerror(
            "Copy Error",
            f"Unable to copy password:\n{error}",
        )


# ============================================================
# BUTTONS
# ============================================================

button_frame = tk.Frame(
    root,
    bg=BG_COLOR,
)

button_frame.pack(pady=10)


generate_button = tk.Button(
    button_frame,
    text="Generate Password",
    command=generate,
    font=BUTTON_FONT,
    bg=GREEN,
    fg="white",
    activebackground="#388E3C",
    activeforeground="white",
    relief="flat",
    width=20,
    cursor="hand2",
)

generate_button.grid(
    row=0,
    column=0,
    padx=4,
)


copy_button = tk.Button(
    button_frame,
    text="Copy Password",
    command=copy_password,
    font=BUTTON_FONT,
    bg=BLUE,
    fg="white",
    activebackground="#1976D2",
    activeforeground="white",
    relief="flat",
    width=17,
    cursor="hand2",
)

copy_button.grid(
    row=0,
    column=1,
    padx=4,
)


clear_button = tk.Button(
    button_frame,
    text="Clear History",
    command=clear_history,
    font=BUTTON_FONT,
    bg=RED,
    fg="white",
    activebackground="#D32F2F",
    activeforeground="white",
    relief="flat",
    width=15,
    cursor="hand2",
)

clear_button.grid(
    row=0,
    column=2,
    padx=4,
)


# ============================================================
# START APPLICATION
# ============================================================

root.mainloop()
