"""
Working of append() mode
Let’s see how the append mode works:
"""
# Python code to illustrate append() mode
file = open('hello.txt', 'a')
file.write("Regarding my work profile i am having a total of 4 yr experience in Python development")
file.close()

"""
There are also various other commands in file handling that is used to handle various tasks like: 

rstrip(): This function strips each line of a file off spaces from the right-hand side.
lstrip(): This function strips each line of a file off spaces from the left-hand side.
It is designed to provide much cleaner syntax and exception handling when you are working with code. 
That explains why it’s good practice to use them with a statement where applicable. 
This is helpful because using this method any files opened will be closed automatically after one is done, 
so auto-cleanup. 
Example: 
"""
# Python code to illustrate with()
with open("file.txt") as file:
    data = file.read()

