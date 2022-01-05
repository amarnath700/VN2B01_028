"""Print the following patterns using loop :
a.
*
**
***
****
b.
  *
 ***
*****
 ***
  *
c.
1010101
 10101
  101
   1
   """
n = int(input("enter count"))
i =0
while i <= n:
    print("*" * i)
    i += 1

#  b
i = 1
j = 2
while i >= 1:
    a = " "*j + "*"*i + " "*j
    print(a)
    i = i + 2
    j = j - 1
    if i > 5:
        break
i = 3
j = 1
while i >= 1:
    a = " "*j + "*"*i + " "*j
    print(a)
    i = i - 2
    j = j + 1

#  c
"""
1010101
 10101
  101
   1
   """
i = 3
j = 3
while i >= 0:
    a = " " * j + "10" * i + "1"
    print(a)
    i = i - 1
    j = j + 1