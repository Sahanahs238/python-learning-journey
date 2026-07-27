class Student:
    def __init__(self,):
        self.__marks=90

    def Set_marks(self,marks):
        self.__marks=marks

    def Get_marks(self):
        return self.__marks

s=Student()
s.Set_marks(98)
print(s.Get_marks())

