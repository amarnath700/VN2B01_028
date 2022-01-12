"""
Python:
    Python is a general purpose interpreter,interactive mode, objected oriented programming
    and high-level language.


    Interpreted : Python is processed at runtime by the Interpreter. You do not need to compile
    your program before executing it
    Interactive : You can actually sit at a Python prompt and interact with the interpreter directly
    to write your programs.
    Object-Oriented − Python supports Object-Oriented style or technique of programming that encapsulates
    code within objects.
    high-level Language − Python is a great language for the beginner-level programmers and supports the
    development of a wide range of applications from simple text processing to WWW browsers to games.


History of python:
            Python was created by Guido van Rossum, and released in 1991.Now the python version is 3.10
            version 2.0 if we give 5/2 then output is 2
            version 3.0 if we give 5/2 then output is 2.5
            this is the simple example of version update


Why Python?
1.Simple Syntax
2.Length of code is very less when compare to remaining languages
3.Complex problems can be solved in simple manner

Feature of Python:
1.Simple to Learn
2.Open source ,we download Source code in free, we modify the code as we like
3.Portability , python program can run in any environment with same interface in all platform.
4.Object-oriented programming.
5.Standard libraries
6.Case-sensitive
7.Platform independent
8.no compilation and linking in python.
9.no data type declaration.















Important Questions: 1. Introduction: How interpreter works in python?
A.	Python is processed at runtime by interpreter .you do not need any compiler your program before executing it.
In python interpreter,execute line-by-line execution.


Python features
•	Simple to learn
•	Open source
•	Portability- it can be   embedded in every environment.
•	High-level interpreter- it will take memory management itself.
•	Object-oriented
•	Standard libraries-inside libraries function having
•	Platform independent
•	No type declaration
•	No compilation and linking


Interpreter CPython IronPython Jython
A.	Cpython: it is default and most widely used interpreter of python, written in c.
Cpython compiles any python code into byte code and that byte code interpreted through evaluation process.
 Cpython does not translate into python code to c
B.	Jython: jython compiles python code into java bytecode. We can run python code on the java platform
C.	Iron-python: iron-python is a popular python implementation has been written in c-sharp(C#) and has designed
 to run on the .net platform .it creates bridge between python and .net universe.


Dynamically typed programming language
A.	Static: data type are checking before execution.
B.	Dynamic: data type are checking during execution.
    python is an interpreter, interpreter can execute code in line-by-line execution
    thus data type checking done during execution. Hence, python is a dynamically typed programming language.


Procedure Oriented vs Object oriented programming languages

Procedural Oriented Programming	:
In procedural programming, program is divided into small parts called functions.
Procedural programming follows top-down approach.
There is no access specifier in procedural programming.
Adding new data and function is not easy.
Procedural programming does not have any proper way for hiding data so it is less secure.
In procedural programming, overloading is not possible.
In procedural programming, function is more important than data.
Procedural programming is based on unreal world.
Examples: C, FORTRAN, Pascal, Basic etc.


object-oriented programming:
In object-oriented programming, program is divided into small parts called objects.
Object-oriented programming have access specifiers like private, public, protected etc.
Adding new data and function is easy.
Object-oriented programming provides data hiding, so it is more secure.
Overloading is possible in object-oriented programming.
In object-oriented programming, data is more important than function.
Object-oriented programming is based on real world.
Examples: C++, Java, Python, C# etc.


Setting path in python. Importance?
Your Python program and executable code can reside in any directory of your system, therefore Operating System
provides a specific search path that index the directories Operating System should search for executable code.
The Path is set in the Environment Variable of My Computer properties:
To set path follow the steps:
Right-click on My Computer ->Properties ->Advanced System setting ->Environment Variable ->New

In Variable name write path and in Variable value copy path up to
C://Python(i.e., path where Python is installed). Click Ok ->Ok.


Environment variables importance in python?
Environment variables— variables that exist outside your code as part of your server environment— can help
you by both streamlining and making more secure the process of running your scripts and applications.



Different ways to run python program?
Here are the ways with which we can run a Python script.

Interactive Mode
Command Line
Text Editor (VS Code)
IDE (PyCharm)

Interactive Mode:
In Interactive Mode, you can run your script line by line in a sequence.
To enter an interactive mode, you will have to open Command Prompt on your Windows machine and
type ‘python’ and press Enter.

Command Line
To run a Python script store in a ‘.py’ file in command line, we have to write ‘python’ keyword
before the file name in the command prompt.

Text Editor (VS Code)
To run Python scripts on a text editor like VS Code (Visual Studio Code) then you will have to do the following:
Go in the extension section or press ‘Ctrl+Shift+X’ on Windows, then search and install the extension named ‘Python’
and ‘Code Runner’. Restart your vs code after that.
Now, create a new file with the name ‘hello.py’ and write the below code in it:
print('Hello World!')
Then, right click anywhere in the text area and select the option that says ‘Run Code’ or
press ‘Ctrl+Alt+N’ to run the code.

IDE (PyCharm)
To run Python scripts on a IDE (Integrated Development Environment) like PyCharm,





source file:
Python source files are files that contain Python source code.
As Python can be used as a scripting language, Python source files can be considered as scripts.
PYW files are invoked on pythonw.exe instead of python.exe in order to prevent a DOS console from popping up to
display the output

Compiler and Interpreter
Compilers and interpreters are programs that help convert the high level language (Source Code) into machine codes
to be understood by the computers. Computer programs are usually written on high level languages.
A high level language is one that can be understood by humans.
To make it clear, they contain words and phrases from the languages in common use – English or other
languages for example. However, computers cannot understand high level languages as we humans do.
They can only understand the programs that are developed in binary systems known as a machine code.
To start with, a computer program is usually written in high level language described as a source code.
These source codes must be converted into machine language and here comes the role of compilers and interpreters.

compiler:
A compiler creates the program. It will analyze all the language statements to check if they are correct.
If it comes across something incorrect, it will give an error message.
If there are no errors spotted, the compiler will convert the source code into machine code.
The compiler links the different code files into programs that can be run such as exe.
Finally, the program runs.



interpreter:
An interpreter creates the program. It neither links the files nor generates machine code.
The source statements are executed line by line while executing the program.

interpreted* programming language

cpython vs ironpyhon vs jython:
interactive
object-oriented
high-level programming language
functional programming and structured programming
procedural vs object-oriented programming
Dynamically typed programming language  int x = 10 <==>  x = 10
Automatic garbage collection



"""
my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# stat from index 1 with step 2( means 1, 3, 5, an so on)
for i in my_list[1::2]:
    print(i, end=" ")
