"""
Iterative Statements or loop statements:
      some Block of statement can execute continuously.
      it stops,when condition is false. Otherwise, state execute continuously.

there are 2 types of iterative statements:
1. for loop
2. while loop

statement execute 1 time is called iteration.
statement execute n times is called n iterations.

****important:need to follow in loop
1. loop variable initialize
2. condition
3. loop variable update.
"""
"""
While loop:
While Loop is used to repeat a block of code. Instead of running the code block once, 
It executes the code block multiple times until a certain condition is met.
syntax:

while condition:
    statement1
    -
    -
    -
statement end
"""
# print n natural numbers using while loop.
n = int(input("enter n value:"))
i = 0  # loop variable initialize
while i <= n:  # condition
    print(i)
    i = i + 1  # loop variable update
print("End loop")

"""
for loop :
For loop is used to iterate over elements of a sequence. It is often used when you have a piece of code which 
you want to repeat “n” number of time.
syntax:

for variable in sequence or range:
           statement
           
           
.
     for loop can execute in  2 types
     1. sequence
     2. range()
     
1. sequence:
        syntax:
     
2. range()

To loop through a set of code a specified number of times, we can use the range() function,
The range() function returns a sequence of numbers, starting from 0 by default, 
and increments by 1 (by default), and ends at a specified number.
        range(start,stop, step)
        start = starting value = loop variable initialize
        stop  = end value       = condition
        step  = difference      = loop variable update.
     

"""
n = int(input(" enter n value:"))
for i in range(n):
    print(i)

"""
nested loop:
        nested loop means, we use loop inside the loop.
    BY USING NESTED LOOP, we created out put in rows and columns.
"""
x = int(input("enter x value"))
for i in range(n):
    for j in range(n):
        print("*", end=" ")
    print(" ")
