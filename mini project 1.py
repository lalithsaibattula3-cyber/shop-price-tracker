#electricity bill


units = int(input("enter the units value :  "))       #enter the units

if units <= 100:
    total = units*1.50                                #unit price  is 1.50 
    print(total)

elif  101 <= units <= 200:
      total = units*2.50                              #unit price is 2.50
      print(total)

elif 201 <= units <= 300 :
      total = units*4.00                              #unit price is 4.00
      print(total)

else:
     total = units*6.00                               #unit price is 6.00
     print(total)