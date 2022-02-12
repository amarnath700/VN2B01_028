"""
A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern.
RegEx can be used to check if a string contains the specified search pattern.

RegEx Module:
Python has a built-in package called re, which can be used to work with Regular Expressions.
Import the re module

"""
import re

x = "HI I AM AMARNATH REDDY"
y = re.search("^HI.*REDDY$", x)
z = re.search("^hi.*reddy$", x)
print(y)

if y:
    print("YES! We have a match!")
else:
    print("No match")

if z:
    print("YES! We have a match!")
else:
    print("No match")

"""
RegEx Functions
The re module offers a set of functions that allows us to search a string for a match:

Function	Description
findall =	Returns a list containing all matches
search	=   Returns a Match object if there is a match anywhere in the string
split	=   Returns a list where the string has been split at each match
sub	    =   Replaces one or many matches with a string
"""
"""
Metacharacters
Metacharacters are characters with a special meaning:

Character	Description	Example	Try it
[]	= A set of characters	=           "[a-m]"	
\	= Signals a special sequence (can also be used to escape special characters) =	"\d"	
.	= Any character (except newline character) =	"he..o"	
^	= Starts with =             	"^hello"	
$	= Ends with	=                    "planet$"	
*	= Zero or more occurrences =	"he.*o"	
+	= One or more occurrences = 	"he.+o"	
?	= Zero or one occurrences =      "he.?o"	
{}	= Exactly the specified number of occurrences =	"he{2}o"	
|	= Either or	"falls|stays"	
()	= Capture and group	 	



Special Sequences
A special sequence is a \ followed by one of the characters in the list below, and has a special meaning:

Character	Description	Example	Try it
\A	= Returns a match if the specified characters are at the beginning of the string	"\AThe"	
\b	= Returns a match where the specified characters are at the beginning or at the end of a word
(the "r" in the beginning is making sure that the string is being treated as a "raw string")	r"\bain"
r"ain\b"	
\B	= Returns a match where the specified characters are present, but NOT at the beginning (or at the end) of a word
(the "r" in the beginning is making sure that the string is being treated as a "raw string")	r"\Bain"
r"ain\B"	
\d	= Returns a match where the string contains digits (numbers from 0-9) =	"\d"	
\D	= Returns a match where the string DOES NOT contain digits =	"\D"	
\s	= Returns a match where the string contains a white space character =	"\s"	
\S	= Returns a match where the string DOES NOT contain a white space character =	"\S"	
\w	= Returns a match where the string contains any word characters (characters from a to Z, 
digits from 0-9, and the underscore _ character) =	"\w"	
\W	= Returns a match where the string DOES NOT contain any word characters =	"\W"	
\Z	= Returns a match if the specified characters are at the end of the string =	"Spain\Z"	
Sets
A set is a set of characters inside a pair of square brackets [] with a special meaning:

Set	Description	Try it
[arn]=	Returns a match where one of the specified characters (a, r, or n) are present	
[a-n]=	Returns a match for any lower case character, alphabetically between a and n	
[^arn]=	Returns a match for any character EXCEPT a, r, and n	
[0123]=	Returns a match where any of the specified digits (0, 1, 2, or 3) are present	
[0-9]=	Returns a match for any digit between 0 and 9	
[0-5][0-9]=	Returns a match for any two-digit numbers from 00 and 59	
[a-zA-Z]=	Returns a match for any character alphabetically between a and z, lower case OR upper case	
[+]	In sets, +, *, ., |, (), $,{} has no special meaning, so [+] means: 
return a match for any + character in the string 


The findall() Function
The findall() function returns a list containing all matches.
"""
y = re.findall("[A-D]", x)
print(y)

y = re.findall("[A-Z]", x)
print(y)

# finding word
y = re.findall("NA", x)
print("Uppercase Letter finding:", y)

y = re.findall("th", x)
print("Small letter i finding:", y)

x = "i have 25 rupees"
y = re.findall("\d", x)  # \d find all numbers
print("find numbers:", y)

y = re.findall("r.p.e.", x)  # . Any character
print("Find any character", y)

y = re.findall("r.*s", x)  # '*': '0' or more occurrence
print("zero or more occurrence", y)

y = re.findall("r.+s", x)  # '+': '1' or more occurrence
print("one or more occurrence", y)

y = re.findall("rupee.+s", x)  # '+': '1' or more occurrence
print("one or more occurrence", y)
# no missing characters


y = re.findall("r.?s", x)  # '?': '1' or '0' occurrence
print("zero or one occurrence", y)
# because here 4 missing

y = re.findall("rupe.?s", x)  # '?': '1' or '0' occurrence
print("one or zero occurrence", y)

y = re.findall("r.{4}s", x)  # { }exact occurrence
print("exact occurrence", y)

y = re.findall("r.{3}s", x)  # { }exact occurrence
print("exact occurrence", y)
# here 4 missing I have given 2

y = re.findall("\Ai", x)  # \A Returns a match if the specified characters are at the beginning of the string
print("Begining string", y)

y = re.findall("\d", x)  # \d if string contain digits
print("string contain digits", y)

y = re.findall("\D", x)  # \D if string  not contain digits
print("except digits", y)

y = re.findall("\w", x)  # \w if string contain any character
print(" any character", y)

y = re.findall("\W", x)  # \W if string contain any character
print(" only space", y)


# email id
x = input("enter email id:")
y = re.findall("[a-z@.0-9]", x)
if y:
    print("Email id:", x)
else:
    print("invalid email:", x)

"""
The search() Function
The search() function searches the string for a match, and returns a Match object if there is a match.
If there is more than one match, only the first occurrence of the match will be returned
"""
x = "hii am Amarnath"
y = re.search("\s", x)
print(y.end())


