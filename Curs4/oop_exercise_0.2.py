class User:
    def __init__(self, name):
        self.name = name
        self.__password = None

    @property
    def password(self):
        return self.__password[0] + '*' * (len(self.__password) - 2) + self.__password[-1]

    @password.setter
    def password(self, password):
        if len(password) < 6:
            self.__password = password + '#' * (6 - len(password))
        else:
            self.__password = password

    @password.deleter
    def password(self):
        print("Delete password")
        del self.__password


eu = User('Mihai')
eu.password = 'abc'
print(eu.password)
eu.password = 'abcdd123'
print(eu.password)
del eu.password

