class Mobile:
    def __init__(self, android_ver, ram, storage, brand, price):  # constructor
        self.android_ver = android_ver
        self.storage = storage
        self.ram = ram
        self.brand = brand
        self.price = price

    def mobiledetails(self):
        print("mobile details", self.android_ver, self.ram, self.storage)


class Mobile1(Mobile):

    def brand1(self):
        print("mobile brand:", self.brand)
        print("mobile price:", self.price)
        print("android_ver:", self.android_ver)
        print("ram:", self.ram)


class Mobile2(Mobile1):

    def brand2(self):
        print("mobile brand:", self.brand)
        print("mobile price:", self.price)
        print("android_ver:", self.android_ver)
        print("ram:", self.ram)


android_ver = int(input("enter android version:"))
ram = int(input("enter mobile Ram in Gb:"))
storage = int(input("enter mobile storage in Gb:"))
brand = input("enter mobile brand:")
price = int(input("enter of mobile price:"))

m1 = Mobile1(android_ver, ram, storage, brand, price)
m1.brand1()
m1.mobiledetails()

m2 = Mobile2(android_ver, ram, storage, brand, price)
m2.brand1()
m2.brand2()
m2.mobiledetails()