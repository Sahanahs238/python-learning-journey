class Circle:
    def Draw(self):
        print("drawing a circle")

class Square:
    def Draw(self):
        print("drawing a sqiare")

class Triangle:
    def Draw(self):
        print("drawing a triangle")

def Draw_shape(shape):
    shape.Draw()

c = Circle()
s = Square()
t = Triangle()

Draw_shape(c)
Draw_shape(s)
Draw_shape(t)
