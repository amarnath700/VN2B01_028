x = int(input("enter x number:"))
n = int(input("enter n value:"))
i = 1
while i <= n:
    n = n * i
    print(int(x**n)/n)
    i += 1