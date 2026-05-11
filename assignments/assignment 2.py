#print 1 to 5 
for i in range (1,6):
    print(i)

#print 3*3 star pattern
for i in range(3):
    for j in range(3):
        print("*",end='')
    print()

#print a star pattern right angled triangle
n = 4
for i in range (1,n+1):
    for j in range(i):
        print("*",end="")
    print()

#print an inverted right angle triangle
n = 4
for i in range(n,0,-1):
    for j in range(i):
        print("*",end="")
    print()

#print multiplication tables 
n = 7
for i in range(1,13):
    print(n,"x",i,"=",n*i)

#print prime numbers from 1 to 50
for n in range(2, 51):
    is_prime = True
    for i in range(2, n):
        if n % i == 0:
            is_prime = False
            break
    if is_prime:
        print(n)

#print perfect numbers from 1 to 100    
for n in range(1,101):
    sum = 0
    for i in range(1,n):
        if n % i == 0:
            sum += i
    if sum == n :
        print(n)

#matrix display
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
for row in matrix:
    for value in row:
        print(value,end="")
    print()

#matrix addition
A = [
    [1, 2],
    [4, 5],
]

B = [
    [4, 6],
    [7, 8],
]
result = [[0,0],[0,0]]
for i in range(2):
    for j in range (2):
        result[i][j] = A[i][j] +B[i][j]

for row in result:
    print(row)

#print transpose of a matrix
matrix = [
    [1,2,3],
    [4,5,6],
]
transpose = [[0,0],[0,0],[0,0]]
for i in range(2):
    for j in range(3):
        transpose[j][i] = matrix[i][j]
for row  in transpose:
    print(row)

#string pattern
s = "lalith"
for i in range(1,len(s)+1):
    print(s[:i])

#chess board
n = 4
for i in range(n):
    for j in range(n):
        if (i + j) % 2 == 0:
            print("#", end=" ")
        else:
            print("*", end=" ")
    print()
