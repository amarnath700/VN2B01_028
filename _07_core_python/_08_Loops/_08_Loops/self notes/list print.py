#  Write a for loop so that every item in the list is printed.

lst = ["koala", "cat", "fox", "panda", "chipmunk", "sloth", "penguin", "dolphin"]
for x in lst:
    print(x)

# Write a for loop which print "Hello!, " plus each name in the list. i.e.: "Hello!, Sam"
for x in lst:
    print("Hello!,", x)

# Using a for loop and .append() method append each item with a Dr. prefix to the lst.

lst1 = []
for x in lst:
    lst1.append("Dr." + x)
print(lst1)

# Write a for loop which appends the square of each number to the new list.
lst1 = [3, 7, 6, 8, 9, 11, 15, 25]
lst2 = []
for x in lst1:
    lst2.append(x ** 2)
print(lst2)

# Write a for loop using an if statement, that appends each number to the new list if it's positive.
lst1 = [111, 32, -9, -45, -17, 9, 85, -10]
lst2 = []
for x in lst1:
    if x >= 0:
        lst2.append(x)
print(lst2)

# Using for loop and if statement, append the value minus 1000 for each key to the new list if the value is above 1000.
# i.e.: if the value is 1500, 500 should be added to the new list.
dit = {"z1": 900, "t1": 1100, "p1": 2300, "r1": 1050, "k1": 3200, "g1": 400}
lst = []
for x in dit.values():
    if x >= 1000:
        lst.append(x - 1000)
print(lst)

# Write a for loop which appends the type of each element in the first list to the second list.
x = [23, "Python", 23.98]
y = []
for i in x:
    y.append(type(i))
print(y)

#  loop through a tuple of mixed data type and extract only integer values
x = (1, 2, 'apple', 3, 4, 'orange')
y = []
for i in x:
    if type(i) == int:
        y.append(i)
print(y)

# Tuple unpacking: extract tuples stored in a list
x = [(1, 2), (3, 4), (5, 6)]
list1 = []
list2 = []
for i, j in x:
    list1.append(i)
    list2.append(j)
print(list1)
print(list2)

# Python dictionary
x = {"apple": 2.50, "orange": 4.99, "banana": 0.59}

# Access all the keys in a dictionary
for i in x.keys():
    print(i)

# Access all the values in a dictionary
for i in x.values():
    print(i)

# Access both the keys and the values together from a dictionary
for i, j in x.items():
    print('Key: ', i)
    print(f'Value: {j}')

# Find an average of all values in a dictionary
val = []
for i in x.values():
    val.append(i)
    aver = sum(val) / len(val)
print(aver)

# Updating values: reduce all values by 25%
# (in a practical application it would be like giving a 25% discount on all fruits)
for i, j in x.items():
    print('Key: ', i)
    print(f'Value: {j - (j * 0.25)}')

#