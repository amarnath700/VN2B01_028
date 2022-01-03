"""
 A cloth showroom has announced the following discounts on the purchase of specific items :

Amount	   Shorts      	Pants	Shits/T-Shirts
0-100	     –           3%	      5%
101-200	     5%        	 8%	      10%
201-300	     10%    	 12%	  15%
Above 300	 18%         20%	  22%
Ask user to enter the amount and assign following code for the items such as
sh for shorts, p for pans and sht for shirts/t-shirts.
Compute the discount and net amount paid by customer.

"""
print(" welcome to cloth showroom")
x = int(input("enter shorts amount:"))
y = int(input("enter pants amount:"))
z = int(input("enter shirts/t-shirts amount:"))
if 0 < x or 0 < y or 0 < z:
    if 0 <= x <= 100:
        x1 = x
    elif 100 < x <= 200:
        x1 = x * 0.05
    elif 200 < x <= 300:
        x1 = x * 0.1
    elif 300 < x:
        x1 = x * 0.18
    else:
        x1 = 0
        print(" enter valid amount")
    if 0 <= y <= 100:
        y1 = y * 0.03
    elif 100 < y <= 200:
        y1 = y * 0.08
    elif 200 < y <= 300:
        y1 = y * 0.12
    elif 300 < y:
        y1 = y * 0.2
    else:
        y1 = 0
        print(" enter valid amount")
    if 0 <= z <= 100:
        z1 = z * 0.05
    elif 100 < z <= 200:
        z1 = z * 0.1
    elif 200 < z <= 300:
        z1 = z * 0.15
    elif 300 < z:
        z1 = z * 0.22
    else:
        z1 = 0
        print(" enter valid amount")
else:
    print("you are not purchased any cloth")

print("short discount:", x1)
print("pants discount:", y1)
print("shirts/t-shirts discount:", z1)
print("total amount:", (x - x1) + (y - y1) + (z - z1))
