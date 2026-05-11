for i in range(1,11):
    print(i)


for i in range(1,21):
    if i % 2 ==0 :
        print(i)

for i in range (21,1,-1):
    if i % 2 != 0:
        print(i)

for i in range(10,0,-1):
    print(i)

n=int(input("enter a number: "))
for i in range(1,11):
    print(n,"x",i,"=",n*i)

n=int(input("enter a number"))
for i in range(11,0,-1):
    print(n,"x" ,i,"=",n*i)

n=int(input("enter a number: "))
sum =0
for i in range(1,n+1):
    sum = sum+i 
    print(sum)

n=int(input("enter a number"))
fact=1
for i in range(1,n+1):
    fact =fact*i
    print(fact)

n = int(input("enter a number"))
count=0
for i in str(n):
    count=count+1
    print(count)