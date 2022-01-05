n = int(input("enter number:"))
i = 1
while i <= n:
    if i % 2 != 0:
        if i % 3 != 0:
            print(i)
    i = i + 1
