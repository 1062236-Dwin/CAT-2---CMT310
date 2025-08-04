class BankAccount:
    """A simple bank account class with deposit, withdraw, and balance check."""

    def __init__(self, balance=0):
        if balance < 0:
            raise ValueError("Initial balance cannot be negative.")
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be greater than zero.")
        self.balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be greater than zero.")
        if amount > self.balance:
            raise ValueError("Insufficient funds.")
        self.balance -= amount

    def get_balance(self):
        return self.balance
