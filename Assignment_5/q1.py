"""
Q1. Student Performance Tracker
Store student marks in different subjects, calculate average marks, display topper, and handle missing data.
"""

SUBJECTS = ["Math", "Science", "English", "History"]

students = {
    "Ravi": {"Math": 82, "Science": 74, "English": 91},
    "Sneha": {"Math": 90, "Science": 88, "English": 79, "History": 85},
    "Aditi": {"Math": 76, "History": 80},
}


def get_average(marks):
    if not marks:
        return 0.0
    return sum(marks.values()) / len(marks)


def build_student_report(student_marks):
    report = {}
    for name, marks in student_marks.items():
        missing = [sub for sub in SUBJECTS if sub not in marks]
        if missing:
            print(f"Warning: {name} is missing marks for {', '.join(missing)}.")
        average = get_average(marks)
        report[name] = {
            "marks": marks,
            "average": round(average, 2),
            "missing_subjects": missing,
        }
    return report


def get_topper(report):
    if not report:
        return None
    topper = max(report.items(), key=lambda item: item[1]["average"])
    return topper


def display_report(report):
    for name, data in report.items():
        print(f"\nStudent: {name}")
        print("Marks:")
        for subject in SUBJECTS:
            print(f"  {subject}: {data['marks'].get(subject, 'N/A')}")
        print(f"Average: {data['average']}")
        if data["missing_subjects"]:
            print("Missing subjects:", ", ".join(data["missing_subjects"]))


if __name__ == "__main__":
    print("Student Performance Tracker")
    report = build_student_report(students)
    display_report(report)
    topper = get_topper(report)
    if topper:
        name, data = topper
        print(f"\nTopper: {name} with average {data['average']}")
    else:
        print("No student records available.")
