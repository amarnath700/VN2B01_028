"""
elif Statement
The elif statement allows you to check multiple expressions for TRUE and execute a block of code
as soon as one of the conditions evaluates to TRUE.
Similar to the else, the elif statement is optional.
However, unlike else, for which there can be at most one statement,
there can be an arbitrary number of elif statements following an if.

syntax
if expression1:
   statement(s)
elif expression2:
   statement(s)
elif expression3:
   statement(s)
else:
   statement(s)
"""
"""
x = int(input("x value:"))
y = int(input("y value:"))
if x > y:
    print(" x is greater than y")
elif x < y:
    print("x is less than y")
else:
    print("Both x and y are equal")
"""

#  Take input of age of 3 people by user and determine oldest and youngest among them.
"""
x = int(input("Enter x person age:"))
y = int(input("Enter y person age:"))
z = int(input("Enter z person age:"))

if x <= y and x <= z:
    print(" x is youngest:", x)
    if y <= z:
        print("z is oldest:", z)
    else:
        print("y is oldest", y)
elif y <= x and y <= z:
    print("y is youngest ", y)
    if x <= z:
        print("z is oldest:", z)
    else:
        print("x is oldest", x)

elif z <= x and z <= y:
    print("z is youngest ", z)
    if x <= y:
        print("y is oldest:", y)
    else:
        print("x is oldest", x)

else:
    print("All are equal", z)

"""
"""

A school has following rules for grading system:
a. Below 25 - F
b. 25 to 45 - E
c. 45 to 50 - D
d. 50 to 60 - C
e. 60 to 80 - B
f. Above 80 - A
Ask user to enter marks and print the corresponding grade.


x = int(input("Enter marks:"))
if x > 100:
    print("enter valid marks")
else:
    if x < 25:
        print(" Grade is F :", x)
    elif 25 <= x < 45:
        print("Grade is E :", x)
    elif 45 <= x < 50:
        print("Grade is D :", x)
    elif 50 <= x < 60:
        print("Grade is C :", x)
    elif 60 <= x < 80:
        print("Grade is B :", x)
    else:
        print("Grade is A:", x)
"""
#  The given number is of one digit or two digits or three digits or more than three digits.
x = input("enter the numbers:")
y = len(x)
print("x value length:", y)
if y == 1:
    print("Given number is one digit:", x)
elif y == 2:
    print("Given number is Two digit:", x)
elif y == 3:
    print("Given number is three digit:", x)
else:
    print("Given number is more than three digit:", x)

"""
x = input("enter the numbers:")
if 0 < y < 10:
    print("Given number is one digit:", x)
elif 10 <= y < 100:
    print("Given number is Two digit:", x)
elif 100 <= y < 1000:
    print("Given number is three digit:", x)
else:
    print("Given number is more than three digit:", x)
"""


