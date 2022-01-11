"""
Tuple:
Tuples are used to store multiple items in a single variable.
Tuple is one of 4 built-in data types in Python used to store collections of data, the other
3 are List, Set, and Dictionary, all with different qualities and usage.
A tuple is a collection which is ordered and unchangeable.

Tuples are written with round brackets.
Tuple items are ordered, unchangeable, and allow duplicate values.
Tuples are unchangeable, meaning that you cannot change, add, or remove items once the tuple is created.
But there are some workarounds.


Change Tuple Values:
Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.
But there is a workaround. You can convert the tuple into a list, change the list,
and convert the list back into a tuple.
"""
x = (1, 2.5, 3, 1, "Amar", "10")
print(x)
print(type(x))
print(id(x))

# index
print(x[1])
print(x[-1])

# slicing
print(x[:4])
print(x[-4:])
print(x[-4:4])

i = 0
for i in range(len(x)):
    print(x[i])
    i = i + 1

# length
print(len(x))


# by using type casting we can Add values into tuple.below are steps
# convert into list.
# add value to list.
# convert into tuple.

print("*****  Tuple value  *****")
print(x)
x = list(x)  # converting tuple to list
print("convert tuple to list:", x, type(x))
x.append([1000])  # by using append adding value into list
print("list after append", x, type(x))
x.extend([25, "nath"])  # by using extend adding value into list
print("list:", x, type(x))
x = tuple(x)  # converting list to tuple
print("tuple:", x, type(x))


x = x + x
print(x)

# x.remove(10) tuple is immutable.so, add and remove are won't work
# print(x)

# remove
print("*****  Tuple value  *****")
print(x)
x = list(x)  # converting tuple to list
print("convert tuple to list:", x, type(x))
x.remove("nath")  # by using remove value into list
print("list:", x, type(x))
x = tuple(x)  # converting list to tuple
print("tuple:", x, type(x))

# count
y = x.count(2.5)
print("count:",y)



# delete
print("*****  Tuple value  *****")
print(x)
del x


