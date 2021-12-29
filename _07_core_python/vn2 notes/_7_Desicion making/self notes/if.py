"""
If statement:
     'if' statement is a single line condition statement.'if' condition is true  then output is print .
     'if' statement always true statement.
     True - except '0', None, null, empty. remaining all are true
     False - '0', None, null, empty
Ex:
"""
if 0:
    print("output is zero")  # if statement is false so output is not shown in console

if 10:
    print("output is 10")  # if statement is True so output is  shown in console

if None:
    print("None")
if "False":
    print("False")
if False:
    print("Hello")
if True:
    print("True")
if "True":
    print("World")

"""
If condition  using operators
Arithmetic operators:"""
print("----------If statement  using Arithmetic operators----------")
a = 10
b = 10

if a + b:
    print("output value:", a + b)
if a - b:
    print("output value:", a - b)  # output is '0'.so, 0 is false.output is not shown
if a * b:
    print("output value:", a * b)
if a / b:
    print("output value:", a / b)
if a // b:
    print("output value:", a // b)
if a % b:
    print("output value:", a % b)
if a ** b:
    print("output value:", a ** b)

print("----------If statement  using Assignment operators----------")
a = 10
b = 10
if a == (10 + 30) and a == (10 + 30):
    print("output value:", a == b)  # output is '0'.so, 0 is false.output is not shown
if a >= b:
    print("output value:", a >> b)


print("----------If statement  using Comparison operators----------")

if a == b:
    print("output value:", a == b)
if a < b:
    print("output value:", a < b)  # condition is false
if a > b:
    print("output value:", a > b)  # condition is false
if a >= b:
    print("output value:", a >= b)
if a <= b:
    print("output value:", a <= b)
if a != b:
    print("output value:", a != b)  # condition is false

print("----------If statement  using Logical operators----------")

if a == b and b == a:
    print("output value:True")
if a <= b and b <= a:
    print("output value:True")
if a == b or b == a:
    print("output value:True")
if a <= b or b <= a:
    print("output value:True")
if a != b and a == b:
    print("output value:True")
if a != b or a == b:
    print("output value:True")

print("----------If statement  using identity operators----------")

if a is b:
    print("output value:True")
if a is not b:
    print("output value:True")
if (a is b) or (a is not b):
    print("identity operator")

print("----------If statement  using Membership operators----------")
a = 1
b = [20, 3, 1, 1, ]
if a in b:
    print("output value:True")
if a not in b:
    print("output value:True")
if (a in b) and (a not in b):
    print("identity operator")

print("----------If statement  using Bitwise operators----------")
a = 10
b = 200

if a | b:
    print("output value:", a | b)
if a & b:
    print("output value:", a & b)
if ~a:
    print("output value:", ~a)
if a ^ b:
    print("output value:", a ^ b)


