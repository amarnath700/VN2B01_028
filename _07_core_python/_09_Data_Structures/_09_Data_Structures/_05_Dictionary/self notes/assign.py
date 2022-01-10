"""
Create Nested Dictionary using given List
Input : test_dict = {‘Gfg’ : 4, ‘best’ : 9}, test_list = [8, 2]
Output : {8: {‘Gfg’: 4}, 2: {‘best’: 9}}
"""
test_dict = {'Gfg': 4, 'is': 5, 'best': 9}
test_list = [8, 3, 2]

# printing original dictionary and list
print("The original dictionary is : " + str(test_dict))
print("The original list is : " + str(test_list))

# using zip() and loop to perform
# combining and assignment respectively.
res = {}
for key, ele in zip(test_list, test_dict.items()):
    res[key] = dict([ele])

# printing result
print("The mapped dictionary : " + str(res))

li = ["name", "age", "location"]
di = {"name": "amar", "sal": 25000}

for li in di.keys():
    if li == di.keys:
        print("output:", di)
