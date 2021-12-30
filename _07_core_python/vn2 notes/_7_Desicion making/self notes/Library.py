"""
Accept the number of days from the user and calculate the charges
for library according to following:
till five days:Rs 2/day
six to ten days:Rs 3/day
11 to 15 days:Rs 4/day
after 15 days:Rs 5/day

"""
x = int(input("Enter no. of days:"))
if x > 15:
    print("Charges for Library:", x * 5)
elif 11 <= x <= 15:
    print("Charges for Library:", x * 4)
elif 6 <= x <= 10:
    print("Charges for Library:", x * 3)
elif 1 <= x <= 5:
    print("Charges for Library:", x * 2)
else:
    print("No Charges")

