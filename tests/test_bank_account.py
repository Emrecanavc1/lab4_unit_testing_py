import pytest
from src.bank_account import BankAccount

def test_deposit():
    acc = BankAccount()
    acc.deposit(100)
    assert acc.balance == 100

def test_withdraw():
    acc = BankAccount(200)
    acc.withdraw(50)
    assert acc.balance == 150

def test_withdraw_insufficient_funds():
    acc = BankAccount()
    with pytest.raises(ValueError, match="Insufficient funds"):
        acc.withdraw(100)

def test_transfer():
    acc1 = BankAccount(300)
    acc2 = BankAccount(100)
    acc1.transfer_to(acc2, 150)
    assert acc1.balance == 150
    assert acc2.balance == 250
