x = [10, 20, "amar", 2.5, "ravi", 99]
y = [20, 2.5, "viveka", "john", 888, "1d5d"]
z = ["amar", "viveka", 2.5, 20, "raja", "vijay"]

# Find the length of a Set in Python
print("----Find the length of a Set in Python----")
x1 = set(x)
print(len(x1), type(x1))  # 6 <class 'set'>
y1 = set(y)
print(len(y1), type(y1))

# Maximum and Minimum in a Set
print("----Maximum and Minimum in a Set----")
a = {10, 2.5, 3, 100, 555, 2.36}
print(max(a), min(a), type(a))

# Remove items from Set
a = list(a)
print(len(a))
i = 0
while i <= 2:
    a.pop(i)
    print(set(a))
    i = i+1

# Check if two lists have at-least one element common.

print("common elements", x1 & y1)

# Python program to find common elements in three lists using sets
print("common elements in 3 sets", x1 & y1 & set(z))

# Find missing and additional values in two lists
a = x1 & y1
b = x1.symmetric_difference(y)
print("missing value:", a, "Additional values in 2 sets:", b)

#
