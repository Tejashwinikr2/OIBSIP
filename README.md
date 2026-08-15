# BMI Calculator

## Overview

BMI Calculator is a Python desktop application that calculates a user's Body Mass Index (BMI) based on their weight and height.

The application provides a graphical interface for entering user details, calculating BMI, displaying the BMI category, and storing BMI records for future reference.

## Features

- User-friendly graphical interface
- Enter user's name
- Enter weight in kilograms
- Enter height in meters
- Calculate BMI
- Display BMI rounded to two decimal places
- Classify BMI into health categories
- Input validation for invalid values
- Store BMI records using SQLite
- Support records for multiple users
- Retrieve previous BMI records
- BMI history tracking
- BMI trend visualization
- Error handling for database operations

## BMI Categories

The application classifies BMI values as follows:

| BMI Range | Category |
|---|---|
| Below 18.5 | Underweight |
| 18.5 – 24.9 | Normal Weight |
| 25 – 29.9 | Overweight |
| 30 and above | Obesity |

## Technologies Used

- **Python 3.14** — Application development
- **Tkinter** — Graphical user interface
- **SQLite** — Local database storage
- **Matplotlib** — BMI trend visualization

## Project Structure

```text
Python-Task2-BMICalculator/
│
├── app.py
├── bmi.py
├── database.py
├── bmi_history.db
├── requirements.txt
├── README.md
└── screenshots/
