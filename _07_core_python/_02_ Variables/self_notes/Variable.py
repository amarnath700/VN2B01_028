"""
python Variable:
In python,Variables are containers for storing data values
A variable is created the moment you first assign a value to it .
A Python variable is a reserved memory location to store values.
In other words, a variable in a python program gives data to the computer for processing.
Variable also known as identifier and used to hold value
Every value in Python has a datatype.
python has no command to declaring a variable
x = 100
here "x" is variable
" = " is operator
" 100 " is value

LHS -> should always be a variable
RHS -> finally should become value



"""
num = 80  # write operation, dynamically typed program,so no need data type
print(num)  # output is 80.
print(type(num))  # output is int
print(id(num))
'''output is 2384604760784.location id.
if  we give same values to multiple variables we get same id.
example:'''
x = 80
z = 80
print(id(x))
print(id(z))  # for all 3 variables ,we got same value location id.
y = 25  # write operation
"""
process of value allocate:

step-1: Load the statement

step-2: Execution starts from R.H.S = L.H.S

step-3: In R.H.S ,finds the type of data like int, float, boolean, str

step-4: If any expression , it performs the operation.final value, 
it converts final value into binary format
Binary value of 25 = 0011001

step-5: Binary value will be allocated some memory
id :2065680499696
step-6: Memory address will be referred to variable
this is write operation or create operation
"""
print(y)
print(id(y))
# read operation
'''
Read operation:
step-1: python will go to the variable referred  address.
step-2: it will load the binary value of that address.
step-3: convert to decimal value.
step-4: gives(print function) value is on console.
'''
x = 5
print(x)
print(id(x))
x = 7
print(x)
print(id(x))
x = 10
print(x)
print(id(x))
y = 5
print(y)
print(id(y))
"""
 Note: we assign only one value to one variable.
 if we assign 2nd value to the same variable . 1st value goes garbage collection
  """
"""
variable names:
name must and should use only alpha,numeric and underscore(_).
1. 1st letter starts _(underscore) or letters (lowercase)
2. Don't use numbers
3. Don't use keywords ,special symbols
"""
_AGE = 25
print(_AGE)

"""1age = 2  # variable is invalid decimal literal
print(1age)"""

_1age = 200  # variable is invalid decimal literal
print(_1age)


"""
variables are case sensitive.
ex:
AGE,AGe,AgE,Age,aGe,agE,age
these are are different variable.
Note - Variable name should not be a keyword.
"""
AGE = 1
AGe = 3
AgE = 6
Age = 10
aGe = 15
agE = 20
age = 25
print(AGE)
print(AgE)
print(age)
print(aGe)


x = 25  # value is integer data type
print(x)
print(type(x))
print(id(x))

x = 25.5  # value is float data type
print(x)
print(type(x))
print(id(x))

x = 25j  # value is complex data type
print(x)
print(type(x))
print(id(x))

x = "Amar"  # value is string data type
print(x)
print(type(x))
print(id(x))

x = True   # value is boolean data type
print(x)
print(type(x))
print(id(x))



