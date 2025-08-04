import pytest
from banking.BankAccount import BankAccount  # Correct based on your file name

@pytest.fixture
def account():
    """Fixture with an initial balance of 100."""
    return BankAccount(100)

def test_default_initial_balance():
    acc = BankAccount()
    assert acc.get_balance() == 0

def test_custom_initial_balance():
    acc = BankAccount(200)
    assert acc.get_balance() == 200

def test_negative_initial_balance_raises_error():
    with pytest.raises(ValueError):
        BankAccount(-50)

def test_deposit_valid_amount(account):
    account.deposit(50)
    assert account.get_balance() == 150

def test_deposit_zero_raises_error(account):
    with pytest.raises(ValueError):
        account.deposit(0)

def test_deposit_negative_raises_error(account):
    with pytest.raises(ValueError):
        account.deposit(-10)

def test_withdraw_valid_amount(account):
    account.withdraw(60)
    assert account.get_balance() == 40

def test_withdraw_zero_raises_error(account):
    with pytest.raises(ValueError):
        account.withdraw(0)

def test_withdraw_negative_raises_error(account):
    with pytest.raises(ValueError):
        account.withdraw(-20)

def test_withdraw_more_than_balance_raises_error(account):
    with pytest.raises(ValueError):
        account.withdraw(150)

def test_get_balance(account):
    assert account.get_balance() == 100
