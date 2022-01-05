"""
write a program to display sum of odd no. and even no. b/w 12 to 37.
"""
s = 0
s1 = 0
for x in range(12, 37+1):
    if x % 2 == 0:
        s = s + x
    else:
        s1 = s1 + x

print(s)
print(s1)

print("------while------")
s = 0
s1 = 0
i = 12
while i <= 37:
    if i % 2 == 0:
        s = s + i
    else:
        s1 = s1 + i
    i += 1
print(s)
print(s1)

