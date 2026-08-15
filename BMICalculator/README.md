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

File Description

File
Purpose
app.py
Controls the graphical interface and application workflow

bmi.py
Contains BMI calculation and category classification logic

database.py
Handles SQLite database creation, saving, and retrieving BMI records

bmi_history.db
SQLite database used to store BMI records

requirements.txt
Lists external Python dependencies

README.md
Project documentation

screenshots/
Contains screenshots of the working application

BMI Formula

BMI is calculated using:
Plain text
BMI = Weight (kg) / Height² (m)
For example:
Plain text
Weight = 60 kg
Height = 1.65 m

BMI = 60 / (1.65 × 1.65)
BMI = 22.04
The result is classified as Normal Weight.

Installation
Prerequisites
Python 3.14
Visual Studio Code or another Python-compatible IDE

Install Dependencies
Open a terminal inside the project directory and run:

Bash
python -m pip install -r requirements.txt
Run the Application

Bash
python app.py

How to Use
Launch the BMI Calculator.
Enter the user's name.
Enter weight in kilograms.
Enter height in meters.
Click Calculate BMI.

The BMI value and category are displayed.
The BMI record is stored in the local SQLite database.
Previous records can be retrieved for the selected user.
BMI history can be used to visualize changes over time.

Input Validation
The application validates user input and displays an error message when:
Name is empty
Weight is empty
Height is empty
Weight is not numeric
Height is not numeric
Weight is zero or negative
Height is zero or negative

Database
The application uses SQLite for local data storage.
Each BMI record contains:
Record ID
User name
Weight
Height
BMI
BMI category

Date and time
The database allows BMI records to be associated with different users and retrieved for historical analysis.

BMI Trend
The application can visualize a user's BMI records over time using a line chart.
The trend chart helps users observe changes in their BMI across recorded measurements.

Screenshots

Screenshots demonstrating the working BMI Calculator application are stored in the screenshots/ folder.

Recommended screenshots include:
Main BMI Calculator interface
BMI calculation result
BMI history
BMI trend chart

Future Improvements
Possible future improvements include:
User profile management
Additional health-related measurements
Export BMI history to CSV
Improved visualization options
Date-range filtering
Dark and light theme support

Author
Tejashwini
Python Programming Internship Project
Oasis Infobyte
