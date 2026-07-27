class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

    def Display(self):
        print(self.name)
        print(self.salary)

Employee1=Employee("Ajay",5000)
Employee1.Display()
