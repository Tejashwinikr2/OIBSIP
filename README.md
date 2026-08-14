# Secure Password Generator

## Overview

Secure Password Generator is a Python desktop application that helps users create strong passwords according to their preferred length and character requirements. The application provides a simple graphical interface along with password strength analysis, entropy estimation, clipboard support, and recent password history.

The project focuses on secure password generation using Python's `secrets` module rather than the standard `random` module.

## Features

* Generate secure random passwords
* Select password length from 8 to 64 characters
* Include uppercase letters
* Include lowercase letters
* Include numbers
* Include special symbols
* Require at least two character categories
* Exclude visually similar characters
* Display password strength
* Display numerical strength score
* Calculate estimated password entropy
* Copy generated passwords to the clipboard
* Store the five most recently generated passwords
* Clear password history
* Dark-themed graphical user interface

## Technologies Used

* **Python 3.14** — Application development
* **Tkinter** — Graphical user interface
* **secrets** — Secure random password generation
* **string** — Standard character sets
* **math** — Entropy calculation
* **Pyperclip** — Clipboard functionality

## Project Structure

```text
PasswordGenerator/
│
├── app.py
├── constants.py
├── generator.py
├── strength.py
├── requirements.txt
├── README.md
└── screenshots/
```

### File Description

| File               | Purpose                                                         |
| ------------------ | --------------------------------------------------------------- |
| `app.py`           | Controls the graphical interface and application workflow       |
| `constants.py`     | Stores application settings, colors, character sets, and limits |
| `generator.py`     | Contains the secure password-generation logic                   |
| `strength.py`      | Calculates password strength and estimated entropy              |
| `requirements.txt` | Lists external Python dependencies                              |
| `README.md`        | Project documentation                                           |
| `screenshots/`     | Contains application screenshots                                |

## Installation

### Prerequisites

* Python 3.14
* Visual Studio Code or another Python-compatible IDE

### Install Dependencies

Open a terminal inside the project directory and run:

```bash
python -m pip install -r requirements.txt
```

### Run the Application

```bash
python app.py
```

## How to Use

1. Launch the application.
2. Select the required password length using the slider.
3. Select at least two character categories.
4. Choose uppercase letters, lowercase letters, numbers, and/or symbols.
5. Enable **Exclude Similar Characters** when needed.
6. Click **Generate Password**.
7. The generated password will appear in the output field.
8. Review the displayed strength score and entropy.
9. Use **Copy Password** to copy the password to the clipboard.
10. Review previously generated passwords in the history section.
11. Use **Clear History** when you want to remove the stored password history.

## Security Approach

The application uses Python's `secrets` module for password generation. This module is designed for security-sensitive random values and is more appropriate for password generation than the general-purpose `random` module.

When multiple character categories are selected, the generator first adds a character from each selected category and then fills the remaining positions from the combined character pool. The resulting characters are securely shuffled before the password is returned.

## Password Strength Analysis

The application evaluates the generated password using factors including:

* Password length
* Lowercase characters
* Uppercase characters
* Numeric characters
* Special characters

The interface displays:

* Strength category
* Numerical strength score
* Estimated entropy in bits

## Screenshots

The `screenshots` folder contains images demonstrating the application's functionality.

Recommended screenshots include:

1. Main application interface
2. Generated password with strength analysis
3. Password history

## Future Improvements

Possible future improvements include:

* Password visibility toggle
* Custom symbol selection
* Passphrase generation
* Light and dark theme switching
* Encrypted password-history storage
* Additional password-quality checks

## Author

**Tejashwini**

Python Programming Internship Project
**Oasis Infobyte**
