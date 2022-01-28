# Count characters in string for Super deluxe
'''
CRUD : Retrieve
Data type : String
state : string : super deluxe
behaviour : for loop

# mathematical approach
1.super deluxe
2.search each character
3.initialize the counter
4.count any character occurs again increment should be 0 to 1

'''
print("_____2. using Builtin functions approach____")
s = "super deluxe  "
print("count of e characters :", s.count("e", 0, len(s)))
print("count of s characters :", s.count("s", 0, len(s)))
print("count of u characters :", s.count("u"))

print("____3.using algorithm approach____")
s = "super deluxe"
i = 0
for var in s:
    if i == "u":
        i += 1
    print("number of u characters :", s.count("u"))

print("___4.using functions approach____")
str = input("enter the string:")


def count():
    result = str.count()
    return result


print("count of a and e in str:", str.count("a", 0, len(str)), str.count("e", 0, len(str)))
print("____5.using opps approach____")


class Count:
    def __init__(self, str):
        self.str = str

    def get_str(self):
        print("input string:", self.str)

    def get_count(self):
        print("number of a characters in string:", str.count("a", 0, len(str)))


mani = Count("welcome obama")
mani.get_str()
mani.get_count()