"""
It is used to restrict access to methods and variables.
In encapsulation, code and data are wrapped together within a single unit from being modified by accident.

A class is an example of encapsulation. A class bundles data and methods into a single unit.
And a class provides the access to its attributes via methods.
The idea of information hiding is that if you have an attribute that isn’t visible to the outside,
you can control the access to its value to make sure your object is always has a valid state.
"""


class SuperClass:
    def __init__(self, i, j, k):  # user constructor
        self.__i = i  # private attribute
        self._j = j  # protected attribute
        self.k = k  # public attribute

    def top_bottom(self):
        print("Body parts :", self._j, self.k, self.__i)


class BaseClass(SuperClass):
    def top(self):
        print("Body parts :", self._j, self.k, "self.__i")


class DerivedClass(BaseClass):
    def bottom(self):
        print("Body parts :", self._j, self.k)


i = "head"
j = "stomach"
k = "legs"
d = DerivedClass(i, j, k)
print("***** using derived class object *****")
d.bottom()
d.top_bottom()

b = BaseClass(i, j, k)
print("***** using Base class object")
b.top_bottom()
b.top()
# b.bottom()
print("***** using Superclass object *****")
s = SuperClass(i, j, k)
b.top_bottom()
