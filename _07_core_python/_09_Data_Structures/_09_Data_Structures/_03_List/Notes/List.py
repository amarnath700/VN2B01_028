"""
LIST:
Lists are used to store multiple items in a single variable.
Lists are created using square brackets "[]".
list is mutable.
list allows duplicate values.
list can store different type of datatypes.

"""
x = [10, 20.5, "amar", [30, "nath"], {40, "siva"}, (50, 0.6), 'a']
print(x)
print(id(x))

print("------index------")
print(x[3])
print(x[4])
print(id(x[4]))
print(x[5][0])
print(id(x[5][0]))

print("****** slicing ******")
print(x[2:6])
print(x[4:])
print(x[-5:-2])

print("***** ADD ITEMS *****")

print("       *****     append     *****        ")
print(x)
x.append("rama")  # append() method used only adding 1 item in to list.
x.append(["viveka", "mani", 50, 30.6])  # by using append  we add any value or data structure
print(x)
x.append([20, 30])
print(x)

print("   *****       insert     *****      ")
print(x)
x.insert(1, "hi")  # by using insert
print(x)
x.insert(4, ["how", "are", "you"])
print(x)
x.insert(2, {3.2, 4.6})
print(x)

print("*****  extend  *****")
print(x)
x.extend([50, [60, 90]])  # extend, add more value  with one push
print(x)
x.extend([10, [30.6, "hmm"], {5, 8}])
print(x)

print("***** Delete- pop(index),remove(value) ******")
print(x)
x.pop(5)  # by using pop, we delete the value with the help of  index
print(x)
x.pop()  # if we give empty last value is delete
print(x)

print("***** remove *****")
print(x)
x.remove(50)  # if we know the value then we use remove() for delete.
# if duplicate value is list only fist value is delete
print(x)

y = [1, 1, 1, 2, 3, 1, 3, 5, 6]
y.remove(1)
print(y)

print("*****  count(object)  *****")
print(y.count(1))  # count is used to find how many same value in list
print(y.count(5))

print("***** Reverse *****")
print(x)
x.reverse()
print(x)

print("***** sort *****")
print(y)
y.sort()
print(y)
z = [10, 20, 30, [10, 20, 30]]
print(z)
#  z.sort()  # not work in if list is having sub-list
#  print(z)
z = ["am", "Am", "aM", "AA"]
print(z)
z.sort()  # ascending order
print(z)
z.sort(reverse=True)  # descending order
print(z)

print("*****  copy  *****")
x = [1, 2, 3, [2, 5, 6]]
print(x)
x1 = x.copy()
print(x1)

x.append(10)
print(x)
print(x1)

x1 = x  # if we do modification anyone lists.after also both x1, x list are same.
print(x)
print(x1)

x.insert(2, [10, 50])
print(x)
print(x1)

print("******   join   ******")
a = [10, 20, 30]
b = [50, 60, 70]
print(a + b)
print(a*3)
print(a+b)

print("****** membership *****")
print(20 in a)
print(50 in a)
print(50 in a+b)

print("***** minimum value in list *****")
print(min(a))
print(min(b))







