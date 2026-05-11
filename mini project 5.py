import random

letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "!@#$%^&*()_+"

length = int(input("Enter password length: "))
use_numbers = input("Include numbers? (y/n): ")
use_symbols = input("Include symbols? (y/n): ")

all_chars = letters

if use_numbers == 'y':
    all_chars += numbers

if use_symbols == 'y':
    all_chars += symbols

password = ""

for i in range(length):
    ch = random.choice(all_chars)
    password += ch

print("Your Password is:", password)


