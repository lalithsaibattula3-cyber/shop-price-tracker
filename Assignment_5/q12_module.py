"""
Utility module for Q12.
Provides factorial and palindrome check functions.
"""

def factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    result = 1
    for value in range(2, n + 1):
        result *= value
    return result


def is_palindrome(text):
    normalized = ''.join(ch.lower() for ch in text if ch.isalnum())
    return normalized == normalized[::-1]
