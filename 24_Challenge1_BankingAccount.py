class Account:
    def __init__(self, title=None, balance=0):
        self.title = title
        self.balance = balance


class SavingsAccount(Account):
    def __init__(self, title=None, balance=0, interestRate=0):
        super().__init__(title, balance)
        self.interestRate = interestRate


Mark = Account("Mark", 5000, 5)
print(Mark.title)
print(Mark.balance)
print(Mark.interestRate)
    

            


