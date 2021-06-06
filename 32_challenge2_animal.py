class Animal:
    def __init__(self, name=None, sound=None):
        self.name = name
        self.sound = sound

    def Animal_details(self):
        print("Name: ", self.name)
        print("Sound: ", self.sound)


class Dog(Animal):
    
    def __init__(self, name=None, sound=None, family=None):        
        super().__init__(name, sound)
        self.family = family

    def Animal_details(self):
        super().Animal_details()
        print("Family: ", self.family)

class Sheep(Animal):
    
    def __init__(self, name=None, sound=None, color=None):
        super().__init__(name, sound)
        self.color = color

    def Animal_details(self):        
        super().Animal_details()
        print("Color: ", self.color)

d = Dog("Pongo", "Woof Woof", "Husky")
d.Animal_details()
print(" ")
s = Sheep("Billy", "Baaa Baaa", "White")
s.Animal_details()