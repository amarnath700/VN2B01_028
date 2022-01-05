"""
Global variable:
Variables that are created outside a function are known as global variables.
Global variables can be used by everyone, both inside of functions and outside.

Normally, when you create a variable inside a function, that variable is local, and can
only be used inside that function.

The global Keyword:
To create a global variable inside a function, you can use the global keyword.

"""
a = 20  # global Variable


def display():
    global b
    b = 10    # by the giving global keyword to b variable .
    print(a)
    print(b)


display()
print(a)
print(b)
"""
Type Casting or type conversion:

   By using Type Casting we can convert one data type into another data type.
   ex:
"""
x = 50.256  # Here  50.256 is float.
print(type(x))  # output is float

x = int(x)  # Here float value is converting into integer

print(type(x))  # output is int

""" 
In all cases Type casting won't works. int,float any values can convert into str.
but, str value not convert into int or float.if str value is numeric value is convert into int or float.
Ex:
   """

x = "Amar"  # Here Amar is string
print(type(x))  # output is str

x = int(x)  # Here we're converting  string value to integer.we get error
print(type(x))

"""
There are two type of type casting
Implicit casting:
       if a compiler converts one data type into another type data automatically then we called as implicit casting.
there is no data loss
"""
x = "9"
print(x)
print(type(x))
y = int(x)
print(y)
print(type(y))
"""
Explicit casting:
        when a data of one type is converted explicity to another type wth 
        the help of pre-define function we called explicit casting.
        there is data loss due to force-ly conversing data type 
"""
x = 12.23
print(x)  # output is 12.23
print(type(x))  # float
y = int(x)
print(y)  # Output is 12 data loss
print(type(y))  # int
