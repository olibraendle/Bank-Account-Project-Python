from account import BankAccount
from utils import hash_password


def test_initial_balance_is_zero(user):
    assert user.get_balance() == 0


def test_deposit_increases_balance(user):
    user.deposit("100")
    assert user.get_balance() == 100.0


def test_multiple_deposits_add_up(user):
    user.deposit("100")
    user.deposit("50")
    assert user.get_balance() == 150.0


def test_withdrawal_decreases_balance(user):
    user.deposit("100")
    user.withdrawal("40")
    assert user.get_balance() == 60.0


def test_withdrawal_exact_balance(user):
    user.deposit("100")
    user.withdrawal("100")
    assert user.get_balance() == 0.0


def test_deposit_records_in_history(user):
    user.deposit("100")
    history = user.get_history()
    assert len(history) == 1


def test_withdrawal_records_in_history(user):
    user.deposit("100")
    user.withdrawal("40")
    history = user.get_history()
    assert len(history) == 2


def test_each_instance_has_own_history():
    """
    Checks the mutable default argument fix.
    Two separate accounts must not share the same history dict.
    """
    a = BankAccount("a", "A", "a", "a@a.com", "x")
    b = BankAccount("b", "B", "b", "b@b.com", "y")
    a.deposit("999")
    assert len(b.get_history()) == 0
