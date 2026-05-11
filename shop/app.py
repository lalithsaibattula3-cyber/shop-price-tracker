from datetime import datetime
from db import connect, create_tables

create_tables()


# ➕ Add bill
def add_bill(item_name, total_price, quantity, unit, date):
    conn = connect()
    cursor = conn.cursor()

    # Calculate price per unit
    price_per_unit = total_price / quantity

    # Check if item exists
    cursor.execute("SELECT id FROM items WHERE name = ?", (item_name,))
    result = cursor.fetchone()

    if result:
        item_id = result[0]
    else:
        cursor.execute("INSERT INTO items (name) VALUES (?)", (item_name,))
        item_id = cursor.lastrowid

    # Insert bill
    cursor.execute("""
        INSERT INTO bills (item_id, total_price, quantity, unit, price_per_unit, date)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (item_id, total_price, quantity, unit, price_per_unit, date))

    conn.commit()
    conn.close()


# 🔍 Get latest price
def get_latest_price(item_name):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT b.total_price, b.date, b.price_per_unit, b.unit
        FROM bills b
        JOIN items i ON b.item_id = i.id
        WHERE LOWER(i.name) = LOWER(?)
        ORDER BY b.date DESC
        LIMIT 1
    """, (item_name,))

    result = cursor.fetchone()
    conn.close()
    return result


# 🖥️ Menu
def menu():
    while True:
        print("\n--- Shop Price Tracker ---")
        print("1. Add Bill")
        print("2. Search Item")
        print("3. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            name = input("Item name: ")
            total_price = float(input("Total Price: "))
            quantity = float(input("Quantity (number only): "))
            unit = input("Unit (kg/litre/pkt/box): ")

            date = datetime.now().strftime("%Y-%m-%d %I:%M %p")

            add_bill(name, total_price, quantity, unit, date)
            print("Added successfully ✅")

        elif choice == "2":
            name = input("Enter item name: ")
            result = get_latest_price(name)

            if result:
                print(f"\nTotal price: ₹{result[0]} on {result[1]}")
                print(f"Price per unit: ₹{result[2]} per {result[3]}")
            else:
                print("Item not found ❌")

        elif choice == "3":
            print("Exiting...")
            break

        else:
            print("Invalid choice ❌")


# ▶️ Run app
menu()