age = int(input("enter the age: "))

if age < 5:
    price = 0

elif age <= 12:
    price =  50

elif age <= 60:
    price = 100

else:
    price = 70

print(price)