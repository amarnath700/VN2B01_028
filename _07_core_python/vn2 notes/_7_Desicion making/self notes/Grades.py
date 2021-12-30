"""
Accept the percentage from the user and display the grade according to following criteria:
a. Below 25 - D
b. 25 to 45 - C
c.45 to 50 - B
d. 50 to 60 - B+
e. 60 to 80 - A
f. Above 80 - A+

"""

x = int(input("Enter marks:"))
if x > 100:
    print("enter valid marks")
else:
    if x < 25:
        print(" Grade is D :", x)
    elif 25 <= x < 45:
        print("Grade is C :", x)
    elif 45 <= x < 50:
        print("Grade is B :", x)
    elif 50 <= x < 60:
        print("Grade is B+ :", x)
    elif 60 <= x < 80:
        print("Grade is A :", x)
    else:
        print("Grade is A+ :", x)