def n_table(i):
    if i == 2:
        return str(2 * i)
    else:
        print("wrong value")


def n_table1(i):
    for x in range(1, 11):
        return str(i * x)


def pattern(i=5, j=0):
    while i >= 1:
        a = " " * j + "*" * i + " " * j
        print(a)
        i = i - 2
        j = j + 1
        return a
