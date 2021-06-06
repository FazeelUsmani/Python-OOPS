x = 5  # type of x is an integer
print(type(x))

x = "Educative"  # type x is now string
print(type(x))


class Dog:
    def Speak(self):
        print("Bhou Bhou")


class Cat:
    def Speak(self):
        print("Meow meow")


class AnimalSound:
    def Sound(self, animal):
        print("The animal is ", type(animal))
        animal.Speak()

sound = AnimalSound()
dog = Dog()
cat = Cat()

sound.Sound(dog)
sound.Sound(cat)


