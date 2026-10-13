
import pandas as pd

students = pd.read_csv("students.csv")

students["Total"] = (
    students["Maths"] +
    students["Python"] +
    students["DBMS"]
)

students["Average"] = students["Total"] / 3

print(students[["Name", "Total", "Average"]])

def calculate_grade(average):
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"


students["Grade"] = students["Average"].apply(calculate_grade)

print(students[["Name", "Average", "Grade"]])

def check_result(row):
    if row["Maths"] >= 35 and row["Python"] >= 35 and row["DBMS"] >= 35:
        return "Pass"
    else:
        return "Fail"


students["Result"] = students.apply(check_result, axis=1)

print(students[["Name", "Maths", "Python", "DBMS", "Result"]])

import numpy as np

maths_marks = students["Maths"].to_numpy()

highest_maths = np.max(maths_marks)
lowest_maths = np.min(maths_marks)
average_maths = np.mean(maths_marks)

highest_average = np.max(students["Average"])

print("\n--- Class Performance Statistics ---")
print("Highest Maths mark:", highest_maths)
print("Lowest Maths mark:", lowest_maths)
print("Class Maths average:", round(average_maths, 2))
print("Highest student average:", round(highest_average, 2))

top_students = students[students["Average"] >= 80]

print("\n--- Top Performing Students ---")
print(top_students[["Student_ID", "Name", "Average", "Grade"]])

print("\n--- Subject-wise Class Averages ---")

print("Maths average:", round(np.mean(students["Maths"]), 2))
print("Python average:", round(np.mean(students["Python"]), 2))
print("DBMS average:", round(np.mean(students["DBMS"]), 2))

subject_averages = {
    "Maths": np.mean(students["Maths"]),
    "Python": np.mean(students["Python"]),
    "DBMS": np.mean(students["DBMS"])
}

best_subject = max(subject_averages, key=subject_averages.get)

print("\n--- Best Performing Subject ---")
print("Subject averages:", subject_averages)
print("Best performing subject:", best_subject)


attendance = students["Attendance"].to_numpy()

average_attendance = np.mean(attendance)

print("\n--- Attendance Analysis ---")
print("Class average attendance:", round(average_attendance, 2), "%")

print("\nStudents with attendance below 75%:")

low_attendance = students[students["Attendance"] < 75]

if low_attendance.empty:
    print("No students have attendance below 75%.")
else:
    print(low_attendance[["Student_ID", "Name", "Attendance"]].to_string(index=False))


highest_student = students.loc[students["Average"].idxmax()]
lowest_student = students.loc[students["Average"].idxmin()]

print("\n--- Student Performance Highlights ---")

print("Highest Performing Student:")
print("Name:", highest_student["Name"])
print("Average:", round(highest_student["Average"], 2))

print("\nLowest Performing Student:")
print("Name:", lowest_student["Name"])
print("Average:", round(lowest_student["Average"], 2))


subjects = ["Maths", "Python", "DBMS"]

print("\n--- Subject-wise Performance ---")

for subject in subjects:
    average = np.mean(students[subject])
    print(subject, "Average:", round(average, 2))
