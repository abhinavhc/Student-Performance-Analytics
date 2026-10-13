# Student Performance Analytics System

## Project Overview
The Student Performance Analytics System is a Python-based project that analyzes student marks and attendance. It generates performance reports using Pandas and NumPy.

## Features
- Calculates total and average marks for each student.
- Assigns grades based on average marks.
- Determines pass or fail status.
- Calculates highest, lowest, and average Maths marks.
- Identifies top-performing students.
- Finds the highest and lowest overall performers.
- Calculates subject-wise average marks.
- Analyzes class attendance and identifies students with attendance below 75%.

## Technologies Used
- Python
- Pandas
- NumPy

## Project Files
- `main.py` — Contains the program logic and analytics.
- `students.csv` — Contains the sample student dataset.
- `README.md` — Project documentation.

## How to Run
1. Install Python on your computer.
2. Install the required libraries:

   ```bash
   pip install pandas numpy
   ```

3. Keep `main.py` and `students.csv` in the same folder.
4. Open a terminal in that folder.
5. Run:

   ```bash
   python main.py
   ```

## Dataset
The sample dataset contains 20 students with the following fields:
- Student ID
- Name
- Department
- Maths marks
- Python marks
- DBMS marks
- Attendance percentage

## Grading Criteria
- A: Average ≥ 90
- B: Average ≥ 80
- C: Average ≥ 70
- D: Average ≥ 60
- F: Average below 60

A student passes only if their marks are at least 35 in all three subjects.

## Learning Outcomes
This project demonstrates the use of Python functions, conditional statements, loops, NumPy calculations, Pandas DataFrames, data filtering, and basic data analysis.

## Author
Student Performance Analytics System — Academic Project
