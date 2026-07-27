class Circle:
    def __init__(self,radius):
        self.radius=radius

    def area(self):
        print(3.14 * self.radius * self.radius)

circle1=Circle(4)
circle1.area()
