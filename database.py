import sqlite3
from account import *
import json
from utils import hash_password

# print(help(sqlite3))


def db_insert(user: BankAccount) -> None:
    """this functions inserts a new user into the database"""

    ## standard block for initializing the db
    cx = sqlite3.connect("users.db")
    cu = cx.cursor()

    # check if the right table is already made otherwise pass it:
    try:
        cu.execute(
            "create table users (username, fullname, address, email, password, balance, account_history)"
        )
    except:
        pass

    data = user.get_data_db()
    cu.execute("insert into users values (?,?,?,?,?,?,?)", data)
    cx.commit()
    cx.close()


def db_fetchdata_user(user: str) -> tuple:
    """fetches the data of the user that the program wants"""

    ## standard block for initializing the db
    cx = sqlite3.connect("users.db")
    cu = cx.cursor()

    # check if the right table is already made otherwise pass it:
    try:
        cu.execute(
            "create table users (username, fullname, address, email, password, balance, account_history)"
        )
    except:
        pass

    data = ()
    for row in cu.execute("select * from users where username = ?", (user,)):
        data += row

    cx.close()
    return data


def db_passwordcheck(user: str, password: str) -> bool:
    """fetches the password from an existing user and return the password for checking"""
    check_password = db_fetchdata_user(user)[4]

    if hash_password(password) == check_password:
        return True

    else:
        return False


def db_userexistence(user: str) -> bool:
    """checks if the username already exists in the database"""

    ## standard block for initializing the db
    cx = sqlite3.connect("users.db")
    cu = cx.cursor()

    # check if the right table is already made otherwise pass it:
    try:
        cu.execute(
            "create table users (username, fullname, address, email, password, balance, account_history)"
        )
    except:
        pass

    for row in cu.execute("select username from users"):
        if row[0] == user:
            cx.close()
            return True

    else:
        cx.close()
        return False


def db_updatebalance(user: BankAccount) -> None:
    """this function updates the bank balance if something changes"""

    ## standard block for initializing the db
    cx = sqlite3.connect("users.db")
    cu = cx.cursor()

    # check if the right table is already made otherwise pass it:
    try:
        cu.execute(
            "create table users (username, fullname, address, email, password, balance, account_history)"
        )
    except:
        pass

    data = user.get_data_db()

    username = data[0]
    new_balance = data[5]
    account_history = data[6]

    cu.execute(
        "update users set balance = ?, account_history = ? where username = ?",
        (new_balance, account_history, username),
    )
    cx.commit()
    cx.close()


def db_recreateObject(username: str) -> BankAccount:
    """this function recreates the data from the DB and creates an object for the methods"""

    user = db_fetchdata_user(username)

    return BankAccount(
        username=user[0],
        fullname=user[1],
        address=user[2],
        email=user[3],
        password=user[4],
        balance=user[5],
        account_history=json.loads(user[6]),
    )
