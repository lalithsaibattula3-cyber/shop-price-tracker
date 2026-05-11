"""
Q6. EMI Calculator
Create a function with arguments (P, R, T), return EMI, and use default arguments.
"""

import math


def calculate_emi(P=100000, R=7.5, T=12):
    monthly_rate = R / (12 * 100)
    n = T
    if monthly_rate == 0:
        return P / n
    emi = P * monthly_rate * math.pow(1 + monthly_rate, n) / (math.pow(1 + monthly_rate, n) - 1)
    return round(emi, 2)


if __name__ == "__main__":
    print("EMI Calculator")
    print("EMI for ₹100000 at 7.5% for 12 months:", calculate_emi())
    print("EMI for ₹500000 at 9.0% for 24 months:", calculate_emi(500000, 9.0, 24))
