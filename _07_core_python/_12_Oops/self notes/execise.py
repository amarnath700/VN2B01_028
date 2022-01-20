class Person:
    name = "Amar"
    age = 30

    def run(self):
        print("Running")

    def sleep(self):
        print("sleeping")


p = Person()
print(p.name,p.age)
p.run()
p.sleep()



class Person:

    def __init__(self, nam, ag):
        self.nam = nam
        self.ag = ag

    def display(self):
        print(self.nam, self.ag)


p1 = Person("amar", 30)
p1.display()

# Create a Class with instance attributes
# Write a Python program to create a Vehicle class with max_speed and mileage instance attributes.
class Vehicle:  # class
    def __init__(self, max_speed, mileage):  # constructor
        self.max_speed = max_speed
        self.mileage = mileage


# 'v' is object
v = Vehicle(120, 25)
print(v.max_speed, v.mileage)


# Create a Vehicle class without any variables and methods
class Vehicle:  # class
    pass


# Create a Circle class and initialize it with radius. Make two methods getArea and getCircumference inside this class.
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        print(3.14 * (self.radius ** 2))

    def circumference(self):
        print(3.14 * self.radius * 2)


x = int(input("enter circle radius:"))
a = Circle(x)
a.area()
a.circumference()
"""

Create a Temperature class. Make two methods :
1. convertFahrenheit - It will take celsius and will print it into Fahrenheit. (0°C × 9/5) + 32
2. convertCelsius - It will take Fahrenheit and will convert it into Celsius. (5°F − 32) × 5/9
"""


class Temperature:
    def __init__(self, tem):
        self.tem = tem

    def fahrenheit(self):
        print((self.tem * 9 / 5) + 32, "F")

    def celsius(self):
        print((self.tem - 32) * 5 / 9, "C")


x = int(input("enter temperature:"))
temp = Temperature(x)
temp.celsius()
temp.fahrenheit()


"""
Create a Student class and initialize it with name and roll number. Make methods to :
1. Display - It should display all information's of the student.
2. setAge - It should assign age to student
3. setMarks - It should assign marks to the student.
"""


class Student:
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll

    def display(self):
        print("Name:", self.name)
        print("Roll No. :", self.roll)
        print("Age:", self.age)
        print("Marks:", self.marks)

    def setage(self):
        self.age = int(input("enter age:"))

    def setmarks(self):
        self.marks = int(input("enter marks"))


name = input("enter name:")
roll = int(input("enter roll no. :"))

s = Student(name, roll)
s.setage()
s.setmarks()
s.display()
