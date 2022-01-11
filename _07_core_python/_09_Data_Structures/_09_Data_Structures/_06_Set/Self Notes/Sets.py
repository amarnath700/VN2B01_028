"""
Sets:
Set is a collection of data can store in one variable.
Set not allow Duplicate value.
Set allow Different data type. Sets are unordered so, indexing and slicing won't works.
set is mutable. we can add and delete value in set.
In set, elements are immutable.
Set written in curly Braces.

"""
print("------------- Set Values --------------")
x = {10, 20, "amar", "siva", 60, 2.5}
print(x)
print(type(x))
print(id(x))

# Membership
print("------------- Membership --------------")
for i in x:
    print(i)

# ADD arguments
print("------------- ADD Values --------------")
x.add("viveka")  # add() method is used to add arguments into list
print(x)

# x.add(60,40, 9.2) Only one argument add into set.if we add more we will get error.
print(x)
y = [1.1, 1.2, 1.3]
x.update(y)
print(x)

# Delete argument
print("------------- Delete Values --------------")
x.discard("siva")  # in sets discard() method is used for delete the arguments
print(x)
x.pop()
print(x)
x.remove(20)
print(x)


# join sets
"""

"""
x = {'a', 'b', 'c', 'd', 'e'}
y = {'f', 'g', 'h', 'c', 'e'}
print("------------- X Values --------------")
print(x)
print("------------- Y Values --------------")
print(y)

# union()
print("------------- Union Values --------------")
z = x | y  # By using symbol union() method can print all value duplicate value will delete
print(z)
a = x.union(y)  # By using union() method
print(a)


# intersection()
print("------------- intersection Values --------------")
z = x & y  # by using intersection method only print common value in both sets
print(z)
a = x.intersection(y)
print(a)


# difference()
print("------------- Difference Values --------------")
z = x - y  # by using difference we will print
print(z)
a = y.difference(x)
print(a)
z = x.symmetric_difference(y)
print(z)
x.symmetric_difference_update(y)
print(x)







