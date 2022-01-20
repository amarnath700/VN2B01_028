"""
Python Inheritance allows us to define a class that inherits all the methods and properties from another class.
Parent class is the class being inherited from, also called base class.
Child class is the class that inherits from another class, also called derived class.
Create a Parent Class:
Any class can be a parent class, so the syntax is the same as creating any other class
"""


class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)


# Use the Person class to create an object, and then execute the printname method:

x = Person("John", "Doe")
x.printname()
"""
Create a Child Class
To create a class that inherits the functionality from another class, 
send the parent class as a parameter when creating the child class
"""


class Student(Person):
    pass


"""
Types Of Inheritance
In Python, based upon the number of child and parent classes involved, there are five types of inheritance. 
The type of inheritance are listed below:

Single inheritance
Multiple Inheritance
Multilevel inheritance
Hierarchical Inheritance
Hybrid Inheritance

"""
"""
single inheritance:
A child class inherits from a single-parent class.
single inheritance allows only one base class and one derived class.
by the using of derived calls object we access base class also.
syntax:
class Bass_class:
    statements
    +
    +
    statements n
    
class Derived_class(Base_class):
    statements
    
derived class object = derived class(arguments)
derived class object.base class method()


"""


# example
class Baseclass:

    def bdisplay(self):
        print("Base class")


class Derivedclass(Baseclass):

    def ddisplay(self):
        print("Derived class")


dobject = Derivedclass()
dobject.ddisplay()
dobject.bdisplay()
"""
Multilevel inheritance:

In multilevel inheritance, a class inherits from a child class or derived class. Suppose three classes A, B, C. 
A is the superclass, B is the child class of A, C is the child class of B. In other words, 
we can say a chain of classes is called multilevel inheritance.
                        Super class
                            |
                            |
                        Class(Super class)
                            |
                        n-1 class(n-2 class)
                            |
                            |
                        Derived class(n-1 class)
                        
                        Derived_object = derived class() 




"""


class A:
    def adisplay(self):
        print("Super class")


class B(A):
    def bdisplay(self):
        print("Base class")


class C(B):
    def cdisplay(self):
        print("Derived class")


print("******* Derived class *******")

c_object = C()
c_object.cdisplay()
c_object.bdisplay()
c_object.adisplay()

print("******* BASE CLASS *******")

b_object = B()
b_object.bdisplay()
b_object.adisplay()

print("******* SUPER CLASS *******")

a_object = A()
a_object.adisplay()


"""
Hierarchical Inheritance:

In Hierarchical inheritance, more than one child class is derived from a single parent class. 
In other words, we can say one parent class and multiple child classes.


"""
