# ------------------------------------------------------------------------------------------ #
# Title: Assignment05
# Desc: This assignment demonstrates using dictionaries, files, and exception handling
# Change Log: (Who, When, What)
#   RRoot,1/1/2030,Created Script
#   Avanti Gulhane,11/11/2026,Completed Assignment 05
# ------------------------------------------------------------------------------------------ #

import json

# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:
    1. Register a Student for a Course.
    2. Show current data.
    3. Save data to a file.
    4. Exit the program.
-----------------------------------------
'''
FILE_NAME: str = "Enrollments.json"

# Define the Data Variables
student_first_name: str = ''
student_last_name: str = ''
course_name: str = ''
student_data: dict = {}
students: list = []
file = None
menu_choice: str = ''

# Read existing student registrations from the JSON file
try:
    file = open(FILE_NAME, "r")
    students = json.load(file)
except (FileNotFoundError, json.JSONDecodeError, OSError) as error:
    print(f"Unable to load enrollment data: {error}")
    students = []
finally:
    if file is not None and not file.closed:
        file.close()

# Present and process the data
while True:
    print(MENU)
    menu_choice = input("What would you like to do: ")

    if menu_choice == "1":
        try:
            student_first_name = input("Enter the student's first name: ").strip()
            if not student_first_name:
                raise ValueError("First name cannot be empty.")
        except (ValueError, EOFError) as error:
            print(f"Unable to enter first name: {error}")
            continue

        try:
            student_last_name = input("Enter the student's last name: ").strip()
            if not student_last_name:
                raise ValueError("Last name cannot be empty.")
        except (ValueError, EOFError) as error:
            print(f"Unable to enter last name: {error}")
            continue

        course_name = input("Please enter the name of the course: ").strip()
        student_data = {"FirstName": student_first_name,
                        "LastName": student_last_name,
                        "CourseName": course_name}
        students.append(student_data)
        print(f"You have registered {student_first_name} {student_last_name} for {course_name}.")
        continue

    elif menu_choice == "2":
        print("-" * 50)
        for student in students:
            print(f"Student {student['FirstName']} {student['LastName']} is enrolled in {student['CourseName']}")
        print("-" * 50)
        continue

    elif menu_choice == "3":
        file = None
        try:
            file = open(FILE_NAME, "w")
            json.dump(students, file, indent=4)
        except (OSError, TypeError) as error:
            print(f"Unable to save enrollment data: {error}")
            continue
        finally:
            if file is not None and not file.closed:
                file.close()

        print("The following data was saved to file!")
        for student in students:
            print(f"Student {student['FirstName']} {student['LastName']} is enrolled in {student['CourseName']}")
        continue

    elif menu_choice == "4":
        break
    else:
        print("Please only choose option 1, 2, 3, or 4")

print("Program Ended")
