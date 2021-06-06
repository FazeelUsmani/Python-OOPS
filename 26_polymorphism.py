class Rectangle():
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        self.sides = 4

    def getArea(self):
        return (self.width*self.height)

class Circle():
    def __init__(self, radius=0):
        self.radius = radius
        self.sides = 0

    def getArea(self):
        return (3.14 * self.radius * self.radius)
        

shapes = [Rectangle(4, 6), Circle(7)]

print("Sides of a rectangle are ", str(shapes[0].sides))
print("Area of a rectangle is ", str(shapes[0].getArea()))

print("Sides of a circle are", str(shapes[1].sides))
print("Area of circle is:", str(shapes[1].getArea()))
