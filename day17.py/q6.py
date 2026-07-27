class Animal:
    def eat(self):
        print("Animal is eating")


class Dog(Animal):
    def eat(self):
        print("Dog eats chicken")

    def bark(self):
        print("Dog barks")


dog = Dog()

dog.eat()
dog.bark()