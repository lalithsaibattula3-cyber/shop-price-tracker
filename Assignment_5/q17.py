"""
Q17. Expense Tracker
Add, delete, view expenses, display summary, and use a top-down approach.
"""

expenses = []


def add_expense(category, amount, note=""):
    item = {"category": category, "amount": amount, "note": note}
    expenses.append(item)
    print(f"Added expense: {category} - ₹{amount}")


def delete_expense(index):
    if 0 <= index < len(expenses):
        removed = expenses.pop(index)
        print(f"Deleted expense: {removed['category']} - ₹{removed['amount']}")
        return True
    print("Invalid expense index.")
    return False


def view_expenses():
    if not expenses:
        print("No expenses recorded.")
        return
    print("Expense list:")
    for idx, item in enumerate(expenses, start=1):
        print(f"{idx}. {item['category']} - ₹{item['amount']} ({item['note']})")


def summary():
    total = sum(item["amount"] for item in expenses)
    categories = {}
    for item in expenses:
        categories[item["category"]] = categories.get(item["category"], 0) + item["amount"]
    print(f"Total expenses: ₹{total}")
    print("By category:")
    for cat, amt in categories.items():
        print(f"- {cat}: ₹{amt}")


if __name__ == "__main__":
    add_expense("Food", 250, "Lunch")
    add_expense("Travel", 120, "Bus fare")
    add_expense("Books", 500, "Reference book")
    view_expenses()
    summary()
    delete_expense(1)
    print()
    view_expenses()
    summary()
