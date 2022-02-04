# copy an image into new file

f1 = open('pa.JPG', 'rb')
f2 = open('new.JPG', 'wb')

# read bytes from f1 and write the bytes to f2
bytes = f1.read()
f2.write(bytes)
print("copy data to new.JPG  successfully")
f1.close()
f2.close()

# taken image from another dir and copy an image into new file

f1 = open(r'C:\Users\Ironm\Desktop\New folder\Amarnath Pan Card.JPG', 'rb')
f2 = open('new pan card.JPG', 'wb')

# read bytes from f1 and write the bytes to f2
bytes = f1.read()
f2.write(bytes)
print("copy data to new.JPG  successfully")
f1.close()
f2.close()

# taken image from another dir and copy an image format into new file

f1 = open(r'C:\Users\Ironm\Desktop\New folder\Amarnath Pan Card.JPG', 'rb')
f2 = open('new pan card.png', 'wb')

# read bytes from f1 and write the bytes to f2
bytes = f1.read()
f2.write(bytes)
print("copy data to new.JPG  successfully")
f1.close()
f2.close()