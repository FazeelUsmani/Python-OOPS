class Circle:
    def __init__(self, radius):
        self.__radius = radius
    
    def print_area(self):
        return (3.14 * self.__radius**2)
    
obj = Circle(3)

print(obj.print_area())


class Employee:

    def __init__(self, name='', ID=0, department=''):
        self.__name = name
        self.__ID = ID
        self.__department = department

    def get_name(self):
        return self.__name
    def set_name(self, x):
        self.__name = x

    def get_ID(self):
        return self.__ID
    def set_ID(self, x):
        self.__ID = x

    def get_department(self):
        return self.__department
    def set_department(self, x):
        self.__department = x
    
        