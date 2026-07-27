class Employee :
    def __init__(self,name):
        self.name=name

class Manager(Employee):
    pass

manager1=Manager("Ajay")
print(manager1.name)