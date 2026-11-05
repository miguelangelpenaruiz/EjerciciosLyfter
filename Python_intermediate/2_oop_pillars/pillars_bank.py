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
try:
    account.withdraw(500)       # Error not enough funds
except ValueError as error:
    print(f"Error: {error}")
try:
    account.deposit(-50)        # Error
except ValueError as error:
    print(f"Error: {error}")
try:
    account.withdraw(-20)       # Error
except ValueError as error:
    print(f"Error: {error}")
try:
    account.balance = 999       # Error
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
        if self._balance - amount < self.min_balance:
            raise ValueError(f"You cannot do a withdraw because your minimum balance is {self.min_balance}")
        super().withdraw(amount)

basic_ppr = SavingsAccount(1000)

basic_ppr.deposit(2000)

try:
    basic_ppr.withdraw(1500)        # Error
except ValueError as error:
    print(f"Error: {error}")

basic_ppr.withdraw(1000)
