# fiction_club = input("Enter fiction club members: ")
# science_club = input("Enter science club members: ")

# fiction_club = {name.strip() for name in fiction_club.split(",") if name.strip()}
# science_club = {name.strip() for name in science_club.split(",") if name.strip()}

# both_clubs = fiction_club & science_club
# only_fiction = fiction_club - science_club

# print("Members in both clubs:", both_clubs)
# print("Members only in the fiction club:", only_fiction)

bank1 = int(input("enter the transaction of bank 1:"))
bank2 = int(input("enter the transaction of bank 2:"))

common = bank1 & bank2

print(common)