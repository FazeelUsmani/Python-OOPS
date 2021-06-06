class Ingredient:
    def __init__(self, name=''):
        self.name = name

    def printDetails(self):
        print(self.name)


class Pizza:
    def __init__(self, cheese, tomato, topping, dough):
        self.cheese = Ingredient(cheese)
        self.tomato = Ingredient(tomato)
        self.pepperoni = Ingredient(topping)
    
    def __init__(self, name='', quantitiy=0):
        self.name = name

    def printDetails(self):
        print(self.name)


class Pizza:
    def __init__(self, cheese, tomato, topping, dough):
        self.cheese = Ingredient(cheese)
        self.tomato = Ingredient(tomato)
        self.topping = Ingredient(topping)
        self.dough = Ingredient(dough)


    def printIngredients(self):
        self.cheese.printDetails()
        self.tomato.printDetails()
        self.topping.printDetails()
        self.dough.printDetails()

pepperoni_pizza = Pizza('cheese', 'tomato', 'pepperoni', 'dough')
pepperoni_pizza.printIngredients()