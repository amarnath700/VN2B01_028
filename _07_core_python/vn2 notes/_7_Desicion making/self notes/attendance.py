"""
Accept the following from the user and calculate the percentage of class attendance:
a. Total number of working days
b. Total number of days for absent

After calculating percentage show that,if the percentage is less than 75,
than student will not be able to sit in exam.

"""
x = int(input("Enter no. of working days:"))
y = int(input("Enter no. of absent days:"))
z = ((x - y)/x) * 100
if z > 75:
    print("Sit in exam:", z)
else:
    print("Not able to sit in Exam:", z)

