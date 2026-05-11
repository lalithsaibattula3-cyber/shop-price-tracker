num=int(input("enter a number"))
bin = ""
decimal = num
while decimal > 0:
    rem = decimal % 2
    bin = str(rem)+bin
    decimal =decimal // 2
print(bin)

           