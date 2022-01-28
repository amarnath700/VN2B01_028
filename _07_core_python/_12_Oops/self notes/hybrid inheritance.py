class B1:
    def a(self):
        print("Letter Is 'A'")


class B2:
    def d(self):
        print("Letter Is 'D'")


class D1(B1):  # Single Inheritance
    def b(self):
        print("Letter Is 'B'")


class D2(B2):
    def c(self):
        print("Letter Is 'C'")


class D3(B1, B2):  # multiple inheritance
    def e(self):
        print("Letter Is 'E'")


class D4(D2):  # multiple inheritance
    def f(self):
        print("Letter Is 'F'")


class D5(B1):  # Hierarchical  Inheritance
    def g(self):
        print("Letter Is 'G'")




d3 = D3()
d2 = D2()
d1 = D1()

d3.e()
d3.a()
d3.d()
