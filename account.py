from utils import *


class BankAccount:


    def __init__(self, username, password):
        """initialize the user"""

        self.username = username
        self.password = password
        self.balance = 0
        self.account_history = []
        
        

    def deposit(self, amount):

        if check_if_float(amount):
            if float(amount) < 0:
                print("Can't add negative amount. Pls add a correct amount.")
                print()

            else:
                self.balance += float(amount)
                self.account_history.append(self.balance)

        else:
            print("Pls add a number not a string.")
            print()


    def withdrawal(self, amount):

        if check_if_float(amount):
            if float(amount) > self.balance:
                print("Withdrawal is too high for your balance.")
                print()

            else:
                self.balance -= float(amount)
                self.account_history.append(self.balance)

        else:
            print("Pls add a number not a string.")
            print()
