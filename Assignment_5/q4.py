"""
Q4. Password Strength Checker
Validate password with string functions and report strength level.
"""

SPECIAL_CHARACTERS = set("!@#$%^&*()-_=+[]{}|;:'\",.<>?/`~")


def password_strength(password):
    if not password:
        return "Very Weak"

    has_upper = any(ch.isupper() for ch in password)
    has_lower = any(ch.islower() for ch in password)
    has_digit = any(ch.isdigit() for ch in password)
    has_special = any(ch in SPECIAL_CHARACTERS for ch in password)
    length = len(password)

    score = sum([has_upper, has_lower, has_digit, has_special])
    if length >= 12 and score == 4:
        return "Very Strong"
    if length >= 8 and score >= 3:
        return "Strong"
    if length >= 6 and score >= 2:
        return "Moderate"
    return "Weak"


def display_password_feedback(password):
    print(f"Password: {password}")
    print("Uppercase:", any(ch.isupper() for ch in password))
    print("Lowercase:", any(ch.islower() for ch in password))
    print("Digit:", any(ch.isdigit() for ch in password))
    print("Special character:", any(ch in SPECIAL_CHARACTERS for ch in password))
    print("Strength level:", password_strength(password))


if __name__ == "__main__":
    display_password_feedback("Summer2026$")
    print()
    display_password_feedback("weakpass")
