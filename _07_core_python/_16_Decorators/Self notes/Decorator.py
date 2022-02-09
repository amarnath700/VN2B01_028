"""
Decorators are a very powerful and useful tool in Python.
it allows programmers to modify the behavior of function or class
"""


def fun(n):
    def fun1():
        print("Hello")

    def fun2():
        print("World")

    if n == 1:
        return fun1()
    else:
        return fun2()


fun(1)
fun(2)


# Decorators
def hello(hell):
    def inner():
        print("Hello")
        return hell

    return inner()


@hello
def world():
    print("world")


print(world())


#
def family(group):
    def inner():
        print("My dear Family Members")

        def inner1():
            print("grand son and daughter")
            return group

        print("Grand Father And mother")
        return inner1()

    return inner()


@family
def middle():
    print("father and mother")


print(middle())


# parameter decorators
def multiple(func):
    def inner(*args):
        print(*args)
        return func

    return inner()


@multiple
def num(a, b):
    print("i of square of j")
    return a ** b


a = 5
b = 6
print(num(a, b))


# multiple decorators
def family(group):
    def inner():
        print("Grand son and daughter")
        return group

    return inner()


def family1(group):
    def inner():
        print("My dear Family1 Members")
        print("Grand Father And mother")
        x = group()
        return x
    return inner()


@family
@family1
def middle():
    print("father and mother")
    return





# defining a decorator
def hello_decorator(func):
    # inner1 is a Wrapper function in
    # which the argument is called

    # inner function can access the outer local
    # functions like in this case "func"
    def inner1():
        print("Hello, this is before function execution")

        # calling the actual function now
        # inside the wrapper function.
        func()

        print("This is after function execution")

    return inner1


# defining a function, to be called inside wrapper
def function_to_be_used():
    print("This is inside the function !!")


# passing 'function_to_be_used' inside the
# decorator to control its behaviour
function_to_be_used = hello_decorator(function_to_be_used)

# calling the function
function_to_be_used()


def hello_decorator(func):
    def inner1(*args, **kwargs):
        print("before Execution")

        # getting the returned value
        returned_value = func(*args, **kwargs)
        print("after Execution")

        # returning the value to the original frame
        return returned_value

    return inner1


# adding decorator to the function
@hello_decorator
def sum_two_numbers(a, b):
    print("Inside the function")
    return a + b


a, b = 1, 2

# getting the value through return of the function
print("Sum =", sum_two_numbers(a, b))


# chaining Decorator

def decor1(func):
    def inner():
        x = func()
        return x ** x

    return inner


def decor(func):
    def inner():
        x = func()
        return 3 ** x

    return inner


@decor1
@decor
def num():
    return 1


print(num())


decor1(decor(num))




