x = int(input("enter the kilometers:"))
if 0 <= x <= 10:
    print("total bill:", x * 11)
elif 10 < x <= 90:
    print("total bill", (x * 10))
elif 90 < x:
    print("total bill", (x * 9))
else:
    print("you are not travel")
