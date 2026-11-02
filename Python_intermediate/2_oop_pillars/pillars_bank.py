class BankAccount:
    def __init__(self):
        self._balance = 0
    @property
    def balance(self):
        return self._balance

    def deposit(self, amount):
        if amount < 0:
            print("You can not deposit a negative number")
        else:
            self._balance = self._balance + amount
            print(self._balance)

    def withdraw(self, amount):
        if amount < 0:
            print("Do not enter a negative number for the withdraw")
        elif (self._balance - amount) < 0:
            print('Not enough funds for the withdraw')
        else:
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

class SavingAccount(BankAccount):
    def __init__(self, min_balance):
        try:
            self.min_balance = float(min_balance)
            if self.min_balance < 0:
                raise ValueError
        except ValueError:
            print('The minimum balance must be a positive number')


