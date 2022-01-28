"""
Abstraction:
A class that consists of one or more abstract method is called the abstract class.
Abstract methods do not contain their implementation.
Abstract class can be inherited by the subclass and abstract method gets its definition in the subclass.
Abstraction classes are meant to be the blueprint of the other class.
An abstract class can be useful when we are designing large functions.
An abstract class is also helpful to provide the standard interface for different implementations of components.
Python provides the abc module to use the abstraction in the Python program.

Syntax

from abc import ABC
class ClassName(ABC):

Points to Remember
Below are the points which we should remember about the abstract base class in Python.

An Abstract class can contain the both method normal and abstract method.
An Abstract cannot be instantiated; we cannot create objects for the abstract class.
"""
from abc import ABC, abstractmethod


class Office(ABC):
    @abstractmethod
    def salary(self):
        None


class Uday(Office):
    def salary(self):
        print("Uday Salary:", 25200)


class Vivek(Office):
    def salary(self):
        print("Viveka Salary:", 50250)
        print("Good employee")


class Siva(Office):
    def salary(self):
        print("Siva Salary:", 20000)
        if x <= 10:
            print("x is less than or equal to 10")
        else:
            print("x is greater than 10")


x = int(input("enter 10 value:"))
v = Vivek()
v.salary()

s = Siva()
s.salary()

#o = Office()
#o.salary()

# program of laptop
from abc import ABC, abstractmethod


class Laptop(ABC):
    @abstractmethod
    def brand(self):
        None


class Lenovo(Laptop):
    def brand(self):
        if z == "lenovo":
            print("Laptop is lenovo brand")
        else:
            print("Laptop is not lenovo")


class Hp(Laptop):
    def brand(self):
        if z == "hp":
            print("Laptop is HP brand")
        else:
            print("Laptop is not HP")


class Dell(Laptop):
    def brand(self):
        if z == "dell":
            print("Laptop is Dell brand")
        else:
            print("Laptop is not Dell")


print("type selected Brands only Lenovo or Dell or HP")
y = input("enter laptop brand: ")

z = y.lower()

l = Lenovo()
l.brand()


d = Dell()
d.brand()

h = Hp()
h.brand()
