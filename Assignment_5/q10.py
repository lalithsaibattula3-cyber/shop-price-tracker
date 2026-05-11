"""
Q10. ATM Simulation
Handle invalid input, raise exception for insufficient balance, and use try-except-finally.
"""

class InsufficientBalanceError(Exception):
    pass


class ATM:
    def __init__(self, balance=0.0):
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self.balance:
            raise InsufficientBalanceError("Insufficient balance for withdrawal.")
        self.balance -= amount
        return self.balance


if __name__ == "__main__":
    atm = ATM(balance=3000)
    try:
        print("Initial balance: ₹", atm.balance)
        atm.deposit(1500)
        print("After deposit: ₹", atm.balance)
        atm.withdraw(5000)
    except InsufficientBalanceError as e:
        print("Transaction failed:", e)
    except ValueError as e:
        print("Invalid input:", e)
    finally:
        print("Final balance: ₹", atm.balance)
