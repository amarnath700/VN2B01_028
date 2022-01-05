# write a program to check whether a number is prime or not ?
x = int(input("Enter number:"))
count = 0

for i in range(2, (x // 2 + 1)):
    if x % i == 0:
        count = count + 1
        break

if count == 0 and x != 1:
    print(" %d is a Prime Number" % x)
else:
    print(" %d is not a Prime Number" % x)
