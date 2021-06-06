# initializing values
class Employee:
    ID = 3758
    salary = 2500
    department = "HR"

print("Initializing values")
Steve = Employee()
print(Steve.ID)
print(Steve.salary)
print(Steve.department)
print()


# assigning values
class Employee:
    ID = None
    salary = None
    department = None

John = Employee()
John.ID = 123
John.salary = 1000
John.department = "Customer Service"

# creating properties outside class
John.title = "Manager"
print("Assigning Values")
print("ID: ", John.ID)
print("Salary: ", John.salary)
print("Department: ", John.department)
print("title: ", John.title)

