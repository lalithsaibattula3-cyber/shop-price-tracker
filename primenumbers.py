numbers = {1,5,56,48,46,23,78,56,32,45,65,78,89}

print("Prime numbers in the set: ")

for n in numbers:
    if n > 1:
        prime = True
        for i in range(2, n):
            if n % i == 0:
                prime = False
                break
        if prime:
            print(n)
