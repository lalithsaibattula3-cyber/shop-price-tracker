"""
Q13. Math Toolkit
Use math and random modules to perform calculations and generate random values.
"""

import math
import random


def demonstrate_math_toolkit():
    values = [random.randint(1, 20) for _ in range(5)]
    print("Random values:", values)
    print("Square roots:", [round(math.sqrt(v), 2) for v in values])
    print("Sine of first value:", round(math.sin(math.radians(values[0])), 4))
    print("Logarithm of first value:", round(math.log(values[0]), 4))
    print("Random float between 0 and 1:", random.random())
    print("Random choice from values:", random.choice(values))


if __name__ == "__main__":
    demonstrate_math_toolkit()
