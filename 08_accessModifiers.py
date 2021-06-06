class Employee:
    def __init__(self, ID, salary):
        self.ID = ID
        self.__salary = salary  # salary is a private property

    def getSalary(self):
        return self.__salary


Steve = Employee(3789, 2500)
print("ID:", Steve.ID)
# print("Salary:", Steve.__salary)  # this will cause an error
# Instead you can have a public function which inturn calls __salary variable
print(Steve.getSalary())

print("\n\n")
print("Implementing private methods")

class Employee:
    def __init__(self, ID, salary):
        self.ID = ID
        self.__salary = salary  # salary is a private property

    def displaySalary(self):  # displaySalary is a public method
        print("Salary:", self.__salary)

    def __displayID(self):  # displayID is a private method
        print("ID:", self.ID)


Steve = Employee(3789, 2500)
Steve.displaySalary()
# Steve.__displayID()  # this will generate an error


print("\n\n")
print("Accessing private variables from main using _className.__privateVariable")
class Employee:
    def __init__(self, ID, salary):
        self.ID = ID
        self.__salary = salary  # salary is a private property
        print("Init")


Steve = Employee(3789, 2500)
print(Steve._Employee__salary)  # accessing a private property
print("before init")
print(Steve.ID)