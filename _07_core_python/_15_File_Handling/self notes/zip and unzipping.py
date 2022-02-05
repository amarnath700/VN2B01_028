students = ["Amar", "Viveka", "Lavi", "Adi", "Lavanya"]
age = [30, 28, 24, 32, 26]
course = ["python", "java", "testing", "embedded", "c"]

for s, a, c in zip(students, age, course):
    print("student name and age:", (s, a, c))

# zipping
print("***** Zipping  ******")
mapped = zip(students, age, course)
x = set(mapped)
print(mapped)
print(x)

# unzipping
print("*****  Unzipping  *****")
studentsz, agez, coursez = zip(*x)

print("student names:", list(studentsz))
print("Student course:", set(coursez))
print("student age:", tuple(agez))
