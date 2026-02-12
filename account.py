
class BankAccount:


    def __init__(self, username: str, password: str) -> None:
        """initialize the user"""

        self.username = username
        self.__password = password
        self.__balance = 0
        self.__account_history = []
        
        

    def get_balance(self) -> float:
        return self.__balance


    def get_history(self) -> float:
        return self.__account_history



    def deposit(self, amount: str) -> None:
        self.__balance += float(amount)
        self.__account_history.append(self.__balance)



    def withdrawal(self, amount: str) -> None:
        self.__balance -= float(amount)
        self.__account_history.append(self.__balance)



    def check_passwords(self, string: str) -> bool:
        if string == self.__password:
            return True
        else:
            return False