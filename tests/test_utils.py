from account import BankAccount
from utils import check_float, check_amount, check_amountwithdrawal, hash_password


# --- check_float ---


def test_check_float_valid():
    assert check_float("3.14") is True


def test_check_float_integer_string():
    assert check_float("100") is True


def test_check_float_invalid():
    assert check_float("abc") is False


def test_check_float_empty():
    assert check_float("") is False


# --- check_amount ---


def test_check_amount_positive():
    assert check_amount("50") is True


def test_check_amount_zero():
    # 0 is allowed for deposits (current behaviour)
    assert check_amount("0") is True


def test_check_amount_negative():
    assert check_amount("-10") is False


def test_check_amount_invalid_string():
    assert check_amount("hello") is False


# --- check_amountwithdrawal ---


def make_user(balance: float) -> BankAccount:
    u = BankAccount("t", "T", "t", "t@t.com", "x")
    if balance > 0:
        u.deposit(str(balance))
    return u


def test_withdrawal_valid():
    assert check_amountwithdrawal("50", make_user(100)) is True


def test_withdrawal_exact_balance():
    assert check_amountwithdrawal("100", make_user(100)) is True


def test_withdrawal_over_balance():
    assert check_amountwithdrawal("200", make_user(100)) is False


def test_withdrawal_zero():
    # withdrawing 0 should be blocked (0 < amount condition)
    assert check_amountwithdrawal("0", make_user(100)) is False


def test_withdrawal_negative():
    assert check_amountwithdrawal("-10", make_user(100)) is False


def test_withdrawal_invalid_string():
    assert check_amountwithdrawal("abc", make_user(100)) is False


# --- hash_password ---


def test_hash_is_consistent():
    assert hash_password("secret") == hash_password("secret")


def test_different_passwords_give_different_hashes():
    assert hash_password("secret") != hash_password("other")


def test_hash_is_not_plaintext():
    assert hash_password("secret") != "secret"
