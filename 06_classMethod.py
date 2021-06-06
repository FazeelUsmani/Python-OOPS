class MyClass:
    classVariable = 'educative'

    @classmethod
    def demo(cls):
        return cls.classVariable

print(MyClass.demo())
MyClass.classVariable = 'Manchestor United'   # can change class variable
print(MyClass.demo())

print("\n\nclass method implementation\m")
class Player:
    teamName = 'Liverpool'  # class variables

    def __init__(self, name):
        self.name = name  # creating instance variables

    @classmethod
    def getTeamName(cls):
        return cls.teamName


print(Player.getTeamName())




