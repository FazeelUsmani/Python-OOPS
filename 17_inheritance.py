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
        Vehicle.__init__(self, make, color, model)    
        # here we can also user super() instead of Vehicle
        self.doors = doors

    def printCarDetails(self):
        self.printDetails()
        print("Doors: ", self.doors)

Bolero = Car("Mahindra", "Turf Green", 2010, 5)
Bolero.printDetails()



    