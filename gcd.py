# def gcd_(a,b):
#     gcd = 1
#     for i in range (1,min(a,b)+1):
#         if a%i == 0 and b%i == 0:
#             gcd = i
#     return gcd

# #hastag question
# morning = set(input("enter the morning hastags:").split())
# evening = set(input("enter the evening hastags:").split())

# new = evening - morning

# dropped = morning - evening 

# stable = morning & evening 

# print("new:",new)
# print("dropped:",dropped)
# print("stable:",stable)

#SUPER MARKET 
item = input("enter the items:")
list = []
try:
    data = list.split()
    if not data:
        print("cart is empty")
    else:
        total = sum(float(x) for x in data)
        print(total)
except:
    print("invalid price dected")


f = open("lalith.txt","r")
for line in f:
    words = line.split()

    for w in words:
        print(w[::-1],end="")
    print()
f.close()

#palindrome
def palindrome(n):
    rev = 0
    m = n
    while n>0:
        digit = n%10
        rev = rev * 10 + digit
        n = n // 10
    return rev == n 
 
n = int(input("enter a number: "))
if (palindrome(n)):
    print("palindrome")
else:
    print("not a palindrome")

no_of_students = int(input("enter number of students:"))
students_list = []
for i in range(no_of_students):
    name = input("enter the name:")
    marks = input("enter the marks:")
    students_list[name] = marks

highest = max(students_list.values())
lowest = min(students_list.values())
average = sum(students_list.values())/ no_of_students
top_score = max(students_list,key = students_list.get)

print({
     "highest :",highest,
      "lowest :",lowest,
      "average :",average,
      "top score :",top_score
})
