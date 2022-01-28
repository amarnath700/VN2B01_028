"""
Map():
applies a given function to all iterable and return new list.
map() function returns a map object(which is an iterator) of the results
after applying the given function to each item of a given iterable (list, tuple etc.)


Syntax :

map(fun, iter)
"""
x = [1, 2, 3, 4, 5]


# square of list
def square(x):
    return x ** 2


y = map(square, x)
print(tuple(y))

# cube
print("*****   Lambda  map   *****")
y = set(map(lambda x: x ** 3, x))
print(y)

"""
Filter: create an output list consisting of values for which the function return true.
The filter() method filters the given sequence with the help of a function that tests each element 
in the sequence to be true or not.
Syntax:

filter(function,iteration)
"""


def greater(i):
    if i >= 2:
        return i


y = filter(greater, x)
print(y)
print(tuple(y))

# lambda
print("*****   Lambda  filter   *****")
y = set(filter(lambda i: i <= 3, x))
print(y)

"""
reduce:Applies a given function to the iterables and returns a single value. 
The reduce(fun,seq) function is used to apply a particular function passed in its argument to all of the list 
elements mentioned in the sequence passed along.This function is defined in “functools” module.

reduce(function,sequence)
"""

print("*****   User def funcion of reduce   *****")
from functools import reduce



def z(a, b):
    return a * b


y = reduce(z, x)
print(y)

print("*****   Lambda reduce   *****")
y = reduce(lambda a, b: a + b, x)
print(y)
# lambda map and filter

print("*****   Lambda map , filter   *****")

y = map(lambda x: x ** x, filter(lambda i: i >= 2, x))

print("*****   Lambda  filter,map   *****")


# using all 3 funcion in lambda

print("*****   Lambda  reduce,map,filer   *****")


y = reduce(lambda a, b: a + b, map(lambda x: x * x, filter(lambda i: i <= 3, x)))
print(y)
