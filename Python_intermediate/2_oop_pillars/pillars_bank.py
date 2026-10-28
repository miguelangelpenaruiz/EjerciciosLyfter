class BankAccount:
    def __init__(self, balance):
        try:
            self.balance = float(balance)
        except ValueError:
            raise ValueError('Balance must be a number')

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
nu = BankAccount(1000)
nu.deposit(8)
nu.withdraw(8)
nu.withdraw(1001)

class SavingAccount(BankAccount):
    def __init__(self, balance):
        super().__init__(balance)

