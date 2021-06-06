print("Bad implementation of Login class")
class User:
    def __init__(self, userName=None, password=None):
        self.userName = userName
        self.password = password

    def login(self, userName, password):
        if ((self.userName.lower() == userName.lower())
                and (self.password == password)):
            print("Access Granted!")
        else:
            print("Invalid Credentials!")


Steve = User("Steve", "12345")
Steve.login("steve", "12345")
Steve.login("steve", "6789")
Steve.password = "6789"
Steve.login("steve", "6789")


print("\n\n\nGood implementation of Login class")
class User:
    def __init__(self, userName=None, password=None):
        self.__userName = userName
        self.__password = password

    def login(self, userName, password):
        if ((self.__userName.lower() == userName.lower())
                and (self.__password == password)):
            print(
                "Access Granted against username:",
                self.__userName.lower(),
                "and password:",
                self.__password)
        else:
            print("Invalid Credentials!")


# created a new User object and stored the password and username
Steve = User("Steve", "12345")
Steve.login("steve", "12345")  # Grants access because credentials are valid
# does not grant access since the credentails are invalid
Steve.login("steve", "6789")
Steve.__password  # compilation error will occur due to this line
