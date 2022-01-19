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
def add(a,b):
in this a,b are the parameters

res = add(a, b)  # function call
a,b are the arguments

Parameters or Arguments?
The terms parameter and argument can be used for the same thing: information that are passed into a function.

From a function's perspective:

A parameter is the variable listed inside the parentheses in the function definition.

An argument is the value that is sent to the function when it is called.
"""


# function to add 2 numbers.
def add(a, b):  # user define function
    sum = a + b
    return sum


# here function name is add(a,b)

a = int(input("enter a value:"))  # main program
b = int(input("enter b value:"))
res = add(a, b)  # function call
print("Result=", res)

"""
Types of Arguments:
There are 4 types of Arguments
1.Required Arguments.
2.keyword Arguments.
3.Default Arguments.
4.variable length Arguments.


Required Argument: 
number of arguments should be same in both function call and function definition
order position should be same.
"""


def display(a, b):
    print(a, b)


display(a=20, b=10)
#    or
display(20, 10)
"""
keyword Arguments:
 order or position is not required
 initialization will be done based on keyword name
 """


def display(a, b):
    print(a, b)


display(b=20, a=10)
"""
Default Argument:
Number of Arguments need not be match with both function call and function def
Some of the Arguments will be consider as Default arguments
"""


def display(name, course="b.tech"):
    print(name)
    print(course)


display(name="Amar", course="m.tech")
display(name="viveka")

"""

Variable length Argument:
it will accept arbitrary no. of argument.
by placing * as prefix to the argument of function definition.
" * " means number of arguments

"""


def display(*course):
    for i in course:
        print(i, end=",")


display("java", "python", "c- lang", "c++ lang")

"""
Anonymous function or lambda functions:
        * this function do not defined by def keyword.
        * return expression but not value
        * one-line function
        * cannot access global variable
        * defined by using lambda keyword
        * this function allow any no. of arguments
        syntax:
            lambda arguments:expression
        """
print()

y = lambda a, b: a + b
print(y(20, 30))
