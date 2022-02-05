"""
Working of open() function
Before performing any operation on the file like read or write, first we have to open that file.
For this, we should use Python’s inbuilt function open()
But at the time of opening, we have to specify the mode, which represents the purpose of the opening file.

Syntax:
f = open(filename, mode)

Where the following mode is supported:

r: open an existing file for a read operation.
w: open an existing file for a write operation. If the file already contains some data then it will be overridden.
a:  open an existing file for append operation. It won’t override existing data.
r+:  To read and write data into the file. The previous data in the file will not be deleted.
w+: To write and read data. It will override existing data.
a+: To append and read data from the file. It won’t override existing data.
"""
# a file named "hello", will be opened with the reading mode.
file = open('hello.txt', 'r')
# This will print every line one by one in the file
for each in file:
    print(each)

"""
read() mode:
There is more than one way to read a file in Python. 
If you need to extract a string that contains all characters in the file then we can use file.read().
"""

file1 = open('zdjongoproject.txt', 'r')
print(file1.read())

# Python code to illustrate with()
with open("hello.txt") as file:
    data = file.read()

    print(data)

# Python code to illustrate split() function
with open("hello.txt", "r") as file:
    data1 = file.readlines()
    for line in data:
        word = line.split()
        print(word)

with open("hello.txt", "r") as file:
    data1 = file.readlines()
# other directory file read
file2 = open(r"C:\Users\Ironm\Desktop\django.txt", "r+")
print(file2.read())
