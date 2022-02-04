file = open(r"C:\Users\Ironm\Desktop\all_in_1.txt", "w")
file.write("hi to All")  # write
file.close()

file = open(r"C:\Users\Ironm\Desktop\all_in_1.txt", "r")
print("file output", file.read())  # read
print("file1 output", file.read(4))

"""
file = open(r"C:\Users\Ironm\Desktop\all_in_1.txt", "a")
file.writelines("\n I am Amarnath reddy \n")
file.write("my native is Tadipatri")
file.close()

with open(r"C:\Users\Ironm\Desktop\all_in_1.txt") as file1:
    data = file1.readlines()
print(data)

with open(r"C:\Users\Ironm\Desktop\all_in_1.txt", "r") as file2:
    data = file2.readlines()
    for line in data:
        word = line.split()
        print(word)

L = ["i Using"," ", "Lenovo", " ", "Laptop"]
with open(r"C:\Users\Ironm\Desktop\all_in_1.txt", "w") as file3:
    file3.write("present i working im Maple Labs pvt ltd \n")
    file3.writelines(L)
    file3.close()  # to change file access modes

with open(r"C:\Users\Ironm\Desktop\all_in_1.txt", "r+") as file3:
    file3.write("present i working im 'R+' pvt ltd \n")
    # Reading form a file
    print("file3 output", file3.read())

with open(r"C:\Users\Ironm\Desktop\all_in_1.txt", "w+") as file4:
    file4.write("present i working im 'W+' pvt ltd \n")
    # Reading form a file
    print("file4 output", file4.read())

with open(r"C:\Users\Ironm\Desktop\all_in_1.txt", "a+") as file5:
    file5.write("present i working im 'A+' pvt ltd \n")
    # Reading form a file
    print("file5 output", file5.read())
    
    
file6 = open(r"C:\Users\Ironm\Desktop\all_in_1.txt", "a+")
file6.write("present i working im 'A+' pvt ltd \n")
    # Reading form a file
    print("file5 output", file6.read())

"""

