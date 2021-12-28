"""
Python Operators:
Operators are used to perform operations on variables and values.

Operators are special symbols in python that carry out arithmetic or logical computation
types of Operators:
1.Arithmetic operator(+,-,*, etc.)
2.Comparison operator(<,>,=, etc.)
3.Logical operator(and, or, not)
4.Bitwise operatorBitwise operators are used to compare (binary) numbers(|, &, etc.)
5.Assignment operator(==,+=, etc.)
6.Identity operator(is, is not)
7.Membership operators(in,not in)
"""
x = 3
y = 5

print(x * y)  # we use * operator for multiple of two values

"""
Arithmetic operator:
        Arithmetic operators are used with numeric values to perform common mathematical operations.
(+,-,*, etc.)"""
x = 7
y = 8
print(x + y)  # addition
print(x - y)  # subtraction
print(x * y)  # multiplication
print(x / y)  # division
print(x % y)  # remainder
print(x ** y)  # power value
print(x // y)  # floor division


"""
Comparison operator:
 Comparison operators are used to compare two values.(<,>,=, etc.)
"""
x = 5
y = 6
print(x > y)  # greater than
print(x < y)  # less than
print(x == y)  # equals to
print(x != y)  # not equals to
print(x >= y)  # greater than or equal to
print(x <= y)  # less than or equal to

"""
Logical operator:
Logical operators are used to combine conditional statements(and, or, not)
"""
x = 10
print(x > 3 and x < 11)  # and operator
print( not(x > 3 and x < 11 ))  # not operator
print(x < 3 or x < 11)  # or operator


"""
Bitwise operator:
Bitwise operators are used to compare (binary) numbers(|, &, etc.)
"""


"""
Identity Operators:
Identity operators are used to compare the objects, not if they are equal, 
but if they are actually the same object, with the same memory location
"""
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)  # returns True because z is the same object as x
print(x is y)  # returns False because x is not the same object as y, even if they have the same content
print(x == y)  # to demonstrate the difference between "is" and "==":
# this comparison returns True because x is equal to y
print(x is not z)  # returns False because z is the same object as x
print(x is not y)  # returns True because x is not the same object as y, even if they have the same content
print(x != y)  # to demonstrate the difference between "is not" and "!=":
# this comparison returns False because x is equal to y


"""
Membership Operators:
Membership operators are used to test if a sequence is presented in an object.
"""


x = ["apple", "banana"]
print("banana" in x)  # returns True because a sequence with the value "banana" is in the list
print("grapes" in x)
print("grapes" not in x)


