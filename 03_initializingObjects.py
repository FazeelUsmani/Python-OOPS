class Employee:
    def __init__(self, ID=None, salary=0, department=None):
        self.ID = ID
        self.salary = salary
        self.department = department

    
Steve = Employee(123, 15000, "Human Resources")

print("Steve")
print("ID: ", Steve.ID)
print("Salary: ", Steve.salary)
print("Department: ", Steve.department)

Mark = Employee()
print("Mark")
print("ID: ", Mark.ID)
print("Salary: ", Mark.salary)
print("Department: ", Mark.department)

