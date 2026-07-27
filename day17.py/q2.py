class Vehicle:
    def start(self):
        print("vehicle started")

class Car(Vehicle):
    def Drive(self):
        print("car is driving")

car1=Car()
car1.start()
car1.Drive()