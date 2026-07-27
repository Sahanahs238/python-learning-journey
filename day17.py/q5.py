class Animal:
    def Sound(self):
        print("Animal makes Sound")

class Cat(Animal):
    def Sound(self):
        print("meow meow")

class Dog(Animal):
    def Sound(self):
        print("bow bow")

animal = Animal()
dog=Dog()
cat=Cat()
animal.Sound()
dog.Sound()
cat.Sound()