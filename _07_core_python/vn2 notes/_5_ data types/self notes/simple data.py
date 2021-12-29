"""
int = 10,20,30
float = 10.9, 20.8
complex = 10j
"""

x = 5  # integer
y = 30.5  # float
z = 20j  # complex

print(x, type(x))
print(y, type(y))
print(z, type(z))

# casting

x = float(x)
y = complex(y)
z = str(z)

print(x, type(x))
print(y, type(y))
print(z, type(z))

x = "Amarnath"  # string
print(x, type(x))
print(x[4])  # indexing
print(x[:8])  # slicing

x = [1, 5.5, 6, 1j, "Amar", ["a", 7, 8.5]]
print(x, type(x))
print(x[4])  # indexing
print(x[:4])  # slicing
print(x[5][2])

x = tuple(x)  # conversion
print(x, type(x))
print(x[1])  # indexing
print(x[:5])  # slicing
print(x[5][0])

x = [1, 5.5, 6, 1j, "Amar", "a", 7, 8.5]
x = set(x)  # conversion
print(x, type(x))
# print(x[1])  # indexing
# print(x[:5])  # slicing

x = {'m': 30, 'name': "amar"}
print(x, type(x))
print(x['m'])

X = {10, 15, 3, 2}
print(x, type(x))

x = [10, 20, 30, 10, 20, 30, 10, 20, 30]
x = list(set(list(x)))
print(x)