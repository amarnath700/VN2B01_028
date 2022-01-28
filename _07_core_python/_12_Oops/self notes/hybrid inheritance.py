class B1:
    def a(self):
        print("Class Is 'A'")


class B2:
    def b(self):
        print("Class Is 'B'")


class D1(B1):  # Single Inheritance
    def d1(self):
        print("Class Is 'D1'")


class D2(B2):
    def d2(self):
        print("Class Is 'D2'")


class D3(B1, B2):  # multiple inheritance
    def d3(self):
        print("Class Is 'D3'")


class D4(D2):  # multiple inheritance
    def d4(self):
        print("Class Is 'D4'")


class D5(B1):  # Hierarchical  Inheritance
    def d5(self):
        print("Class Is 'D5'")


d5 = D5()
d4 = D4()
d3 = D3()
d2 = D2()
d1 = D1()

# Hierarchical  Inheritance
print("****** Hierarchical  Inheritance ****** ")
d5.d5()
d5.a()

d1.d1()
d1.a()

# multiple inheritance
print("****** Multiple  Inheritance ****** ")
d3.d3()
d3.b()
d3.a()

# multilevel inheritance
print("****** Multilevel  Inheritance ****** ")
d4.d4()
d4.d2()
d4.b()
d2.d2()
d2.b()