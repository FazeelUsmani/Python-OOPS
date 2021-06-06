class Shape:  # Shape is a child class of ABC
    def area(self):
        pass

    def perimeter(self):
        pass


class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return (self.length * self.length)

    def perimeter(self):
        return (4 * self.length)


shape = Shape()
square = Square(4)
print(square.area())
print(square.perimeter())



print("\n\nImplementing ABC")

from abc import ABC, abstractmethod

class Shape(ABC):  # Shape is a child class of ABC
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return (self.length*self.length)

    def perimeter(self):
        return (self.length*4)


square = Square(5)
print(square.area())
print(square.perimeter())
