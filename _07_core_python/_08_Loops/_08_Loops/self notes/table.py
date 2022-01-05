#  write a program to print table of number accepted from user.
"""x = int(input("enter table no:"))
i = 0
while i <= 10:
    print(x, "*",  i, "=", i * x)
    i = i + 1
"""
x = int(input("enter table number:"))
for i in range(1, 11):
    print(x, "*", i, "=", i * x)
