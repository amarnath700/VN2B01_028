"""
Dictionary:
Dictionaries are used to store data values in key:value pairs.
A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
Dictionary are mutable. But, keys are immutable. Keys are unique.
Dictionaries are written with curly brackets, and have keys and values
dict = {key1:value1,key2:value2,----------,key n:value n}



"""
x = {'eid': "vn2b01_028", 'name': "AMARNATH REDDY", 'age': 29, 'sal': 25000}
print("Dict list:", x, type(x), id(x))
print(x.keys())
print(x.values())

# keys
y = {'a': 2, 'b': 5, 'c': "siva", 'a': 3}  # here only one a value is print.first a value is deleted. 2nd value.
# in dict list 'a' = 2,'a' =3 .output is 'a' = 3
print(y)

y = {'a': 20, 'a': 60, 'a': 90, 'a': 10, 'a': 40}
print(y)

y = {'a': 2, 'b': 5, 'c': "siva", 'a': 2}  # duplicate value are not display
print(y)

y = {'a': 2, 'b': 5, 'c': "siva", 'd': 2}
print(y)

# index
print("*****  INDEX  *****")
print(x['age'], type(x['age']), id(x['age']))
print(x['name'], type(x['name']), id(x['name']))

print(x.items())
print(x.get('eid'))
print(x.get('sal'))

# length
print(len(x))

# loop ,print keys
for i in x.keys():
    print(i)

# loop , print values
for i in x.values():
    print(i)

# Membership
print("***** Membership  *****")
if "AMARNATH REDDY" in x.values():
    print(x["name"])

# add items
print("*****  Add items *****")
x["location"] = "Anantapur"
print(x)
x["state"] = "A.P"
print(x)

# update items
print("*****  Update *****")
x.update({"name": "viveka"})
print(x)
x.update({"age": 27})
print(x)

# Remove
print("****  pop()  ****")
x.pop("age")  # selected item is delete
print(x)
x.popitem()  # last item is delete
print(x)

print("*****  Delete  *****")
del x["sal"]  # selected item is delete
print(x)
del x["eid"]
print(x)

print("***** Clear()  *****")
x.clear()  # clear the all data in dict
print(x)

# copying
print("***** Copy() *****")
x = {'a': 2, 'b': 5, 'c': "siva", 'd': 2}
x1 = x.copy()
print(x)
print(x1)

x["price"] = 250
print(x)
print(x1)

x2 = dict(x)
print(x)
print(x2)

x["name"] = "ravi"
print(x)
print(x2)

"""
Nested Dictionaries
A dictionary can contain dictionaries, this is called nested dictionaries.


"""
friends = {
    "f1": {"name": "hari", "age": 30}, "f2": {"name": "vinny", "age": 31}, "f3": {"name": "siva", "age": 29}
}

print(friends)
friends["f1"]["location"] = "kadapa"  # added key pair to f1 dict
print(friends)

del friends["f2"]["age"]
print(friends)

x = friends.get("f3")
print(x)
