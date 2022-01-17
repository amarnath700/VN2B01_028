# Write a program to create a function that takes two arguments, name and age, and print their value.
"""def person(name, age):
    print(name, age)


person("amar", 25)




# Write a program to create function func1() to accept a variable length of arguments and print their value.
def func1(*args):
    for i in args:
        print(i)


func1(20, 40, 60)
func1(80, 100)


# Create a function with default argument
# Write a program to create a function show_employee() using the following conditions.
# It should accept the employee’s name and salary and display both.
# If the salary is missing in the function call then assign default value 9000 to salary
def show_employee(name,salary=9000):
    print(name,salary)


show_employee("amar")
show_employee("viveka",100000)
"""


# Create an inner function to calculate the addition in the following way
# Create an outer function that will accept two parameters, a and b
# Create an inner function inside an outer function that will calculate the addition of a and b
# At last, an outer function will add 5 into addition and return it
def outer(a, b):
    def addition(a, b):
        return a + b

    add = addition(a, b)
    return add + 5


x = outer(20, 30)
print(x)
