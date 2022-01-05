# write a program to print number from 1 to 20 except multiple of 2 and 3.
i = 1
while i <= 20:
    if i % 2 != 0:
        if i % 3 != 0:
            print(i)
    i = i + 1

for x in range(0, 20):
    if x % 2 != 0:
        if x % 3 != 0:
            print(x, end=" ")
