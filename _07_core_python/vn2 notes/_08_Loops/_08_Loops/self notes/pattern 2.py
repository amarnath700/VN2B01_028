"""
5 5 5 5 5
4 4 4 4
3 3 3
2 2
1
"""
i = 5
while i >= 5:
    print("5"*i)
    if i >= 4:
        print("4"*(i-1))
        if i >= 3:
            print("3" * (i - 2))
            if i >= 3:
                print("2" * (i - 3))
                if i >= 2:
                    print("1" * (i - 4))

