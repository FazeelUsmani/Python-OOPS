class Account:
    def __init__(self, title=None, balance=0):
        self.title = title
        self.balance = balance

    def getBalance(self):
        return self.balance

    def deposit(self, amount):
        self.balance += amount
        print("Balance after deposit is ", self.balance)

    def withdrawal(self, amount):
        self.balance -= amount
        print("Balance after withdrawal ", self.balance)

class SavingsAccount(Account):
    def __init__(self, title=None, balance=0, interestRate=0):
        super().__init__(title, balance)
        self.interestRate = interestRate

    def interestAmount(self):
        return (self.interestRate * self.balance)/100


obj1 = SavingsAccount("Mark", 2000, 5) 

print(obj1.getBalance())
obj1.deposit(4000)
obj1.withdrawal(1000)
print(obj1.interestAmount())






