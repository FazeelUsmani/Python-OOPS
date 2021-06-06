class Student:
    __name = None
    __RollNumber = None
    
    def getName(self):
        return self.__name

    def setName(self, x):
        self.__name = x
    
    def getRollNumber(self):
        return self.__RollNumber

    def setRollNumber(self, x):
        self.__RollNumber = x
        


demo1 = Student()
demo1.setName("Alex")
print("Name:", demo1.getName())
demo1.setRollNumber(3789)
print("Roll Number:", demo1.getRollNumber())
