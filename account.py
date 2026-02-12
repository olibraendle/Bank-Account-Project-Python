
class BankAccount:


    def __init__(self, username, password):
        """initialize the user"""

        self.username = username
        self.__password = password
        self.__balance = 0
        self.__account_history = []
        
        

    def get_balance(self):
        return self.__balance

    def get_history(self):
        return self.__account_history


    def deposit(self, amount):
        self.__balance += float(amount)
        self.__account_history.append(self.__balance)


    def withdrawal(self, amount):
        self.__balance -= float(amount)
        self.__account_history.append(self.__balance)


    def check_passwords(self, string):
        if string == self.__password:
            return True
        else:
            return False