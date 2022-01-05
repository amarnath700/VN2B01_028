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
sh = int(input("enter short price:"))
p = int(input("enter pant price:"))
sht = int(input("enter shirts/t-shirts:"))
sh1 = sh
sh2 = sh * 0.05
sh3 = sh * 0.1
sh4 = sh * 0.18
p1 = p * 0.03
p2 = p * 0.08
p3 = p * 0.12
p4 = p * 0.2
sht1 = sht * 0.05
sht2 = sht * 0.1
sht3 = sht * 0.15
sht4 = sht * 0.22
if (0 <= sh <= 100) and (0 <= p <= 100) and (0 <= sht <= 100):
    print("discount and net amount:", sh1, p1, sht1, (sh - sh1) + (p - p1) + (sht - sht1))

elif (0 <= sh <= 100) and (0 <= p <= 100) and (101 <= sht <= 200):
    print("discount and net amount:", sh1, p1, sht2, (sh - sh1) + (p - p1) + (sht - sht2))

elif (0 <= sh <= 100) and (0 <= p <= 100) and (201 <= sht <= 300):
    print("discount and net amount:", sh1, p1, sht3, (sh - sh1) + (p - p1) + (sht - sht3))

elif (0 <= sh <= 100) and (0 <= p <= 100) and (300 < sht):
    print("discount and net amount:", sh1, p1, sht4, (sh - sh1) + (p - p1) + (sht - sht4))
#  1 1 4
elif (0 <= sh <= 100) and (101 <= p <= 200) and (0 <= sht <= 100):
    print("discount and net amount:", sh1, p2, sht1, (sh - sh1) + (p - p2) + (sht - sht1))

elif (0 <= sh <= 100) and (101 <= p <= 200) and (101 <= sht <= 200):
    print("discount and net amount:", sh1, p2, sht2, (sh - sh1) + (p - p2) + (sht - sht2))

elif (0 <= sh <= 100) and (101 <= p <= 200) and (201 <= sht <= 300):
    print("discount and net amount:", sh1, p2, sht3, (sh - sh1) + (p - p2) + (sht - sht3))

elif (0 <= sh <= 100) and (101 <= p <= 200) and (300 < sht):
    print("discount and net amount:", sh1, p2, sht4, (sh - sh1) + (p - p2) + (sht - sht4))
# 1 2 4
elif (0 <= sh <= 100) and (201 <= p <= 300) and (0 <= sht <= 100):
    print("discount and net amount:", sh1, p3, sht1, (sh - sh1) + (p - p3) + (sht - sht1))

elif (0 <= sh <= 100) and (201 <= p <= 300) and (101 <= sht <= 200):
    print("discount and net amount:", sh1, p3, sht2, (sh - sh1) + (p - p3) + (sht - sht2))

elif (0 <= sh <= 100) and (201 <= p <= 300) and (201 <= sht <= 300):
    print("discount and net amount:", sh1, p3, sht3, (sh - sh1) + (p - p3) + (sht - sht3))

elif (0 <= sh <= 100) and (201 <= p <= 300) and (300 < sht):
    print("discount and net amount:", sh1, p3, sht4, (sh - sh1) + (p - p3) + (sht - sht4))
# 1 3 4
elif (0 <= sh <= 100) and (300 < p) and (0 <= sht <= 100):
    print("discount and net amount:", sh1, p4, sht1, (sh - sh1) + (p - p4) + (sht - sht1))

elif (0 <= sh <= 100) and (300 < p) and (101 <= sht <= 200):
    print("discount and net amount:", sh1, p4, sht2, (sh - sh1) + (p - p4) + (sht - sht2))

elif (0 <= sh <= 100) and (300 < p) and (201 <= sht <= 300):
    print("discount and net amount:", sh1, p4, sht3, (sh - sh1) + (p - p4) + (sht - sht3))

elif (0 <= sh <= 100) and (300 < p) and (300 <= sht):
    print("discount and net amount:", sh1, p4, sht4, (sh - sh1) + (p - p4) + (sht - sht4))
# 1 4 4
elif (101 <= sh <= 200) and (0 <= p <= 100) and (0 <= sht <= 100):
    print("discount and net amount:", sh2, p1, sht1, (sh - sh2) + (p - p1) + (sht - sht1))

elif (101 <= sh <= 200) and (0 <= p <= 100) and (101 <= sht <= 200):
    print("discount and net amount:", sh2, p1, sht2, (sh - sh2) + (p - p1) + (sht - sht2))

elif (101 <= sh <= 200) and (0 <= p <= 100) and (201 <= sht <= 300):
    print("discount and net amount:", sh2, p1, sht3, (sh - sh2) + (p - p1) + (sht - sht3))

elif (101 <= sh <= 200) and (0 <= p <= 100) and (300 < sht):
    print("discount and net amount:", sh2, p1, sht4, (sh - sh2) + (p - p1) + (sht - sht4))
# 2 1 4
elif (101 <= sh <= 200) and (101 <= p <= 200) and (0 <= sht <= 100):
    print("discount and net amount:", sh2, p2, sht1, (sh - sh2) + (p - p2) + (sht - sht1))

elif (101 <= sh <= 200) and (101 <= p <= 200) and (101 <= sht <= 200):
    print("discount and net amount:", sh2, p2, sht2, (sh - sh2) + (p - p2) + (sht - sht2))

elif (101 <= sh <= 200) and (101 <= p <= 200) and (201 <= sht <= 300):
    print("discount and net amount:", sh2, p2, sht3, (sh - sh2) + (p - p2) + (sht - sht3))

elif (101 <= sh <= 200) and (101 <= p <= 200) and (300 <= sht):
    print("discount and net amount:", sh2, p2, sht4, (sh - sh2) + (p - p2) + (sht - sht4))
# 2 2 4
elif (101 <= sh <= 200) and (201 <= p <= 300) and (0 <= sht <= 100):
    print("discount and net amount:", sh2, p3, sht1, (sh - sh2) + (p - p3) + (sht - sht1))

elif (101 <= sh <= 200) and (201 <= p <= 300) and (101 <= sht <= 200):
    print("discount and net amount:", sh2, p3, sht2, (sh - sh2) + (p - p3) + (sht - sht2))

elif (101 <= sh <= 200) and (201 <= p <= 300) and (201 <= sht <= 300):
    print("discount and net amount:", sh2, p3, sht3, (sh - sh2) + (p - p3) + (sht - sht3))

elif (101 <= sh <= 200) and (201 <= p <= 300) and (300 < sht):
    print("discount and net amount:", sh2, p3, sht4, (sh - sh2) + (p - p3) + (sht - sht4))
# 2 3 4
elif (101 <= sh <= 200) and (300 < p) and (0 <= sht <= 100):
    print("discount and net amount:", sh2, p4, sht1, (sh - sh2) + (p - p4) + (sht - sht1))

elif (101 <= sh <= 200) and (300 < p) and (101 <= sht <= 200):
    print("discount and net amount:", sh2, p4, sht2, (sh - sh2) + (p - p4) + (sht - sht2))

elif (101 <= sh <= 200) and (300 < p) and (201 <= sht <= 300):
    print("discount and net amount:", sh2, p4, sht3, (sh - sh2) + (p - p4) + (sht - sht3))

elif (101 <= sh <= 200) and (300 < p) and (300 <= sht):
    print("discount and net amount:", sh2, p4, sht4, (sh - sh2) + (p - p4) + (sht - sht4))
# 2 4 4
elif (201 <= sh <= 300) and (0 <= p <= 100) and (0 <= sht <= 100):
    print("discount and net amount:", sh3, p1, sht1, (sh - sh3) + (p - p1) + (sht - sht1))

elif (201 <= sh <= 300) and (0 <= p <= 100) and (101 <= sht <= 200):
    print("discount and net amount:", sh3, p1, sht2, (sh - sh3) + (p - p1) + (sht - sht2))

elif (201 <= sh <= 300) and (0 <= p <= 100) and (201 <= sht <= 300):
    print("discount and net amount:", sh3, p1, sht3, (sh - sh3) + (p - p1) + (sht - sht3))

elif (201 <= sh <= 300) and (0 <= p <= 100) and (300 < sht):
    print("discount and net amount:", sh3, p1, sht4, (sh - sh3) + (p - p1) + (sht - sht4))
# 3 1 4
elif (201 <= sh <= 300) and (101 <= p <= 200) and (0 <= sht <= 100):
    print("discount and net amount:", sh3, p2, sht1, (sh - sh3) + (p - p2) + (sht - sht1))

elif (201 <= sh <= 300) and (101 <= p <= 200) and (101 <= sht <= 200):
    print("discount and net amount:", sh3, p2, sht2, (sh - sh3) + (p - p2) + (sht - sht2))

elif (201 <= sh <= 300) and (101 <= p <= 200) and (201 <= sht <= 300):
    print("discount and net amount:", sh3, p2, sht3, (sh - sh3) + (p - p2) + (sht - sht3))

elif (201 <= sh <= 300) and (101 <= p <= 200) and (300 <= sht):
    print("discount and net amount:", sh3, p2, sht4, (sh - sh3) + (p - p2) + (sht - sht4))
# 3 2 4
elif (201 <= sh <= 300) and (201 <= p <= 300) and (0 <= sht <= 100):
    print("discount and net amount:", sh3, p3, sht1, (sh - sh3) + (p - p3) + (sht - sht1))

elif (201 <= sh <= 300) and (201 <= p <= 300) and (101 <= sht <= 200):
    print("discount and net amount:", sh3, p3, sht2, (sh - sh3) + (p - p3) + (sht - sht2))

elif (201 <= sh <= 300) and (201 <= p <= 300) and (201 <= sht <= 300):
    print("discount and net amount:", sh3, p3, sht3, (sh - sh3) + (p - p3) + (sht - sht3))

elif (201 <= sh <= 300) and (201 <= p <= 300) and (300 < sht):
    print("discount and net amount:", sh3, p3, sht4, (sh - sh3) + (p - p3) + (sht - sht4))
# 3 3 4
elif (201 <= sh <= 300) and (300 < p) and (0 <= sht <= 100):
    print("discount and net amount:", sh3, p4, sht1, (sh - sh3) + (p - p4) + (sht - sht1))

elif (201 <= sh <= 300) and (300 < p) and (101 <= sht <= 200):
    print("discount and net amount:", sh3, p4, sht2, (sh - sh3) + (p - p4) + (sht - sht2))

elif (201 <= sh <= 300) and (300 < p) and (201 <= sht <= 300):
    print("discount and net amount:", sh3, p4, sht3, (sh - sh3) + (p - p4) + (sht - sht3))

elif (201 <= sh <= 300) and (300 < p) and (300 <= sht):
    print("discount and net amount:", sh3, p4, sht4, (sh - sh3) + (p - p4) + (sht - sht4))
# 3 4 4
elif (300 < sh) and (0 <= p <= 100) and (0 <= sht <= 100):
    print("discount and net amount:", sh4, p1, sht1, (sh - sh4) + (p - p1) + (sht - sht1))

elif (300 < sh) and (0 <= p <= 100) and (101 <= sht <= 200):
    print("discount and net amount:", sh4, p1, sht2, (sh - sh4) + (p - p1) + (sht - sht2))

elif (300 < sh) and (0 <= p <= 100) and (201 <= sht <= 300):
    print("discount and net amount:", sh4, p1, sht3, (sh - sh4) + (p - p1) + (sht - sht3))

elif (300 < sh) and (0 <= p <= 100) and (300 < sht):
    print("discount and net amount:", sh4, p1, sht4, (sh - sh4) + (p - p1) + (sht - sht4))
# 4 1 4
elif (300 < sh) and (101 <= p <= 200) and (0 <= sht <= 100):
    print("discount and net amount:", sh4, p2, sht1, (sh - sh4) + (p - p2) + (sht - sht1))

elif (300 < sh) and (101 <= p <= 200) and (101 <= sht <= 200):
    print("discount and net amount:", sh4, p2, sht2, (sh - sh4) + (p - p2) + (sht - sht2))

elif (300 < sh) and (101 <= p <= 200) and (201 <= sht <= 300):
    print("discount and net amount:", sh4, p2, sht3, (sh - sh4) + (p - p2) + (sht - sht3))

elif (300 < sh) and (101 <= p <= 200) and (300 <= sht):
    print("discount and net amount:", sh4, p2, sht4, (sh - sh4) + (p - p2) + (sht - sht4))
# 3 2 4
elif (300 < sh) and (201 <= p <= 300) and (0 <= sht <= 100):
    print("discount and net amount:", sh4, p3, sht1, (sh - sh4) + (p - p3) + (sht - sht1))

elif (300 < sh) and (201 <= p <= 300) and (101 <= sht <= 200):
    print("discount and net amount:", sh4, p3, sht2, (sh - sh4) + (p - p3) + (sht - sht2))

elif (300 < sh) and (201 <= p <= 300) and (201 <= sht <= 300):
    print("discount and net amount:", sh4, p3, sht3, (sh - sh4) + (p - p3) + (sht - sht3))

elif (300 < sh) and (201 <= p <= 300) and (300 < sht):
    print("discount and net amount:", sh4, p3, sht4, (sh - sh4) + (p - p3) + (sht - sht4))
# 4 3 4
elif (300 < sh) and (300 < p) and (0 <= sht <= 100):
    print("discount and net amount:", sh4, p4, sht1, (sh - sh4) + (p - p4) + (sht - sht1))

elif (300 < sh) and (300 < p) and (101 <= sht <= 200):
    print("discount and net amount:", sh4, p4, sht2, (sh - sh4) + (p - p4) + (sht - sht2))

elif (300 < sh) and (300 < p) and (201 <= sht <= 300):
    print("discount and net amount:", sh4, p4, sht3, (sh - sh4) + (p - p4) + (sht - sht3))

else:
    print("discount and net amount:", sh4, p4, sht4, (sh + sh4) + (p + p4) + (sht + sht4))
