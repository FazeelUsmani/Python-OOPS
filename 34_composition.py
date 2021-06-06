class Engine:
    def __init__(self, capacity=0):
        self.capacity = capacity

    def printDetails(self):
        print("Engine Details: (In CC)", self.capacity)


class Tires:
    def __init__(self, tires=0):
        self.tires = tires

    def printDetails(self):
        print("Number of tires:", self.tires)


class Doors:
    def __init__(self, doors=0):
        self.doors = doors

    def printDetails(self):
        print("Number of doors:", self.doors)


class Car:
    def __init__(self, eng, tr, dr, color):
        self.eObj = Engine(eng)
        self.trObj = Tires(tr)
        self.drObj = Doors(dr)
        self.color = color
    
    def printDetails(self):
        self.eObj.printDetails()
        self.trObj.printDetails()
        self.drObj.printDetails()
        print("Car color: ", self.color)



car = Car(1600, 4, 2, "Grey")
car.printDetails()