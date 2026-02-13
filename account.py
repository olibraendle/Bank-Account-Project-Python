import datetime
import json

class BankAccount:


    def __init__(self, username: str,
                  fullname: str,
                  address: str,
                  email: str,
                  password: str, 
                  balance= 0, 
                  account_history = dict({}))-> None:
        """initialize the user"""

        self.username = username
        self.fullname = fullname
        self.__address = address
        self.__email = email
        self.__password = password
        self.__balance = balance
        self.__account_history = account_history
        

    def get_data_db(self) -> tuple:
        """return all the information about a user for the database"""

        return (self.username, 
                self.fullname, 
                self.__address, 
                self.__email,
                self.__password, 
                self.__balance,
                json.dumps(self.__account_history))



    def get_balance(self) -> float:
        return self.__balance


    def get_history(self) -> dict:
        return self.__account_history



    def deposit(self, amount: str) -> None:
        self.__balance += float(amount)

        new_time = str(datetime.datetime.now())
        self.__account_history.update({new_time : self.__balance})



    def withdrawal(self, amount: str) -> None:
        self.__balance -= float(amount)
        
        new_time = str(datetime.datetime.now())
        self.__account_history.update({new_time : self.__balance})

    


    # def check_passwords(self, string: str) -> bool:
    #     if string == self.__password:
    #         return True
    #     else:
    #         return False