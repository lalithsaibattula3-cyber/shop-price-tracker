n=int(input("enter number of terms"))
a,b=0,1
if n<=0:
    print("enter a positive number")
elif n==1:
    print(a)
else:
    print(a,b,end="  ")
    for i in range(3,n+1):
        c=a+b
        print(c,end="  ")
        a=b
        b=c

for i in range(1,6):
    for j in range(1):
        print(i)

n=3
for i in range(n):
    for j in range(n):
        print('*',end="")
    print()



for i in range(1,4):
    for j in range(i):
        print('*',end="")
    print()
