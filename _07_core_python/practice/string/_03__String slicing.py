# P01. REQ : Find length of given string
'''topics:
CRUD : Retrieve
DAtA type: String
state:str = user value
Behaviour: += for loop

Mathematical approach
step1 : hello world
step 2 : count each element
step 3 : initialize the counter to 0
step 4: increment should be added 0 to 1

'''
# Built-in function approach
"""print("_____3. using Builtin functions approach____")
str = input("enter string:")
print("string slicing:", str[1:5])

# algorithm approach
print("____3.using algorithm approach____")
str = input("enter string:")
i = int(input("enter start slicing number:"))
j = int(input("enter start slicing number:"))
for x in range(i,j):
    break

print("Slicing value:", str[i:j])


print("___4.using functions approach____")
str = input("enter string:")
i = int(input("enter start slicing number:"))
j = int(input("enter start slicing number:"))


def slice(i, j):
    return i, j


print("Slicing value:", str[i:j])
"""
print("____5.using opps approach____")


class Slice:
    def __init__(self, str, i, j):
        self.str = str
        self.i = i
        self.j = j

    def st(self):
        print("string name:", self.str)
        print("slicing value:", self.str[self.i:self.j])


str = input("enter string:")
i = int(input("enter start slicing number:"))
j = int(input("enter start slicing number:"))
s = Slice(str, i, j)
s.st()