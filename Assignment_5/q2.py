"""
Q2. Online Shopping Cart
Store items using a list of dictionaries, calculate total cost, remove duplicate items, and apply discount for high totals.
"""

cart_items = [
    {"name": "T-shirt", "price": 450, "quantity": 2},
    {"name": "Sneakers", "price": 3200, "quantity": 1},
    {"name": "T-shirt", "price": 450, "quantity": 1},
    {"name": "Backpack", "price": 1200, "quantity": 1},
]


def consolidate_cart(items):
    consolidated = {}
    for item in items:
        key = item["name"].strip().lower()
        if key in consolidated:
            consolidated[key]["quantity"] += item["quantity"]
        else:
            consolidated[key] = {
                "name": item["name"],
                "price": item["price"],
                "quantity": item["quantity"],
            }
    return list(consolidated.values())


def calculate_total(items):
    return sum(item["price"] * item["quantity"] for item in items)


def apply_discount(total_amount):
    discount_rate = 0.10 if total_amount > 5000 else 0.0
    discount_amount = total_amount * discount_rate
    return round(total_amount - discount_amount, 2), discount_rate


def display_cart(items):
    print("Shopping Cart")
    for item in items:
        print(f"- {item['name']}: ₹{item['price']} x {item['quantity']}")


if __name__ == "__main__":
    unique_cart = consolidate_cart(cart_items)
    display_cart(unique_cart)
    total = calculate_total(unique_cart)
    final_total, discount_rate = apply_discount(total)
    print(f"Total before discount: ₹{total}")
    if discount_rate > 0:
        print(f"Discount applied: {int(discount_rate*100)}%")
    print(f"Final total: ₹{final_total}")
