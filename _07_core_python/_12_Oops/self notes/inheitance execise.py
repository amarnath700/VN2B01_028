
class Vn2:
    def __init__(self, name, em_id, language, exper):
        self.name = name
        self.em_id = em_id
        self.language = language
        self.exper = exper

    def display(self):
        print(self.name, self.em_id)


class Job(Vn2):
    def dis(self):
        print(self.language, self.exper)


name = input("Enter name:")
em_id = input("enter em_id:")
language = input("enter language:")
exper = float(input("enter year of experience:"))
v = Job(name, em_id, language, exper)
v.display()
v.dis()
