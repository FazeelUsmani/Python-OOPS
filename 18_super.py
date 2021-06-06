class Vehicle:  # defining the parent class
    fuelCap = 90


class Car(Vehicle):  # defining the child class
    fuelCap = 50

    def display(self):
        # accessing fuelCap from the Vehicle class using super()
        print("Fuel cap from the Vehicle Class:", super().fuelCap)

        # accessing fuelCap from the Vehicle class using self
        print("Fuel cap from the Car Class:", self.fuelCap)


obj1 = Car()  # creating a car object
obj1.display()  # calling the Car class method display()


print("\n\nCalling parent class methods")
class Vehicle:  # defining the parent class
    def display(self):  # defining diplay method in the parent class
        print("I am from the Vehicle Class")


class Car(Vehicle):  # defining the child class
    # defining diplay method in the parent class
    def display(self):
        super().display()
        print("I am from the Car Class")


obj1 = Car()  # creating a car object
obj1.display()  # calling the Car class method printOut()


print("\n\nsuper() to initialize variables in __init__")
class ParentClass():
    def __init__(self, a, b):
        self.a = a
        self.b = b


class ChildClass(ParentClass):
    def __init__(self, a, b, c):
        super().__init__(a, b)
        self.c = c


obj = ChildClass(1, 2, 3)
print(obj.a)
print(obj.b)
print(obj.c)

print("\n\n Using previous example")
class Vehicle:
    def __init__(self, make, color, model):
        self.make = make
        self.color = color
        self.model = model
    
    def printDetails(self):
        print("Manufacturer: ", self.make)
        print("Colr: ", self.color)
        print("Model: ", self.model)

class Car(Vehicle):
    def __init__(self, make, color, model, doors):
        super().__init__(make, color, model)    # but not use self while initializing Parent
        # here we can also user super() instead of Vehicle
        self.doors = doors

    def printCarDetails(self):
        self.printDetails()
        print("Doors: ", self.doors)

Bolero = Car("Mahindra", "Turf Green", 2010, 5)
Bolero.printDetails()



    