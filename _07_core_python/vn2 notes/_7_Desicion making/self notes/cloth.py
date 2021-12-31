print("/'sh/' for Short")
print("/'p/' for Pants")
print("/'t/' for t-shirts")
opt = input("Enter the product code (/'sh/',/'p/',/'sht/')?:")
amt = int(input("Enter the amount:"))
if opt == 'sh':
    if 0 < amt < 100:
        dis = 0
    elif 100 < amt < 200:
        dis = (amt * 0.05)
    elif 201 < amt < 300:
        dis = amt * 0.1
    else:
        dis = amt * 0.18
elif opt == 'p':
    if 0 < amt < 100:
        dis = amt * 0.03
    elif 100 < amt < 200:
        dis = amt * 0.08
    elif 201 < amt < 300:
        dis = amt * 0.12
    else:
        dis = amt * 0.20
if opt == 't':
    if 0 < amt < 100:
        dis = amt * 0.05
    elif 100 < amt < 200:
        dis = amt * 0.10
    elif 201 < amt < 300:
        dis = amt * 0.15
    else:
        dis = amt * 0.22
bill_amt = amt - dis
print("Customer has to pay:",bill_amt)
