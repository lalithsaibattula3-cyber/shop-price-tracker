name = "lalith - 75 , prashan - 85 , kc - 79 , surya - 79"

record = name.split(" , ")

students = []
for item in record:
    name, marks = item.split(" - ")
    students.append([name, int(marks)])

names = []
marks_list = []

for student in students:
    names.append(student[0])
    marks_list.append(student[1])

print("Names:", names)
print("Marks:", marks_list)

avg = sum(marks_list) / len(marks_list)
print("Average:", avg)

print("Below average students:")
for student in students:
    if student[1] < avg:
        print(student[0], student[1])

students.sort(key=lam

bda x: x[1], reverse=True)
print("Students sorted by marks:")
for student in students:
    print(student[0], student[1])