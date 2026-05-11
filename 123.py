import tkinter as tk
from tkinter import messagebox
import json
import os

FILE = "prices.json"

# ---------- Load & Save ----------

def load_data():
    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            return json.load(f)
    return {}

def save_data():
    with open(FILE, "w") as f:
        json.dump(products, f, indent=4)

products = load_data()

# ---------- Functions ----------

def add_item():
    name = entry_name.get().strip()
    price = entry_price.get().strip()

    if not name or not price:
        messagebox.showerror("Error", "Enter both name and price")
        return

    try:
        price = float(price)
    except:
        messagebox.showerror("Error", "Price must be a number")
        return

    products[name] = price
    save_data()

    messagebox.showinfo("Success", f"{name} added!")
    entry_name.delete(0, tk.END)
    entry_price.delete(0, tk.END)
    show_list()


def delete_item():
    selected = listbox.curselection()
    if not selected:
        messagebox.showerror("Error", "Select item to delete")
        return

    item = listbox.get(selected[0]).split(" - ")[0]

    if item in products:
        del products[item]
        save_data()
        show_list()
        messagebox.showinfo("Deleted", f"{item} removed")


def show_list():
    listbox.delete(0, tk.END)
    for item, price in products.items():
        listbox.insert(tk.END, f"{item} - ₹{price}")


def clear_all():
    global products
    products = {}
    save_data()
    show_list()
    messagebox.showinfo("Cleared", "All items removed")


# ---------- UI ----------

root = tk.Tk()
root.title("Price List Maker")
root.geometry("400x500")
root.configure(bg="#2c3e50")

# Title
tk.Label(root, text="Price List Maker", font=("Arial", 18, "bold"),
         bg="#2c3e50", fg="white").pack(pady=10)

# Input Fields
tk.Label(root, text="Item Name", bg="#2c3e50", fg="white").pack()
entry_name = tk.Entry(root)
entry_name.pack(pady=5)

tk.Label(root, text="Price", bg="#2c3e50", fg="white").pack()
entry_price = tk.Entry(root)
entry_price.pack(pady=5)

# Buttons
tk.Button(root, text="Add Item", command=add_item,
          bg="#27ae60", fg="white", width=20).pack(pady=10)

tk.Button(root, text="Delete Selected", command=delete_item,
          bg="#e74c3c", fg="white", width=20).pack(pady=5)

tk.Button(root, text="Clear All", command=clear_all,
          bg="#f39c12", fg="white", width=20).pack(pady=5)

# Listbox
listbox = tk.Listbox(root, width=40, height=15)
listbox.pack(pady=10)

# Load existing data
show_list()

root.mainloop()