"""
Creating a file using write() mode
Let’s see how to create a file and how write mode works:
To manipulate the file, write the following in your Python environment:


"""
# Python code to create a file
file = open('hello.txt', 'w')
file.write("i am Amarnath Reddy \n")
file.write("my native is Tadipatri")
file.close()


with open("hello.txt", "w") as f:
    f.write("Hello World!!!")
f.close()


