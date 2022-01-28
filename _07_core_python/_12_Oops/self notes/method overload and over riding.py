"""
method overriding:
    Method overriding is a concept of object-oriented programming.
It is a language feature that allows a subclass or child class to provide a specific implementation of a method
which is already provided by one of its super classes or parent classes.
"""


class Vehical:
    def __init__(self):
        self.model = "mahendra xuv"
        self.type = "diesel"

    def disv(self):
        print("vehical:", self.model)
        print("vehical:", self.type)


class Vehical1(Vehical):

    def __init__(self):
        self.model = "TATA safari"
        self.type = "petrol"

    def disv(self):

        print("vehical:", self.model)
        print("vehical:", self.type)


veh1 = Vehical1()
veh1.disv()
veh = Vehical()
veh.disv()

"""
method overloading:
    There is a concept where two or more methods can have the same name. 
But they should have different parameters, different numbers of parameters, different types of parameters, or both.     
These methods are known as overloaded methods and this feature is called method overloading. 

"""


def mul(a, b, c=50):
    return a + b + c


mul(20, 30)
mul(20, 20, 20)
print(mul(20, 30))
print(mul(20, 20, 20))
