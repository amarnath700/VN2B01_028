"""# prime numbers
minimum = int(input(" Please Enter the Minimum Value: "))
maximum = int(input(" Please Enter the Maximum Value: "))

for Number in range(minimum, maximum + 1):
    count = 0
    for i in range(2, (Number // 2 + 1)):
        if Number % i == 0:
            count = count + 1
            break

    if count == 0 and Number != 1:
        print(" %d" % Number, end='  ')"""
"""
lower_value = int(input("Please, Enter the Lowest Range Value: "))
upper_value = int(input("Please, Enter the Upper Range Value: "))

print("The Prime Numbers in the range are: ")
for number in range(lower_value, upper_value + 1):
    if number > 1:
        for i in range(2, number):
            if (number % i) == 0:
                break
        else:
            print(number)"""

# prime
"""
x = int(input("enter x value:"))
y = int(input("enter y value:"))
for n in range(x,y+1):
    if n > 1:
        for i in range(2,n):
            if (n % i) == 0:
                break
        else:
            print(n)"""

# factorial
"""
x = int(input("enter x value:"))
y = 1
for i in range(1, x + 1):
    y = y * i
print(y)

# pattern

x = int(input("enter value :"))
y = int(input("enter value :"))

for i in range(0, x + 1):
    for j in range(y - i, 0,-1):
        print(j,end=' ')
    print()

n = 5
k = 5
for i in range(0,n+1):
    for j in range(k-i,0,-1):
        print(j,end=' ')
    print()
    
# pattern
x = int(input("enter value :"))

for i in range(1, x + 1):
    for j in range(1, i+1):
        print(j, end=' ')
    print()

# sum
x = int(input("Enter value:"))
sum = 0
for i in range(1, x+1, 1):
    sum = sum + i
print(sum)

# count 75869
x = 75869
count = 0
while x != 0:
    x = x//10
    count = count + 1
print(count)

# Reverse
list1 = [10, 20, 30, 40, 50]
x = len(list1)-1
for i in range(x, -1,-1):
    print(list1[i])

# fabinaccl sequence
x = int(input("enter x value:"))
i = 0
j = 1
for k in range(0, x + 1, 1):
    print(i)
    r = i + j
    i = j
    j = r
From a list containing ints, strings and floats, make three lists to store them separately.
x = [10, 20.5, "Amar", "vivek", "chandra", 3.3, 5, 5.6, 5]
a = []
b = []
c = []
for i in x:
    if type(i) == int:
        a.append(i)
    elif type(i) == float:
        b.append(i)
    else:
        c.append(i)
print(a)
print(b)
print(c)

# Using range(1,101), make two list, one containing all even numbers and other containing all odd numbers.
x = []
y = []
for i in range(1, 101):
    if i % 2 == 0:
        x.append(i)
    else:
        y.append(i)
print(x)
print(y)
# From the two list obtained in previous question, make new lists,
# containing only numbers which are divisible by 4, 6, 8, 10, 3, 5, 7 and 9 in separate lists.
four = []
six = []
eight = []
ten = []
three = []
five = []
seven = []
nine = []
for i in range(1,101):
    if i % 4 == 0:
        four.append(i)
    if i % 6 == 0:
        six.append(i)
    if i % 8 == 0:
        eight.append(i)
    if i % 10 == 0:
        ten.append(i)
    if i % 3 == 0:
        three.append(i)
    if i % 5 == 0:
        five.append(i)
    if i % 7 == 0:
        seven.append(i)
    if i % 9 == 0:
        nine.append(i)
print(four)
print(six)
print(eight)
print(ten)
print(three)
print(five)
print(seven)
print(nine)
"""
# Using range(1,101), make a list containing only prime numbers.
x = []
n = 101
if i >= 1:
    for i in range(1,n+1):
        if n % i ==0:
            break
    else:
        print(x)



