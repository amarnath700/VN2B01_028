"""
Built in types:
In programming, data type is an important concept.
Variables can store data of different types, and different types can do different things.
Python has the following data types built-in by default, in these categories:
Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memory view
"""
"""
By using print() function we retrieve the data or result in console.
By using type() function we get data type of value.
By using id() function we get the reference address of value.
Ex:
"""
print("--------- Example of 3 function print(), type(), id() ----------")
x = 100
print(x)
type(x)
id(x)

"""
Numeric Type:
In numeric there are 3 data types. int,float,complex 
int     - from -n to n all numbers with out decimal value are integer
float   - numbers with decimals are float
complex - number are end with "j" either with decimal or without decimal  are complex
EX:
"""
print("--------- Example of 3 Numeric types int, float, complex ----------")
x = 100
print("Integer value is:", x, type(x), id(x))

y = 10.12
print("Float value is:", y, type(y), id(y))

z = 10j
print("Complex value is:", z, type(z), id(z))

#  conversions
a = 20.5
x = int(a)
print("Integer value is:", x, type(x), id(x))

y = float(x)
print("Float value is:", y, type(y), id(y))

z = complex(y)
print("Complex value is:", z, type(z), id(z))

"""
Important
y = "amar"
a = complex(y)
print("Complex value is:", z, type(z), id(z))
"""


"""
Text type:
 if we give  value to a variable with in  double quotation is known as sting
 ex: "python language", "100", "565sfd"
 """

print("--------- Example of String ----------")
x = "100"
print("value is:", x, type(x), id(x))

x = "111.11"
print("value is:", x, type(x), id(x))

x = "Amarnath"
print("value is:", x, type(x), id(x))


#  conversions
a = 20.5
x = str(a)
print("String value is:", x, type(x), id(x))

x = 5555
y = str(x)
print("String value is:", y, type(y), id(y))

y = 546j
z = str(y)
print("String value is:", z, type(z), id(z))

"""
Boolean type:
In Boolean there are 2 value true and false
when given value is equal to ' 0 ' in boolean it is false.
Except ' 0 ' all are true.
EX:
"""

x = 0
y = bool(x)
print("value is:", y, type(y), id(y))

x = "Amar"
y = bool(x)
print("value is:", y, type(y), id(y))
