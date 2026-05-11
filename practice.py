# # a = int(input("enter a number: "))
# # count = 0
# # while a > 0:
# #     count += a % 10
# #     a //= 10
# #     print(count)
# # text = "Hello World"
# # print(text.lower()[6:])

# # n = 19
# # square = 0
# # while n> 0:
# #     digit = n % 10
# #     square = square + digit*digit
# #     n = n//10
# # print(n)

# km = float(input("Enter the distance travelled: "))

# base = 50
# total = base + 12 * km

# if km > 15:
#     total += total * 0.2   # add 20% surcharge

# print("Total fare =", total)

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