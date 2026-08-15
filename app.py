import tkinter as tk
from tkinter import messagebox

from bmi import calculate_bmi, get_bmi_category


def calculate():
    try:
        name = name_entry.get().strip()
        weight = float(weight_entry.get())
        height = float(height_entry.get())

        if not name:
            messagebox.showerror("Input Error", "Please enter a name.")
            return

        if weight <= 0 or height <= 0:
            messagebox.showerror(
                "Input Error",
                "Weight and height must be greater than zero."
            )
            return

        bmi = calculate_bmi(weight, height)
        category = get_bmi_category(bmi)

        result_label.config(
            text=f"BMI: {bmi:.2f}\nCategory: {category}"
        )

    except ValueError:
        messagebox.showerror(
            "Input Error",
            "Please enter valid numeric values."
        )


# -----------------------------
# Main Window
# -----------------------------

root = tk.Tk()
root.title("BMI Calculator")
root.geometry("500x550")
root.resizable(False, False)
root.configure(bg="#1E1E1E")


# Title
title_label = tk.Label(
    root,
    text="BMI Calculator",
    font=("Segoe UI", 24, "bold"),
    fg="white",
    bg="#1E1E1E"
)
title_label.pack(pady=(30, 10))


subtitle_label = tk.Label(
    root,
    text="Calculate and track your Body Mass Index",
    font=("Segoe UI", 11),
    fg="#BDBDBD",
    bg="#1E1E1E"
)
subtitle_label.pack(pady=(0, 25))


# Name
name_label = tk.Label(
    root,
    text="Name",
    font=("Segoe UI", 12),
    fg="white",
    bg="#1E1E1E"
)
name_label.pack()

name_entry = tk.Entry(
    root,
    font=("Segoe UI", 12),
    width=30
)
name_entry.pack(pady=8)


# Weight
weight_label = tk.Label(
    root,
    text="Weight (kg)",
    font=("Segoe UI", 12),
    fg="white",
    bg="#1E1E1E"
)
weight_label.pack(pady=(10, 0))

weight_entry = tk.Entry(
    root,
    font=("Segoe UI", 12),
    width=30
)
weight_entry.pack(pady=8)


# Height
height_label = tk.Label(
    root,
    text="Height (m)",
    font=("Segoe UI", 12),
    fg="white",
    bg="#1E1E1E"
)
height_label.pack(pady=(10, 0))

height_entry = tk.Entry(
    root,
    font=("Segoe UI", 12),
    width=30
)
height_entry.pack(pady=8)


# Calculate Button
calculate_button = tk.Button(
    root,
    text="Calculate BMI",
    font=("Segoe UI", 12, "bold"),
    bg="#4CAF50",
    fg="white",
    padx=20,
    pady=10,
    command=calculate
)
calculate_button.pack(pady=25)


# Result
result_label = tk.Label(
    root,
    text="BMI: --\nCategory: --",
    font=("Segoe UI", 16, "bold"),
    fg="#FFC107",
    bg="#1E1E1E"
)
result_label.pack(pady=15)


root.mainloop()