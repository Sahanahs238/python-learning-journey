class Employee:
    def __init__(self):
        self.__salary=90000

    def Set_salary(self,salary):
        self.__salary=salary

    def Get_salary(self):
        return self.__salary
    
e=Employee()
e.Set_salary(99000)
print(e.Get_salary())
