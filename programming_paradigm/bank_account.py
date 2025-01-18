class BankAccount:
    def __init__(self, initial_balance=0):
        """
        Initialize the bank account with an optional initial balance.
        :param initial_balance: Starting balance, defaults to 0.
        """
        self.__account_balance = initial_balance

    def deposit(self, amount):
        """
        Deposit a specified amount into the account.
        :param amount: Amount to be deposited.
        """
        if amount > 0:
            self.__account_balance += amount

    def withdraw(self, amount):
        """
        Withdraw a specified amount from the account if sufficient funds exist.
        :param amount: Amount to be withdrawn.
        :return: True if withdrawal is successful, False otherwise.
        """
        if 0 < amount <= self.__account_balance:
            self.__account_balance -= amount
            return True
        return False

    def display_balance(self):
        """
        Display the current account balance.
        """
        print(f"Current Balance: ${self.__account_balance:.2f}")