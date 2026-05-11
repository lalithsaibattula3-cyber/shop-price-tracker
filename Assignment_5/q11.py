"""
Q11. Custom Exception
Create a user-defined exception and validate age must be >= 18.
"""

class AgeValidationError(Exception):
    def __init__(self, age):
        super().__init__(f"Age {age} is invalid. Must be 18 or older.")
        self.age = age


def validate_age(age):
    if age < 18:
        raise AgeValidationError(age)
    return True


if __name__ == "__main__":
    test_ages = [16, 18, 21]
    for age in test_ages:
        try:
            validate_age(age)
            print(f"Age {age} is valid.")
        except AgeValidationError as e:
            print("Validation error:", e)
