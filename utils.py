from account import *


def check_float(amount: str) -> bool:
    """checks if input is really a float"""

    try:
        n = float(amount)
        return True
    except ValueError as e:
        print(f"{e}. Pls input an invalid amount.")
        return False
        


def check_amount(amount: str) -> float:
    """checks if the amount is in the right size"""

    if check_float(amount):
        amount = float(amount)
        if amount >= 0:
            return True
        
        else:
            print("Amount can't be negative.")
            return False
    
    else:
        return False




def check_amountwithdrawal(amount: str, user: BankAccount) -> bool:
    """checks if the amount is in the user capabilities"""

    if check_float(amount):
        amount = float(amount)

        if amount >= 0 and not amount >= user.get_balance():
            return True

        else:
            print("Amount can't be negative or bigger than your account balance.")
            return False
    
    else:
        return False
        


def print_accountstatus(user: BankAccount) -> None:
    """this function currently only prints the user account balance"""
    
    print(f"New Account Balance: {user.get_balance()}")
    # print(f"Account History: {user.get_history()}")
    print()


def print_history(user: BankAccount) -> None:
    """this function prints the last user history"""

    history = user.get_history()

    print("History: \n")
    for key, value in history.items():
        print(f"{key} : {value}")