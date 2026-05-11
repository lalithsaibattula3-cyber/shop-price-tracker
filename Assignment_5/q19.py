"""
Q19. Prompt Writing
Write a prompt for a student grading system and compare example outputs.
"""


def build_prompt():
    return (
        "Write a Python program that accepts student names and marks in at least three subjects, "
        "calculates the average, assigns grades based on the average, and prints a report. "
        "Use functions and handle missing marks gracefully."
    )


def example_output():
    return (
        "Student: Akshay\n"
        "Math: 88, Science: 92, English: 79\n"
        "Average: 86.33\n"
        "Grade: A\n"
    )


if __name__ == "__main__":
    print("Prompt for grading system:")
    print(build_prompt())
    print("\nSample expected output:")
    print(example_output())
