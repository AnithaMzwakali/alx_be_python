# programming_paradigm/bank_account.py

class BankAccount:
    """Simple bank account with deposit, withdraw and display operations."""

    def __init__(self, initial_balance=0.0):
        """Initialize account with an optional starting balance."""
        self.__account_balance = float(initial_balance)

    @property
    def balance(self):
        """Read-only access to the current balance (useful for testing)."""
        return self.__account_balance

    def deposit(self, amount):
        """Add amount to the account. Raises ValueError for non-positive amounts."""
        amount = float(amount)
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.__account_balance += amount

    def withdraw(self, amount):
        """
        Try to withdraw amount.
        - Raises ValueError for non-positive amounts.
        - Returns True and deducts the amount if sufficient funds.
        - Returns False and leaves balance unchanged if insufficient funds.
        """
        amount = float(amount)
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if self.__account_balance >= amount:
            self.__account_balance -= amount
            return True
        return False

    def display_balance(self):
        """Print the current balance in a user-friendly format."""
        print(f"Current Balance: ${self.__account_balance:.2f}")
