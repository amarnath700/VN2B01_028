x = int(input("enter total electricity units:"))
if 0 <= x <= 100:
    print("total bill is 0")
elif 100 < x <= 200:
    print("total electricity bill",(x-100)*5)
elif 200 < x:
    print("total bill", ((x-200)*10)+(100*5))
else:
    print("you entered wrong units")
