
#if statement
a=15
if a>0 :
    print('a is a positive number')

b=8
if b % 2 ==0:
    print('b is even')

c=200
if c>=40:
    print('pass')

d=16
if d>=18:
    print('you are eligible for voting')

#if else statement
e=18
if e %2 ==0:
    even = f"{e} is even"
    print(even)

else:
    odd = f"{e} is odd"
    print(odd)


f=8
g=7

if f>g:
    greater = f"{f} is greater than {g}"
    print(greater)
else :
    smaller = f"{f} is smaller than {g}"
    print(smaller)


h=a

if h in  {'a','e','i','o','u'}:
    vowels = f"{h} is an vowel"
    print (vowels)

else :
    consonents = f"{h} is an consonent"
    print (consonents)

i = int(input("enter a number"))

if i % 5 == 0 and i % 11 == 0 :
    print ('both are divided')
else :
    print('invalid')

temperature = int(input("enter the temperature :"))

if temperature >30 :
    print("hot")
else:
    print ("normal")

#match

z =int(input('enter a number (1-7) : '))
match z:
    case 1:
        print('monday')
    case 2:
        print ('tuesday')
    case 3:
        print ('wednesday')
    case 4:
        print('thursday')
    case 5:
        print ('friday')
    case 6:
        print ("saturday")
    case 7: 
        print('sunday')
    case 8:
        print('invalid day')
    
print("hello","world")


for x in "banana":
    print(x)

#conditional expressions 
age = 15
status ='adult' if age >= 18 else "minor"
print(status)
