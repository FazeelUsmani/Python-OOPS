class Country:
    def __init__(self, name=None, population=0):
        self.name = name
        self.population = population

    def printDetails(self):
        print("In country")
        print("Country name: ", self.name)
        print("Populaiton: ", self.population)


class Person:
    def __init__(self, name, country):
        self.name = name
        self.country = country

    def printDetails(self):
        print("Person name: ", self.name)
        self.country.printDetails()

c = Country("India", 121)
p = Person("Fazeel", c)
p.printDetails()

del p
print("")
c.printDetails()

