

class BankAccount:


    def __init__(self, name, password):
        """initialize the user"""

        self.name = name
        self.password = password
        self.balance = 0

    
    

    def create_account(self, name, password):
        """create the account of the user"""

        self.name = name
        self.password = password
        
        account = {"username" : self.name,
                   "password" : self.password,
                   "balance" : self.balance,
                   "history" : []
                    }
        return account

    

users = {}
exit = True
while exit:
    login = input("pls login: ")

    if login not in users:
        new_login = input("Account is not registered yet. Want to create a new account?: [y/n]")

        if new_login == 'y':
            username = input("Input your name: ")
            password = input("input new password: ")
            account = BankAccount(username, password)
            new_account = account.create_account(username, password)
            users.update({username : new_account})
            print(users)
        else:
            continue
    else:
        check_password = input("pls enter your password: ")
        
        if check_password != users[login]['password']:
            print("sorry wrong password!")
        else:
            method = input("Terminal: ")