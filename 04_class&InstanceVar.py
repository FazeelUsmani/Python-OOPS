class Player:
    teamName = 'Liverpool'  # class variable

    def __init__(self, name):
        self.name = name

p1 = Player('Mark')
p2 = Player('Steve')

print("Name:", p1.name)
print("Team Name:", p1.teamName)
print("Name:", p2.name)
print("Team Name:", p2.teamName)

# can change class variable
p2.teamName = 'Manchester United'
print("Name:", p2.name)
print("Team Name:", p2.teamName)

print("\n\n\n")

print('Intance variable must be unique')

class Player:
    teamName = 'Liverpool'  # class variables
    # formerTeams = []   # wrong use of class variable 

    def __init__(self, name):
        self.name = name  # creating instance variables
        self.formerTeams = []


p1 = Player('Mark')
p1.formerTeams.append('Barcelona')
p2 = Player('Steve')
p2.formerTeams.append('Chelsea')

print("Name:", p1.name)
print("Team Name:", p1.teamName)
print(p1.formerTeams)
print("Name:", p2.name)
print("Team Name:", p2.teamName)
print(p2.formerTeams)



print("\n\n\n")
print("smart use of class variables")
class Player:
    teamName = 'Liverpool'      # class variables
    teamMembers = []

    def __init__(self, name):
        self.name = name        # creating instance variables
        self.formerTeams = []
        self.teamMembers.append(self.name)


p1 = Player('Mark')
p2 = Player('Steve')

print("Name:", p1.name)
print("Team Members:")
print(p1.teamMembers)
print("")
print("Name:", p2.name)
print("Team Members:")
print(p2.teamMembers)
