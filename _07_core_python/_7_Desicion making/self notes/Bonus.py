"""
A Company decide to give bonus to employee according to following criteria:
Time period of service     Bonus
More than 10 years      -   10%
>= 6 and <= 10          -   8%
Less than 6 years       -   5%
Ask user for their salary and years of service and print the bonus amount.
"""
x = float(input("Enter the Salary:"))
y = float(input("Enter the Year of service:"))
if y > 10:
    print("Bonus Amount:", x * 0.1)

elif 6 <= y <= 10:
    print("Bonus Amount:", x * 0.08)

else:
    print("Bonus Amount:", x * 0.05)

