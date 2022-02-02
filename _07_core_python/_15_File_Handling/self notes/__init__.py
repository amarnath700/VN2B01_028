L = ["i Using"," ", "Lenovo", " ", "Laptop"]
with open(r"C:\Users\Ironm\Desktop\all_in_1.txt", "w") as file3:
    file3.write(" present i working im Maple Labs pvt ltd \n")
    file3.writelines(L)
    file3.close()  # to change file access modes

with open(r"C:\Users\Ironm\Desktop\all_in_1.txt", "r+") as file3:
    print("file3 output", file3.read())
    file3.write(" \n present i working im 'R+' pvt ltd \n")
    # Reading form a file
    print("file3 output", file3.read())
