import account as acc

def app():

    users = {}
    exit = False
    print(" dfssdfsdffworld")
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

            if user.password != check_password:
                print("sorry wrong password!")
                print()
            else:
                logout = False

                while not logout:
                    method = input(f"""
                    Current Balance : {user.balance}
                    Bank Account History: {user.account_history}

                    Diposit?: [d]
                    Withdrawal?: [w]
                    Logout?:  [l]
                    """)
                    print()

                    if method == 'd':
                        amount = input("What amount do you want to deposit?: ")
                        user.deposit(amount)

                        print(f"New Account Balance: {user.balance}")
                        print(f"Account History: {user.account_history}")
                        print()
                    
                    elif method == 'w':
                        amount = input("What amount do you want to withdrawal?: ")
                        user.withdrawal(amount)
                        print(f"New Account Balance: {user.balance}")
                        print(f"Account History: {user.account_history}")
                        print()
                    
                    elif method == 'l':
                        logout = True
                        print("Logged out successfully")