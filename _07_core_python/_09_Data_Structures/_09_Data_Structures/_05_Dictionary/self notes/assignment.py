# create nested dictionary
x = input("enter family name:")
i = 0
d = f = e = " "
while i <= 2:
    a = input("name:")
    b = input("age:")
    c = input("relation:")
    if i == 0:
        d = d + a + b + c
        i = int(input("enter i value:"))
    elif i == 1:
        f = f + a + b + c
        i = int(input("enter i value:"))

    elif i == 2:
        e = e + a + b + c
        i = int(input("enter i value:"))

    else:
        print("entered wrong value")
print(dict(d + e + f))


