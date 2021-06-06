print("Single level inheritance")
class Vehicle:  # parent class
    def setTopSpeed(self, speed):  # defining the set
        self.topSpeed = speed
        print("Top speed is set to", self.topSpeed)


class Car(Vehicle):  # child class
    def openTrunk(self):
        print("Trunk is now open.")


corolla = Car()  # creating an object of the Car class
corolla.setTopSpeed(220)  # accessing methods from the parent class
corolla.openTrunk()  # accessing method from its own class
 
