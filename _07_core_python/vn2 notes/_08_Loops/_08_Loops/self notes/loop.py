"""
Iterative Statements or loop statements:
      some Block of statement can execute continuously.
      it stops,when condition is false. Otherwise, state execute continuously.

there are 2 types of iterative statements:
1. for loop
2. while loop

if statement execute 1 time is called iteration.
if statement execute n times is called n iterations.

****important:need to follow in loop
1. loop variable initialize
2. condition
3. loop variable update.
"""
"""

syntax:
while loop:
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
    BY USING NESTED LOOP, we created out put in rows and columns.
"""
x = int(input("enter x value"))
for i in range(n):
    for j in range(n):
        print("*", end=" ")
    print(" ")
