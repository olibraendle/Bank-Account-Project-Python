import sqlite3
from account import *
import json
from utils import hash_password


def db_init():
    cx = sqlite3.connect("users.db")
    cu = cx.cursor()
    cu.execute(
        """
        CREATE TABLE IF NOT EXISTS users (
            username TEXT PRIMARY KEY,
            fullname TEXT,
            address TEXT,
            email TEXT,
            password TEXT,
            balance REAL,
            account_history TEXT
        )
    """
    )
    cx.commit()
    cx.close()


def db_insert(user: BankAccount) -> None:
    """this functions inserts a new user into the database"""

    with sqlite3.connect("users.db") as cx:

        data = user.get_data_db()
        cx.execute("insert into users values (?,?,?,?,?,?,?)", data)
        cx.commit()


def db_fetchdata_user(user: str) -> tuple:
    """fetches the data of the user that the program wants"""

    with sqlite3.connect("users.db") as cx:

        data = ()
        for row in cx.execute("select * from users where username = ?", (user,)):
            data += row

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

    with sqlite3.connect("users.db") as cx:
        cu = cx.execute("SELECT 1 FROM users WHERE username = ? LIMIT 1", (user,))
        return cu.fetchone() is not None


def db_updatebalance(user: BankAccount) -> None:
    """this function updates the bank balance if something changes"""

    with sqlite3.connect("users.db") as cx:

        data = user.get_data_db()

        username = data[0]
        new_balance = data[5]
        account_history = data[6]

        cx.execute(
            "update users set balance = ?, account_history = ? where username = ?",
            (new_balance, account_history, username),
        )
        cx.commit()


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
