
# P01. REQ : Find length of given string   ie., "Mani kanta"

'''topics:
CRUD : Retrieve
DAtA type: String
state:str = Mani kanta
Behaviour: += for loop

Mathematical approach
step1 : hello world
step 2 : count each element
step 3 : initialize the counter to 0
step 4: increment should be added 0 to 1

'''
# Built in function approach
x = input("Enter the string :")
print(len(x))

# algorithm approach
print("___using algorithm approach___")
str = input("enter the string : ")
count = 0
for var in str:
    count += 1
    print("length of the string", count)

print("-------3. With functions-------")

# 1. STATE
str1 = input("Enter the string:")
# 2. BEHAVIOR


def find_length(in_str=None):
    le = 0
    for char in in_str:
        le += 1
    return le


print("Length of string : ", find_length(str1))   # 1. single time usage  print(10)

res = find_length(str1)                     # 2. multiple places    x = 10 print(x)
print("Length of string : ", res)
# using oops (object oriented programming system)
print("_____using oops___")
str = input("Enter the string:")


class Length:

    def __init__(self, str):
        self.str = str

    def myfunc(self):
        print("length of the string:", self.str)


l1 = Length(len(str))
l1.myfunc()
