"""
If-Else:
An if statement can be followed by an optional else statement, which executes when the boolean expression is FALSE.
An else statement can be combined with an if statement. An else statement contains the block of code that executes
if the conditional expression in the if statement resolves to 0 or a FALSE value.
The else statement is an optional statement and there could be at most only one else statement following if.

Syntax:
The syntax of the if...else statement is −

if expression:
   statement(s)
else:
   statement(s)
"""
# Take values of length and breadth of a rectangle from user and check if it is square or not.


le = int(input("Enter Value of Length:"))
br = int(input("Enter Value of Berth:"))

if le == br:
    print("it is a Square")
else:
    print("it is  a Rectangle ")

"""
#  Take two int values from user and print greatest among them.
x = int(input("Enter Value:"))
y = int(input("Enter Value:"))

if x > y:
    print("x is greatest:", x)
else:
    print("y is greatest:", y)
"""
"""
A shop will give discount of 10% if the cost of purchased quantity is more than 1000.
Ask user for quantity
Suppose, one unit will cost 100.
Judge and print total cost for user.
"""
"""
x = 1000
print(x)
quantity = float(input("Enter Quantity:"))
if x <= quantity:
    print("total cost :", quantity-(quantity*0.10))
else:
    print("purchase is less than 1000:", quantity)
    
   """

#  write a code to check no. is divide by 7 or not.
"""
x = int(input("enter value:"))
if x % 7 == 0:
    print("x is divide by 7:", x)
else:
    print("x is not divide by 7")

"""
