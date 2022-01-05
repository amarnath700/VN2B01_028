10  # static value
x = 20  # Harding manner
x = input()  # dynamic manner,  if we not give any data type to before input it is default string
"""
Decision-making is anticipation of conditions occurring while execution of the program and specifying
actions taken according to the conditions.
Decision structures evaluate multiple expressions which produce TRUE or FALSE as outcome.
You need to determine which action to take and which statements to execute if outcome is TRUE or FALSE otherwise.
Python programming language assumes any non-zero and non-null values as TRUE, and if it is either zero or null,
then it is assumed as FALSE value.



if statements:
An if statement consists of a boolean expression followed by one or more statements
The if statement contains a logical expression using which data is compared and a decision is made
based on the result of the comparison.

Syntax=
if expression:
   statement(s)
"""
if 10 > 5:
    print("Output Value")

if '0':
    print("Output Zero")

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
x = 10
y = 20
if x < y:
    print("y is greater than x ")

else:
    print("x is greater than y")

"""
elif Statement
The elif statement allows you to check multiple expressions for TRUE and execute a block of code as soon as one of the conditions evaluates to TRUE.

Similar to the else, the elif statement is optional. However, unlike else, for which there can be at most one statement, there can be an arbitrary number of elif statements following an if.

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
x = int(input("x value:"))
y = int(input("y value:"))
if x > y:
    print(" x is greater than y")
elif x < y:
    print("x is less than y")
else:
    print("Both x and y are equal")
