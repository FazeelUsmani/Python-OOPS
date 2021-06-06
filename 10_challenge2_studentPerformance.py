# Implement a class Student that has four properties and two methods. All these attributes (properties and methods) should be public. This problem can be broken down into three tasks:
# Task 1 #

# Implement a constructor to initialize the values of four properties: name, phy, chem and, bio.
# Task 2 #

# Implement a method, totalObtained, in the Student class that calculates total marks of a student.

class Student:
    def __init__(self, name, phy, chem, bio):
        self.name = name
        self.phy = phy
        self.chem = chem
        self.bio = bio
    
    def totalObtained(self):
        return self.phy + self.chem + self.bio

    
    def percentage(self):
        return (self.totalObtained()*100)/300

    
        

