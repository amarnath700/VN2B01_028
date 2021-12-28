"""
Strings:
Strings in python are surrounded by either single quotation marks, or double quotation marks.
'hello' is the same as "hello".

Multiline Strings
You can assign a multiline string to a variable by using three  double quotes Or three single quotes.
"""
x = """
Twinkle twinkle little star.
How I wonder what you are.
Up above the world so high.
Like a diamond in the sky.
Twinkle twinkle little star.
How I wonder what you are."""
print(x)

"""
Strings are Arrays:
Like many other popular programming languages, strings in Python are arrays of bytes representing unicode characters.
However, Python does not have a character data type, a single character is simply a string with a length of 1.
Square brackets can be used to access elements of the string."""

x = "Amarnath Reddy"
print(x[5])
print(x[-5])

''' 
String Length:
To get the length of a string, use the len() function.
'''
print(len(x))

"""
Check String:
To check if a certain phrase or character is present in a string, we can use the keyword in.
"""
x = """hi i am Amarnath Reddy from Andhra pradesh"""
print("Reddy" in x)
print("Rao" in x)