"""
Patrice Moracchini
CSD-325 Module 8.2 JSON Practice

"""

from __future__ import annotations

import json
from pathlib import Path


def print_students(students: list[dict]) -> None:
    # Loop through the student list and print each student's info.
        # Expected keys: F_Name, L_Name, Student_ID, Email
        last_name = s.get("L_Name", "")
        first_name = s.get("F_Name", "")
        student_id = s.get("Student_ID", "")
        email = s.get("Email", "")
        print(f"{last_name}, {first_name} : ID = {student_id} , Email = {email}")


def main() -> None:
    json_path = Path(__file__).with_name("student.json")

    # 1) Load JSON file into a Python list
    try:
        with json_path.open("r", encoding="utf-8") as f:
            students = json.load(f)

        if not isinstance(students, list):
            raise ValueError("student.json must contain a JSON array (list) of students.")

    except FileNotFoundError: 
        print(f"ERROR: Could not find {json_path.name} in {json_path.parent}")
        return
    except json.JSONDecodeError as e:
        print(f"ERROR: {json_path.name} is not valid JSON: {e}")
        return
    except ValueError as e:
        print(f"ERROR: {e}")
        return

    # 2) Print original list
    print("\nOriginal Student list:\n")
    print_students(students)

    # 3) Append your new student info
    new_student = {
        "F_Name": "Patrice",              
        "L_Name": "Moracchini",           
        "Student_ID": 123456,              
        "Email": "patrice.moracchini@me.com"  
    }
    students.append(new_student)

    # 4) Print updated list
    print("\nUpdated Student list:\n")
    print_students(students)

    # 5) Dump updated list back to JSON file
    try:
        with json_path.open("w", encoding="utf-8", newline="\n") as f:
            json.dump(students, f, indent=4)
        print(f"\nThe .json file was updated: {json_path.name}\n")
    except OSError as e:
        print(f"ERROR: Could not write to {json_path.name}: {e}")

# Run the main function
if __name__ == "__main__":
    main()