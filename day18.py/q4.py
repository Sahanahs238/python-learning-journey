class Student:
    def Info(self):
        print(" student information")

class Teacher:
    def Info(self):
        print(" teacher information")

def Display(person):
    person.Info()

stu = Student()
tea = Teacher()

Display(stu)
Display(tea)
        
