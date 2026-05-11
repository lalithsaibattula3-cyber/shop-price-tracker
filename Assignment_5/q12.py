"""
Q12. Utility Module
Import factorial and palindrome check from a separate module.
"""

from q12_module import factorial, is_palindrome


if __name__ == "__main__":
    print("Factorial of 5:", factorial(5))
    print("Is 'Racecar' a palindrome?", is_palindrome("Racecar"))
    print("Is 'Hello' a palindrome?", is_palindrome("Hello"))
