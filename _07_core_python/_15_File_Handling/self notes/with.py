#  using with
"""
With statement:
if we use with statement,no need to close the file. Automatically with statement close the file.
"""

with open(r'C:\Users\Ironm\Desktop\all_in_1.txt', 'r') as f:
    print(f)


# with using write
with open(r'C:\Users\Ironm\Desktop\all_in_1.txt', 'a') as f:
    f.write('hi to All \n')


# with using read
with open(r'C:\Users\Ironm\Desktop\all_in_1.txt', 'r') as f:
    for line in f:
        print(f.read())

#