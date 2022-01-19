# Write a program to create a function that takes two arguments, name and age, and print their value.
def person(name, age):
    print(name, age)


person("amar", 25)




# Write a program to create function func1() to accept a variable length of arguments and print their value.
def func1(*args):
    for i in args:
        print(i)


func1(20, 40, 60)
func1(80, 100)


# Create a function with default argument
# Write a program to create a function show_employee() using the following conditions.
# It should accept the employee’s name and salary and display both.
# If the salary is missing in the function call then assign default value 9000 to salary
def show_employee(name,salary=9000):
    print(name,salary)


show_employee("amar")
show_employee("viveka",100000)



# Create an inner function to calculate the addition in the following way
# Create an outer function that will accept two parameters, a and b
# Create an inner function inside an outer function that will calculate the addition of a and b
# At last, an outer function will add 5 into addition and return it
def outer(a, b):
    def addition(a, b):
        return a + b

    add = addition(a, b)
    return add + 5


x = outer(20, 30)
print(x)



# Define a function that accepts 2 values and return its sum, subtraction and multiplication.
def x(a, b):
    h = a + b
    i = a - b
    j = a * b
    print("sum:",h,"sub:",i, "mul:",j)


a = int(input("enter 'a' value:"))
b = int(input("enter 'b' value"))
x(a, b)

#  Define a function that accepts roll number and returns whether the student is present or absent.
attendance = [12345, 23456, 34567, 45678, 56789, 67890, 78901, 89012, 90123]


def roll_no(x):
    if x in attendance:
        print(x, ":student is present")
    else:
        print(x, ":student is absent")


x = int(input("enter roll number:"))
roll_no(x)

# Define a function in python that accepts 3 values and returns the maximum of three numbers.
def value(a, b, c):
    if a < b < c:
        print(c, "maximum value")
    elif a > b > c:
        print(a, "maximum value")
    else:
        print(b, "maximum value")


a = int(input("enter 'a' value:"))
b = int(input("enter 'b' value:"))
c = int(input("enter 'c' value:"))
value(a, b, c)



# Define a function that accepts a number and returns whether the number is even or odd.
def number(a):
    if a % 2 == 0:
        print("Even number:", a)
    else:
        print("odd number:", a)


a = int(input("enter 'a' value:"))
number(a)



# Define a function which counts vowels and consonant in a word.
def word(x):
    v = 0
    c = 0
    for i in range(len(x)):
        if x[i] in ['a', 'e', 'i', 'o', 'u']:
            v = v + 1
        else:
            c = c + 1

    print("count of vowels:", v)
    print("count of consonant:", c)


x = input("enter word--:")
word(x)



# Define a function that returns Factorial of a number.
def factorial(x):
    y = 1
    for i in range(1, x):
        x = x * i
    print(x)


x = int(input("enter factorial value:"))
factorial(x)



# Define a function that accepts lowercase words and returns uppercase words.

def upper(x):
    y = x.upper()
    print(y)


x = input("enter lower case word:")
upper(x)



# Define a function that accepts radius and returns the area of a circle.
# A = pi * r^2
def area_circle(r):
    area = 3.14 * (r ** 2)
    print(area)


r = int(input("enter the radius:"))
area_circle(r)

"""
lambda function:
# Write a function which takes two arguments: a and b and returns the multiplication of them: a*b. 
Assign it to a variable named: f.
"""
f = lambda a, b: a * b
print(f(3, 6))




