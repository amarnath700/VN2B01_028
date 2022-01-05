i = 100
while i <= 500:
    if i % 2 != 0:
        if i % 11 == 0:
            print(i)
    i = i + 1

for x in range(100, 500, 1):
    if x % 2 != 0 and x % 11 == 0:
        print(x)