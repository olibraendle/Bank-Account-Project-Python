import account as acc
from utils import *

def app():

    users = {}
    exit = False
   
    while not exit:
        login = input("pls login: ")
        
        if login not in users:
            new_login = input("Invalid Input. Do you want to register?: [y/n]")
            print()

            if new_login == 'y':
                username = input("Register your name: ")
                password = input("Register new password: ")
                print()

                new_user = acc.BankAccount(username, password)
                users.update({username : new_user})
                
            else:
                check_exit = input("Do you want to exit the program?: [y/n]")
                if check_exit == 'y':
                    exit = True
        else:
            check_password = input("pls enter your password: ")
            user = users[login]

            if not user.check_passwords(check_password):
                print("sorry wrong password!")
                print()
            else:
                logout = False

                while not logout:
                    method = input(f"""
                    Current Balance : {user.get_balance()}
                    Bank Account History: {user.get_history()}

                    Diposit?: [d]
                    Withdrawal?: [w]
                    Logout?:  [l]
                    """)
                    print()


                    # Diposit Function
                    if method == 'd':
                        amount = input("What amount do you want to deposit?: ")

                        if check_amount(amount):
                            user.deposit(amount)
                            print_accountstatus(user)
                    
                    # Withdrawal function
                    elif method == 'w':
                        amount = input("What amount do you want to withdrawal?: ")

                        if check_amountwithdrawal(amount, user):
                            user.withdrawal(amount)
                            print_accountstatus(user)
                    
                    elif method == 'l':
                        logout = True
                        print("Logged out successfully")

                    else:
                        print("invalid input. Pls choose a method.")
                        print()