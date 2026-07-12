class Rectangle:
    pass
    def area(self):
        print("length",self.length)
        print("breadth",self.breadth)
        return self.length*self.breadth

shape = Rectangle()
shape.length=2
shape.breadth=2

print("area=",shape.area())
