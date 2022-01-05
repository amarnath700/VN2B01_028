"""
a.
1
1 2
1 2 3 
1 2 3 4

b.
* * * *
* * *
* *
*

"""
print("Number Pattern ")

# Decide the row count. (above pattern contains 5 rows)
row = 4
# start: 1
# stop: row+1 (range never include stop number in result)
# step: 1
# run loop 5 times
for i in range(1, row + 1, 1):
    # Run inner loop i+1 times
    for j in range(1, i + 1):
        print(j, end=' ')
    # empty line after each row
    print("")

"""
i = 4
while i >= 1:
    print("*"*i)
    i = i - 1
    """
for x in range(4, 0, -1):
    print("*" * x)
