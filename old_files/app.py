from account import *
from database import *
from utils import *


def app() -> None:

    # users = {}
    exit = False

    while not exit:
        login = input("Pls login or accept defeat: \nOr press e for exit program: ")

        if login == "e":
            exit = True

        elif not db_userexistence(login):
            new_login = input("Invalid Input. Do you want to register?: [y/n]")
            print()

            if new_login == "y":
                username = input("Register your name: ")
                fullname = input("Type in your full name: ")
                address = input("Type in your address")
                email = input("Type in your email")
                password = input("Register new password: ")
                print()

                new_user = BankAccount(
                    username, fullname, address, email, hash_password(password)
                )
                db_insert(new_user)

            else:
                check_exit = input("Do you want to exit the program?: [y/n]")
                if check_exit == "y":
                    exit = True
        else:
            check_password = input("pls enter your password: ")

            if not db_passwordcheck(login, check_password):
                print("sorry wrong password!")
                print()

            else:
                logout = False
                user = db_recreateObject(login)
                while not logout:
                    method = input(
                        f"""
                    Current Balance : {user.get_balance()}

                    Diposit?: [d]
                    Withdrawal?: [w]
                    History?: [h] 
                    Logout?:  [l]
                    """
                    )
                    print()

                    # Diposit Function
                    if method == "d":
                        amount = input("What amount do you want to deposit?: ")

                        if check_amount(amount):
                            user.deposit(amount)
                            db_updatebalance(user)
                            print_accountstatus(user)

                    # Withdrawal function
                    elif method == "w":
                        amount = input("What amount do you want to withdrawal?: ")

                        if check_amountwithdrawal(amount, user):
                            user.withdrawal(amount)
                            db_updatebalance(user)
                            print_accountstatus(user)

                    elif method == "h":
                        print_history(user)

                    elif method == "l":
                        logout = True
                        print("Logged out successfully")

                    else:
                        print("invalid input. Pls choose a method.")
                        print()
