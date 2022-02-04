"""
Iteration:
A process that is repeated more than one time by applying the same logic is called an Iteration.
 a loop is created with few conditions to perform iteration till it exceeds the limit.
 If the loop is executed 6 times continuously, then we could say the particular block has iterated 6 times.
"""
lst = [1, 2, 3, 4, 5]
for i in lst:
    if i % 2 == 0:
        print(str(i) + "even number")
    else:
        print(str(i) + "odd number")

# total loop is five time executed ,above block is iterated 5 times.


"""
Iterators
An iterator is an object that contains a countable number of values.
An iterator is an object that can be iterated upon, meaning that you can traverse through all the values.
it is used to iterate over iterable objects like list, tuples, sets, etc. 
Iterators are implemented using a class and a local variable for iterating is not required here, 
It follows lazy evaluation where the evaluation of the expression will be on hold and stored in the memory 
until the item is called specifically which helps us to avoid repeated evaluation. 
As lazy evaluation is implemented, it requires only 1 memory location to process the value 
and when we are using a large dataset then, wastage of RAM space will be reduced 
the need to load the entire dataset at the same time will not be there.

Using an iterator-

iter() keyword is used to create an iterator containing an iterable object.
next() keyword is used to call the next element in the iterable object.
After the iterable object is completed, to use them again reassign them to the same object.
Technically, in Python, an iterator is an object which implements the iterator protocol, 
which consist of the methods __iter__() and __next__().
"""

s = {1, 2, 3, 4, 5}
it = iter(s)
print(it)

print(next(it))


# createing an iterator
# to create iterator, we need implementation methods,__iter__,__next__
class Add:
    def __iter__(self):
        self.i = 10
        return self

    def __next__(self):
        j = self.i
        self.i += 5
        return j


a = Add()
iterator = iter(a)

print(next(a))
print(next(a))


