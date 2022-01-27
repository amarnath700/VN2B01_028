"""
Access Specifiers:
Various object-oriented languages like C++, Java, Python control access modifications
which are used to restrict access to the variables and methods of the class.
Most programming languages has three forms of access modifiers, which are Public, Protected and Private in a class.
Python uses ‘_’ symbol to determine the access control for a specific data member or a member function of a class.
Access specifiers in Python have an important role to play in securing data from unauthorized access
and in preventing it from being exploited.
A Class in Python has three types of access modifiers:

Public Access Modifier:
Protected Access Modifier
Private Access Modifier


Public Access Modifier:
The members of a class that are declared public are easily accessible from any part of the program. 
All data members and member functions of a class are public by default.

"""


# program to illustrate public access
class Veh:  # bass class
    def __init__(self, brand, type):  # constructor
        self.brand = brand  # public data members
        self.type = type

    def vdis(self):  # public member function
        print("veh", self.type)  # accessing public data member


class Car(Veh):  # derived class
    def display(self):  # public member function
        print("car:", self.brand)  # accessing public data member


class Bike(Veh):
    def dis(self):
        print(self.brand)


brand = "KIA"
type = "petrol"

c = Car(brand, type)
c.display()
v = Veh(brand, type)
v.vdis()
print(v.brand)  # in the program
b = Bike(brand, type)
b.dis()
"""
Protected Access Modifier:
The members of a class that are declared protected are only accessible to a class derived from it. 
Data members of a class are declared protected by adding a single underscore ‘_’ symbol 
before the data member of that class. 
"""


# program to illustrate protected access
class Veh1:  # bass class
    def __init__(self, meilage, speed):  # constructor
        self.meilage = meilage  # public data members
        self._speed = speed  # protected data member

    def vdis1(self):  # protected member function
        print("veh", self.meilage)  # accessing  data member

    @property
    def speed(self):
        return self._speed


class Car1(Veh1):  # derived class
    def __init__(self, meilage, speed):
        Veh1.__init__(self, meilage, speed)

    def display(self):  # protected member function
        print("car:", self._speed)  # accessing protected data member


class Bike1(Car1):
    def dis1(self):
        print(self._speed)


meilage = 25
speed = 120

c = Car1(meilage, speed)
c.display()
v = Veh1(meilage, speed)
v.vdis1()
print(v.speed)
print(v.meilage)
b = Bike1(meilage, speed)
b.dis1()

"""
Private Access Modifier:
The members of a class that are declared private are accessible within the class only, 
private access modifier is the most secure access modifier. 
Data members of a class are declared private by adding a double underscore ‘__’ symbol 
before the data member of that class. 
"""


class Student:
    def __init__(self, name, age):
        self.__name = name
        self._age = age

    def stu(self):
        print("student", self.__name)
        print("student", self._age)


class Child(Student):

    def chi(self):
        print("Child", self.__name)
        print("Child", self._age)


name = "Amar"
age = 30
s = Student(name, age)
s.stu()
c = Child(name, age)
c.chi()
