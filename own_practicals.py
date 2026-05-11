# prices = {}

# while True:
#     print("\n--- Price List System ---")
#     print("1. Add New Item")
#     print("2. Check Item Price")
#     print("3. Exit")

#     choice = input("Enter your choice: ")

#     if choice == "1":
#         item = input("Enter item name: ")
#         price = float(input("Enter price: "))
#         prices[item.lower()] = price
#         print("Item added successfully")

#     elif choice == "2":
#         search = input("Enter item name: ").lower()

#         if search in prices:
#             print("Price of", search, "is", prices[search], "Rs")
#         else:
#             print("Item not found")

#     elif choice == "3":
#         print("Program ended")
#         break

#     else:
#         print("Invalid choice")

from datetime import date

file = open("price_data.txt", "a")

item = input("Enter item name: ")
price = input("Enter price: ")

today = date.today()

file.write(item + "," + price + "," + str(today) + "\n")

file.close()

print("Item stored successfully")




file = open("price_data.txt", "r")

search = input("Enter item name: ")

found = False

for line in file:
    item, price, saved_date = line.strip().split(",")

    if item.lower() == search.lower():
        print("Item:", item)
        print("Price:", price, "Rs")
        print("Date saved:", saved_date)
        found = True
        break

if not found:
    print("Item not found")

file.close()