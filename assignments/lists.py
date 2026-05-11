#Find the length of the list 
a = ["hello", "world", "welcome", "to", "vs","code"]
count = 0
for item in a :
    count += 1 
print (count)

#the element is exists in the list 
search = input("enter the word: ")
for search in a:
 print(search in a)

#sum and avg of the list
a = [-50,-10,-20,30,40,50,60,70,80,99]

total = 0
count = 0
for num in a:
    total += num
    count += 1
avg = total / count
print(total)
print(avg)

#multiply all elements in a list
multiply = 1
for num in a:
    multiply = multiply * num
print(multiply)

#even numbers in a list
for num in a:
    if(num % 2 == 0):
        print(num)

#odd numbers in a list 
for num in a:
    if (num % 2 != 0):
        print(num)

#positive numbers in a list 

positive = 0
for num in a:
    if(num > 0):
        positive += num #   ||print(num)---->>prints the positive numbers ittertively!!
print(positive)   #---->>gives sum of the postive numbers!!


#negative numbers in a list

for c in a:
    if c < 0:
        print(c,end=" ")
