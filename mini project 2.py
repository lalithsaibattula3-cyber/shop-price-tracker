#calculator menu 

print("calculator menu: ")              #choice selection starts here 
print("1.addition")
print("2.subtratcion")
print("3.multiplication")
print("4.division")

while(True):
    choice=int(input("enter any choice: "))

    a = int(input("print any number:"))                      #input 1
    b = int(input("print any number:"))                      #input 2

    if choice == 1:
        total =a+b                                           #addition
        print(total)

    elif choice == 2:
        total = a-b                                          #subtraction
        print(total)

    elif choice == 3:
        total = a*b                                           #multipication
        print(total)

    else:
        total = a/b                                           #division
        print(total)
