"""
Comprehensions in Python

Comprehensions in Python provide us with a short and concise way to construct
new sequences (such as lists, set, dictionary etc.) using sequences which have been already defined.
Python supports the following 4 types of comprehensions:
List Comprehensions
Dictionary Comprehensions
Set Comprehensions
Generator Comprehensions
"""
"""
List Comprehensions:

List Comprehensions:
List Comprehensions provide an elegant way to create new lists. 
The following is the basic structure of a list comprehension:

output_list = [output_exp for var in input_list if (var satisfies this condition)]

Note that list comprehension may or may not contain an if condition. 
List comprehensions can contain multiple for (nested list comprehensions).
"""
# normal code for list
lst = [1, 2, 3, 4, 5, 6]
lst2 = []
j = 0
for i in lst:
    lst2.append(i * 5)

print("lst2 values", lst2)

# using list compensation
lst3 = [i * 5 for i in lst]

print("lst3 values", lst3)

"""
Dictionary Comprehensions:
Extending the idea of list comprehensions, we can also create a dictionary using dictionary comprehensions. 
The basic structure of a dictionary comprehension looks like below.

output_dict = {key:value for (key, value) in iterable if (key, value satisfy this condition)}
"""
lst = [1, 2, 3, 4, 5, 6]
dit = {}
for i in lst:
    dit[i] = i / 2

print("dit output:", dit)

# using compens

dit1 = {i: i / 2 for i in lst}
print("dit output:", dit1)

# program

name = ['Amar', 'Viveka', 'Rajini']
age = [29, 40, 30]

dit2 = {}

# Using loop for constructing output dictionary
for (i, j) in zip(name, age):
    dit2[i] = j

print("Output Dictionary using for loop:",
      dit2)

dit3 = {x: y for x, y in zip(name, age)}

print("Output Dictionary using for Compensation:",
      dit3)

"""
Set Comprehensions:
Set comprehensions are pretty similar to list comprehensions. 
The only difference between them is that set comprehensions use curly brackets { }
"""
lst4 = [1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 7]

set1 = set()

# Using loop for constructing output set
for i in lst4:
    set1.add(i)

print("Output Set using for loop:", set1)

# using Set comp
set2 = {i for i in lst4}

print("Output Set using for loop:", set2)