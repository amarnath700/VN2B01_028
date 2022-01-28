# P02: Count characters in string
'''topics:
CRUD : Retrieve
DAtA type: String
state:str = user value
Behaviour: += for loop

Mathematical approach
step1 : hello world
step 2 : count each element
step 3 : initialize the counter to 0
step 4: count should be added 0 to 1

'''
print("_____2. using Builtin functions approach____")
s = input("enter string:")
print("count of e characters :", s.count("a", 0, len(s)))
print("count of s characters :", s.count("r", 0, len(s)))
print("count of u characters :", s.count("t"))

print("____3.using algorithm approach____")
s = input("enter string:")
i = 0
for var in s:
    if i == "a":
        i += 1
print("number of u characters :", s.count("n"))

print("___4.using functions approach____")
str = input("enter string:")


def count():
    result = str.count()
    return result


print("count of a and e in str:", str.count("a", 0, len(str)), str.count("h", 0, len(str)))
print("____5.using opps approach____")


class Count:
    def __init__(self, str):
        self.str = str

    def get_str(self):
        print("input string:", self.str)

    def get_count(self):
        print("number of a characters in string:", str.count("a", 0, len(str)))


str = input("enter string:")
s = Count(str)
s.get_str()
s.get_count()
