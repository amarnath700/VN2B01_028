"""
Destructor:
Destructors are called when an object gets destroyed. In Python, destructors are not needed as much as in C++ because Python has a garbage collector that handles memory management automatically.
The __del__() method is a known as a destructor method in Python. It is called when all references to the object have been deleted i.e when an object is garbage collected.
Syntax of destructor declaration :

def __del__(self):
  # body of destructor
"""
"""

class Bike:
    def __init__(self):
        print("Bike have Two wheels")

    def __del__(self):
        print("car have four wheels")

    def ty(self):
        print("Bike and car are personal vehicles")


class Vehicles(Bike):
    def ty1(self):
        print("Bus and Train are public vehicles")


v = Vehicles()
v.ty1()

v.ty()
"""

# program

class Tour:
    def __init__(self):
        print("Welcome to India")

    def __del__(self):
        print("Good bye to everyone")


class Place(Tour):
    def place(self):
        print("Mysore zoo is good place for enjoy")


class Place1:
    def place1(self):
        print("sivamogha waterfall is good place for enjoy")


p1 = Place1()
p1.place1()
p = Place()
p.place()