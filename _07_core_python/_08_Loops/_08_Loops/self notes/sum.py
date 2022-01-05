# a+ar+ar^2+-----+ar^n
n = int(input("enter n value:"))
r = int(input("enter r value:"))
a = int(input("enter a value:"))
i = 0
s = 0
while i <= n:
    s = s + a*(r**i)
    i += 1
print(s + a)

