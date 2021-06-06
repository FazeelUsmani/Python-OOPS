class Player:
    teamName = 'Liverpool'  # class variable

    def __init__(self, name) -> None:
        self.name = name   # instance variables

    @staticmethod
    def demo():
        print("My name is ", Player.teamName)   # can only access class variables        
        print("I'm a static method")
        # print(Player.name)      # get's an error as name is instance variable

p1 = Player('Fazeel')
p1.demo()
Player.demo()

print()
class BodyInfo:
    @staticmethod
    def bmi(weight, height):
        return weight / (height**2)


weight = 75
height = 1.8
print(BodyInfo.bmi(weight, height))
