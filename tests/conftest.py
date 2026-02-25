import pytest
from account import BankAccount
from database import db_init, db_insert
from utils import hash_password


@pytest.fixture
def user():
    """A fresh BankAccount with zero balance for each test."""
    return BankAccount(
        "oli", "Oli M", "Street 1", "oli@mail.com", hash_password("secret")
    )


@pytest.fixture
def db(tmp_path, monkeypatch):
    """
    Creates a temporary directory, moves the working directory there,
    and initialises a fresh in-file database for each test.
    The temp directory (and its users.db) is deleted automatically after the test.
    """
    monkeypatch.chdir(tmp_path)
    db_init()
    return tmp_path


@pytest.fixture
def inserted_user(db):
    """Inserts a test user into the temp database and returns the object."""
    user = BankAccount(
        "oli", "Oli M", "Street 1", "oli@mail.com", hash_password("secret")
    )
    db_insert(user)
    return user
