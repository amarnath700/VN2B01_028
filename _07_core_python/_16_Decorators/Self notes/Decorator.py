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

a = fun(1)
b = fun(2)
