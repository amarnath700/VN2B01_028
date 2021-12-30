#  Purchase any product in online portal.
x = int(input(" Enter value:"))
y = "laptop"
z = "mobile"
if 29999 <= x <= 60000:
    print("Purchased product is  ", y)
elif 9999 <= x < 29999:
    print("Purchased product is  ", z)
else:
    print(" Product is not available")