#  simple string program
x = "hi, i am amarnath"
print(x)

print("letter by using index.")
print(x[9])

print("*****slicing value****")
print(x[3:13])
print(x[:13])
print(x[-12:-1])
print(x[-12:])

print("*****String methods*****")
x = " HI THIS IS MY LAPTOP "
print(x.capitalize())  # Converts the first character to upper case
print(x)
print(x.casefold())  # Converts string into lower case
print(x.center(60, '@'))  # Returns a centered string
print(x.count('I'))  # Returns the number of times a specified value occurs in a string
print(x.encode())  # Returns an encoded version of the string
print(x.endswith('P'))  # Returns true if the string ends with the specified value
print(x.endswith('p'))
print(x.find('A'))  # returns the index value
print(x.islower())  # islower is checked given character all leters in lowercase.if all are lower case print "True".if
# anyone letters upper case in string print "false".
print(x.isupper())  # opposite to islower.
print(x.istitle())  # every word start with capital letter.remaining letter must be small.
a = "am\tar\tnath"
print(a.expandtabs(2))  # Sets the tab size of the string
print(len(x))  # return length of list.
print(x.lower())  # convert all word into lower case.
print(a.upper())  # convert all word into upper case.
print(" ".join(x))
print(a.ljust(20), "Lenovo")  # create space b/w fist value and second value
print(x.maketrans("H", "F"))
y = x.maketrans("A", "a")
print(x.translate(y))
print(x)
print(x.partition("MY"))
print(x.replace("MY", "OUR"))

