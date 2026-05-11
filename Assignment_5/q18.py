"""
Q18. Code Improvement
Identify errors in AI-generated code and improve readability and documentation.
"""

# Original AI-generated example (buggy and unclear):
# def calc(x,y):
#   if x > y:
#   return x+y
# c=calc(2,3)
# print("Result" c)


def add_numbers(x, y):
    """Return the sum of two numbers."""
    return x + y


def display_result(x, y):
    """Compute and print a clean result message."""
    total = add_numbers(x, y)
    print(f"Result: {total}")


if __name__ == "__main__":
    display_result(2, 3)
    # Explanation: The improved version uses proper indentation, function names, and string formatting.
