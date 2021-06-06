class Rectangle:
    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def area(self):
        return (self.__length * self.__width)

    def perimeter(self):
        return (2 * (self.__length + self.__width))


obj1 = Rectangle(4, 5)
print("Area is", obj1.area())
print("Perimeter is", obj1.perimeter())
