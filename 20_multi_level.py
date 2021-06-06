class Vehicle:
    def setTopSpeed(self, speed):
        self.topSpeed = speed
        print("The top speed is set to ", self.topSpeed)

    
class Car(Vehicle):
    def openTrunk(self):
        print("Trunk is now open")


class Hybrid(Car):
    def turnOnHybrid(self):
        print("Hybrid mode is now switched on")

camry = Hybrid()
camry.setTopSpeed(120)
camry.openTrunk()
camry.turnOnHybrid()
print(camry.topSpeed)