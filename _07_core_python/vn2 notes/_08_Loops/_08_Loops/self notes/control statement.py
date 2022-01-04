"""
Control Statement:
    The concept of loops is available in almost all programming languages.
    Python loops help to iterate over a list, tuple, string, dictionary, and a set.
    There are two types of loop supported in Python “for” and “while”.
    The block of code is executed multiple times inside the loop until the condition fails.

    3 types of control statement:
    1. break
    2. continuous
    3. pass

    The loop control statements break the flow of execution and terminate/skip the iteration as per our need.
    Python break and continue are used inside the loop to change the flow of the loop from its standard procedure.

    A for-loop or while-loop is meant to iterate until the condition given fails.
    When you use a break or continue statement, the flow of the loop is changed from its normal way.

break statement:
The break statement takes care of terminating the loop in which it is used.
If the break statement is used inside nested loops, the current loop is terminated,
and the flow will continue with the code followed that comes after the loop.

The following are the steps involved in the flowchart.

Step 1:The loop execution starts.

Step 2:If the loop condition is true, it will execute step 2, wherein the body of the loop will get executed.

Step 3:If the loop’s body has a break statement, the loop will exit and go to Step 6.

Step 4:After the loop condition is executed and done, it will proceed to the next iteration in Step 4.

Step 5:If the loop condition is false, it will exit the loop and go to Step 6.

Step 6:End of the loop.


continue statement:
The continue statement skips the code that comes after it,
and the control is passed back to the start for the next iteration.

The following are the steps involved in the flowchart.

Step 1:The loop execution starts.

Step 2:The execution of code inside the loop will be done.
If there is a continued statement inside the loop, the control will go back to Step 4, i.e.,
the start of the loop for the next iteration.

Step 3:The execution of code inside the loop will be done.

Step 4:If there is a continue statement or the loop execution inside the body is done,
it will call the next iteration.

Step 5:Once the loop execution is complete, the loop will exit and go to step 7.

Step 6:If the loop condition in step 1 fails, it will exit the loop and go to step 7.

Step 7:End of the loop.


What is pass statement in Python?
Python pass is a null statement. When the Python interpreter comes across the across pass statement,
it does nothing and is ignored.

When to use the pass statement?
Consider you have a function or a class with the body left empty.
You plan to write the code in the future. The Python interpreter will throw an error
if it comes across an empty body.

A comment can also be added inside the body of the function or class,
but the interpreter ignores the comment and will throw an error.

The pass statement can be used inside the body of a function or class body. During execution, the interpreter,
when it comes across the pass statement, ignores and continues without giving any error.
"""