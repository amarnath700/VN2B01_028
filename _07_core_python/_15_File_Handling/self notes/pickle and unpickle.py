class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def display(self):
        print(self.name, self.age, self.grade)


import pickle


f = open('Student.dat', 'wb')
n = int(input('How many Students to add : '))

for i in range(n):
    name = input('Enter name:')
    age = input('Enter age: ')
    grade = input('Enter Grade: ')
    # create an Student class object
    s = Student(name, age, grade)
    # store the object e into file f
    pickle.dump(s, f)  # python objects to byte stream
# close the file
f.close()


f = open('Student.dat', 'rb')
print('Student details: ')
while True:
    try:
        # read object from file f
        obj = pickle.load(f)
        # display the contents of employee obj
        obj.display()
    except EOFError:
        print('End of file reached...')
        break
