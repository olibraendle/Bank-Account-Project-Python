import pytest
import sqlite3
from account import BankAccount
from database import (
    db_insert,
    db_fetchdata_user,
    db_userexistence,
    db_passwordcheck,
    db_updatebalance,
    db_recreateObject,
)
from utils import hash_password


# --- insert and fetch ---


def test_insert_and_fetch_user(inserted_user):
    data = db_fetchdata_user("oli")
    assert data[0] == "oli"
    assert data[1] == "Oli M"


def test_fetch_nonexistent_user_returns_empty(db):
    data = db_fetchdata_user("nobody")
    assert data == ()


# --- user existence ---


def test_user_exists_after_insert(inserted_user):
    assert db_userexistence("oli") is True


def test_user_does_not_exist(db):
    assert db_userexistence("nobody") is False


# --- duplicate username ---


def test_duplicate_username_rejected(inserted_user):
    """
    The username column has PRIMARY KEY — inserting the same username twice
    must raise an IntegrityError.
    """
    duplicate = BankAccount("oli", "Other", "x", "x@x.com", hash_password("x"))
    with pytest.raises(sqlite3.IntegrityError):
        db_insert(duplicate)


# --- password check ---


def test_correct_password(inserted_user):
    assert db_passwordcheck("oli", "secret") is True


def test_wrong_password(inserted_user):
    assert db_passwordcheck("oli", "wrongpassword") is False


# --- update balance ---


def test_update_balance(inserted_user):
    inserted_user.deposit("500")
    db_updatebalance(inserted_user)

    data = db_fetchdata_user("oli")
    assert data[5] == 500.0


# --- recreate object ---


def test_recreate_object_has_correct_username(inserted_user):
    obj = db_recreateObject("oli")
    assert obj.username == "oli"


def test_recreate_object_has_correct_balance(inserted_user):
    inserted_user.deposit("250")
    db_updatebalance(inserted_user)

    obj = db_recreateObject("oli")
    assert obj.get_balance() == 250.0
