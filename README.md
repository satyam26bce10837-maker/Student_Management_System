# Student Productivity & Academic Management System

## Overview

The Student Productivity & Academic Management System is a Python-based console application developed to manage student academic information.

The system allows the user to store student details, manage subjects and marks, record attendance, calculate academic results, and generate a consolidated academic report.

The project uses JSON files to store data so that information remains available even after the program is closed.

## Features

- Add, view, update, and delete student details
- Add, view, update, and delete subjects and marks
- Validate marks between 0 and 100
- Calculate total marks, percentage, and grade
- Record and view attendance
- Calculate attendance percentage
- Display a warning when attendance is below 75%
- Generate a consolidated student academic report
- Store data permanently using JSON files
- Handle invalid user input using exception handling

## Technologies Used

- Python 3
- JSON
- File Handling
- Functions
- Lists and Dictionaries
- Exception Handling
- Python Modules
- Git
- GitHub

## Project Structure

```text
Student_Management_System/
│
├── main.py
├── student.py
├── subjects.py
├── attendance.py
├── reports.py
├── storage.py
├── .gitignore
│
└── data/
    ├── students.json
    ├── subjects.json
    └── attendance.json
```

## Description of Modules
## main.py

Contains the main menu and controls the flow of the application.

## student.py

Handles student-related operations such as adding, viewing, updating, and deleting student information.

## subjects.py

Handles subjects and marks. It also calculates total marks, percentage, and grade.

## attendance.py

Stores attendance records and calculates attendance percentages.

## reports.py

Generates a consolidated academic report containing student information, subjects and marks, academic result, and attendance.

## storage.py

Contains functions for loading data from JSON files and saving data back to JSON files.

## How to Run
- Install Python 3 on the computer.
- Download or clone this repository.
- Open the project folder in VS Code or a terminal.
- Run the following command:
python main.py
- Use the menu displayed in the terminal to operate the system.

## Data Storage

The application stores information in JSON files inside the data folder.

The three files are:

- students.json
- subjects.json
- attendance.json

This allows the stored information to remain available between program runs.

## Validation and Error Handling

The system checks user input to prevent invalid data.

Examples include:

- Age must be a valid positive number.
- Marks must be between 0 and 100.
- Total attendance classes must be greater than 0.
- Attended classes cannot be greater than total classes.
- Empty required fields are rejected where validation is implemented.
- Invalid numeric input is handled using try-except.

## Testing

The application was manually tested using valid and invalid inputs.

The following areas were tested:

- Student data entry
- Student update and deletion
- Subject and marks management
- Marks validation
- Attendance validation
- Attendance percentage calculation
- Academic result calculation
- Academic report generation
- JSON data persistence

## Future Enhancements

Possible future improvements include:

- Student ID-based record management
- Linking subjects and attendance to individual students
- Search functionality
- Graphical user interface
- More detailed reports
- Automated testing
- Database integration

## Author

Satyam

B.Tech CSE
VIT Bhopal University