# Zero-exceptionError
"""
x = int(input("enter x value:"))
y = int(input("enter y value:"))

try:
    if x < y:
        print("y is greater than x", y / x)

except Exception as z:
    print("enter x value less than y", z)
finally:
    print("always i execute")"""
#
try:
    x = int(input("enter x value:"))
    y = int(input("enter y value:"))

    if x < y:
        print("y is greater than x", y / x)

except Exception as z:
    print("Error", z)
finally:
    print("always i execute")
