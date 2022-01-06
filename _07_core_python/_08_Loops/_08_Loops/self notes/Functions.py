"""
Function:
main use of function is re-usability.
it is easy debugging.

Function Definition:
every function should start with " def " Keyword.
every function should have named (not equal to any keyword).
parameters/arguments(optional) included in b/w parenthesis.
every function name with or without arguments should end with. " : ".
every function return - empty or value.
in python function multi-value return can be done(in tuple).

Function call:

function call have function name and parameters or arguments which are all equal to the function definition.
"""


# function to add 2 numbers.
def add(a, b):
    sum = a + b
    return sum


a = int(input("enter a value:"))
b = int(input("enter b value:"))
res = add(a, b)
print("Result=", res)
