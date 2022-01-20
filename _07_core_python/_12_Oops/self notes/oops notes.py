"""
python supports both procedural and object-oriented programming
procedural programming  we will write code using functions
Object oriented programming - we will write code using classes and objects

OOP Concept:
OOPs - Objected oriented programming
OOPs, in Python is a programming approach that focuses on using objects and classes as same as
other general programming languages. The objects can be any real-world entities.
Python allows developers to develop applications using the OOPs approach with the major focus on code re-usability.
It is very easy to create classes and objects in Python.

There are 7 major principles in oops concepts:
1. class
2. object
3. methods
4. inheritance
   1.single
   2.multilevel
   3.hierarchical
   4.multiple
5. polymorphism
   1.compile time
   2.runtime
6.abstraction
7.encapsulation


CLASSES:

Almost everything in Python is an object, with its properties and methods.
A Class is like an object constructor, or a "blueprint" for creating objects.
class is a logical entity.
CLASS have 3 compartments
1.name
2.attributes
3.function/methods

we can't access classes directly. By using object we call the class.
syntax:

class name:
    statements 1
    *
    *
    *
    statements n
"""


class Person:
    name = "Amarnath"


"""
Object:
    An object is an instance of a class. It is a collection of attributes (variables) and methods. 
We use the object of a class to perform actions.
Every object has the following property.

Identity: Every object must be uniquely identified.
State: An object has an attribute that represents a state of an object, and it also reflects the property of an object.
Behavior: An object has methods that represent its behavior.
Now we can use the class named MyClass to create objects:

Syntax:

<object-name> = <class-name>(<arguments>)  


"""
a = Person()
print(a.name)
"""
The __init__() Function:
NOTE:The __init__() function is called automatically every time the class is being used to create a new object.
The examples above are classes and objects in their simplest form, and are not really useful in real life applications.
To understand the meaning of classes we have to understand the built-in __init__() function.
All classes have a function called __init__(), which is always executed when the class is being initiated.
Use the __init__() function to assign values to object properties, or 
other operations that are necessary to do when the object is being created:
"""


class Laptop:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def detail(self):
        print(self.brand, self.model)


l1 = Laptop("lenovo", "ideal")
l2 = Laptop("dell", "inspire")
l1.detail()
l2.detail()

"""
Python Inheritance
Inheritance allows us to define a class that inherits all the methods and properties from another class.
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
Inheritance:
    Inheritance is a feature used in object-oriented programming; 
    it refers to defining a new class with less or no modification to an existing class. 
    The new class is called derived class and from one which it inherits is called the base. 
    Python supports inheritance; it also supports multiple inheritances. 
    A class can inherit attributes and behavior methods from another class called subclass or heir class.
    
    Syntax:
        class DerivedClass(BaseClass):
            body_of_derived_class
"""
