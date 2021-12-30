"""
Accept the marked price from the user and calculate the net amount as(marked Price - Discount)
to pay according to following criteria:
marked Price       Discount
>10000             -  20%
>7000 and <= 10000  -  15%
<=7000             -  10%

"""

x = int(input(" Enter the Marked price:"))
if x > 10000:
    print("Net amount:", x - (x * 0.2))
elif 7000 < x <= 10000:
    print("Net amount:", x - (x * 0.15))
else:
    print("Net amount:", x - (x * 0.1))
