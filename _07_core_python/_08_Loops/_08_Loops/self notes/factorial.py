# write a program of factorial of user given no.
x = int(input("enter factorial number:"))
i = 1
for i in range(1, x, 1):
    x = x * i
    i += 1
print(x)




