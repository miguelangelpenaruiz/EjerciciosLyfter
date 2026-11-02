class BankAccount:
    def __init__(self):
        self._balance = 0
    @property
    def balance(self):
        return self._balance

    def deposit(self, amount):
        if amount < 0:
            raise ValueError("You can not deposit a negative number")
        self._balance = self._balance + amount
        print(self._balance)

    def withdraw(self, amount):
        if amount < 0:
            raise ValueError("Do not enter a negative number for the withdraw")
        elif (self._balance - amount) < 0:
            raise ValueError('Not enough funds for the withdraw')
        self._balance = self._balance - amount
        print(f'Available funds: {self._balance}')

# Tests
account = BankAccount()
account.deposit(100)        # balance: 100
account.withdraw(30)        # balance: 70
account.withdraw(500)       # Error not enough funds
account.deposit(-50)        # Error
account.withdraw(-20)       # Error
try:
    account.balance = 999
except AttributeError as error:
    print(f"Error: {error}")
print(account.balance)  # 70

class SavingsAccount(BankAccount):
    def __init__(self, min_balance):
        super().__init__()
        self.min_balance = float(min_balance)
        if self.min_balance < 0:
            raise ValueError('The minimum balance must be a positive number')

    def withdraw(self, amount):
        if amount < 0:
            raise ValueError("Do not enter a negative number for the withdraw")
        elif (self._balance - amount) < 0:
            raise ValueError('Not enough funds for the withdraw')
        elif self._balance - amount < self.min_balance:
            raise ValueError(f"You cannot do a withdraw because your minimum balance is {self.min_balance}")
        self._balance = self._balance - amount
        print(f'Available funds: {self._balance}')

