"""
Q15. Quiz Application
Ask multiple questions, use loops and conditional statements, and avoid continue statements.
"""

questions = [
    {
        "question": "What is the capital of India?",
        "options": ["Delhi", "Mumbai", "Kolkata", "Chennai"],
        "answer": "Delhi",
    },
    {
        "question": "What is 5 + 7?",
        "options": ["10", "11", "12", "13"],
        "answer": "12",
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["Earth", "Mars", "Jupiter", "Venus"],
        "answer": "Mars",
    },
]


def run_quiz():
    score = 0
    for item in questions:
        print(item["question"])
        for index, option in enumerate(item["options"], start=1):
            print(f"  {index}. {option}")
        choice = input("Enter option number: ").strip()
        if not choice.isdigit():
            print("Invalid input. Please enter a number.")
        else:
            selected_index = int(choice) - 1
            if 0 <= selected_index < len(item["options"]):
                selected_option = item["options"][selected_index]
                if selected_option == item["answer"]:
                    score += 1
                    print("Correct!")
                else:
                    print("Incorrect.")
            else:
                print("Invalid option selected.")
        print()
    print(f"Quiz finished. Your score: {score}/{len(questions)}")


if __name__ == "__main__":
    run_quiz()
