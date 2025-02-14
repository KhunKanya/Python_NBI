from bank_account import BankAccount
import pytest


def test_deposit():
    account = BankAccount(100)
    account.deposit(50)
    assert account.get_balance() == 150, f"Expected balance to be 150, but got {account.get_balance()}"


def test_withdraw():
    account = BankAccount(100)
    account.withdraw(30)
    assert account.get_balance() == 70, f"Expected balance to be 70, but got {account.get_balance()}"


def test_get_balance():
    account = BankAccount(100)
    assert account.get_balance() == 100, f"Expected balance to be 100, but got {account.get_balance()}"


def test_apply_interest():
    account = BankAccount(100)
    account.apply_interest()
    assert account.get_balance() == 101, f"Expected balance to be 101, but got {account.get_balance()}"


def test_can_pay_bill():
    account = BankAccount(100)
    assert account.can_pay_bill(50) == True, f"Expected True, but got {account.can_pay_bill(50)}"
    assert account.can_pay_bill(150) == False, f"Expected False, but got {account.can_pay_bill(150)}"


def test_deposit_negative_amount():
    account = BankAccount(100)
    with pytest.raises(ValueError):
        account.deposit(-50)


def test_withdraw_too_much():
    account = BankAccount(100)
    with pytest.raises(ValueError, match="Insufficient funds"):
        account.withdraw(150)
