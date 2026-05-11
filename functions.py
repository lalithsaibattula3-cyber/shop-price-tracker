# import math 
# def greet():
#     print("hello")
# greet()

# def greet(name):
#     print("hello",name)
# greet("lalith")

# def add(a,b):
#     return a+b
# result = add(5,3)
# print (result)

# can = add(87,98)
# print(can)

# def greet(name = "student"):
#     print("hello",name)
# greet()
# greet("lalith")

# def add(a,b):
#     sum1=sum2=0
#     return sum(a)+sum(b)
# a =[1,2,3,5,7]
# b =[8,7,5,6,4]
# total = add(a,b)
# print(total)
# a=[3,4]
# b = [8,8]
# total = add(a,b)
# print(total)

# #prinme number function
# def prime(a):
#     if a == 1 or a == 0:
#         return False
#     b=int(math.sqrt(a))
#     for i in range(2,b+1):
#         if a % i == 0:
#             return False
#     return True
# while(True):
#     a = int(input("enter an value:"))
#     for i in range(0,a+1):
#         p = prime(i)
#         print(f"{i}={p}")
#     print("="*20)

# def mult(a,b):
#     return a*b
# while(True):
#     a = int(input("enter the first number:"))
#     if a == -1000:
#         break
#     b = int(input("enter the secondnumber:"))
#     print(mult(a,b))


# import qr_generator
# img = qr_generator.make("https://amzn.in/d/007HZ1qU")
# img.show()

def fun(a,b=10):
    return a+b
print(fun(2))