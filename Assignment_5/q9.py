"""
Q9. Student Record Manager
Add, search, and update student records using file storage and proper file operations.
"""

import json
import os

DATA_FILE = "student_records.json"


def load_records():
    if not os.path.exists(DATA_FILE):
        return {}
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_records(records):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(records, f, indent=2)


def add_student(student_id, name, marks):
    records = load_records()
    records[str(student_id)] = {"name": name, "marks": marks}
    save_records(records)
    print(f"Added student {name} (ID: {student_id})")


def search_student(student_id):
    records = load_records()
    return records.get(str(student_id))


def update_student(student_id, name=None, marks=None):
    records = load_records()
    record = records.get(str(student_id))
    if not record:
        return False
    if name:
        record["name"] = name
    if marks:
        record["marks"] = marks
    records[str(student_id)] = record
    save_records(records)
    return True


if __name__ == "__main__":
    add_student(101, "Riya", {"Math": 85, "Science": 78})
    add_student(102, "Arjun", {"Math": 92, "English": 88})
    print("Search ID 102:", search_student(102))
    updated = update_student(101, marks={"Math": 88, "Science": 80})
    print("Update successful:" , updated)
    print("Updated record:", search_student(101))
