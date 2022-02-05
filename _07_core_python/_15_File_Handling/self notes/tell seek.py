"""
File Positions
The tell() method tells you the current position within the file;
in other words, the next read or write will occur at that many bytes from the beginning of the file.

The seek(offset[, from]) method changes the current file position.
The offset argument indicates the number of bytes to be moved.
The from argument specifies the reference position from where the bytes are to be moved.

"""

# tell method.
f = open(r'hello.txt', 'r')
f.read()
# tell method
# n = int(input("enter cursor value:"))
s = f.tell()
print(s)


# seek method.

