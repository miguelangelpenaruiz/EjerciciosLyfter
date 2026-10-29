class BankAccount:
    balance = 0

    def deposit(self, amount):
        self.balance = self.balance + amount
        print(self.balance)

    def withdraw(self, amount):
        if (self.balance - amount) < 0:
            print('Not enough funds for the withdraw')
        else:
            self.balance = self.balance - amount
            print(f'Available funds: {self.balance}')

# Tests
nu = BankAccount()
nu.deposit(8)
nu.withdraw(8)
nu.withdraw(1001)

class SavingAccount(BankAccount):
    def __init__(self, min_balance):
        try:
            self.min_balance = float(min_balance)
            if self.min_balance < 0:
                raise ValueError
        except ValueError:
            print('The minimum balance must be a positive number')


