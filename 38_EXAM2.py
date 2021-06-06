class Salary:

    def __init__(self, base_pay=0, bonus=0):
        self.__base_pay = base_pay
        self.__bonus = bonus
    
    def get_bonus(self):
        return self.__bonus

    def set_bonus(self, x):
        self.__bonus = x

    def get_base_pay(self):
        return self.__base_pay
    
    def set_base_pay(self, x):
        self.__base_pay = x

    # Write methods Salary class here

class Employee:
    
    def __init__(self, name='', base_pay=0, bonus=0):
        self.__name = name 
        self.__salary = Salary(base_pay, bonus)

    def get_name(self):
        return self.__name
    
    def set_name(self, x):
        self.__name = x

    def get_salary(self):
        return self.__salary.get_base_pay() + self.__salary.get_bonus()

    def set_salary(self, base_pay, bonus):
        self.__salary.base_pay = base_pay
        self.__salary.bonus = bonus


E1 = Employee("Fazeel", 2000, 50)

print(E1.get_name())
E1.set_name("Usmani")
print(E1.get_name())
print()
print(E1.get_salary())