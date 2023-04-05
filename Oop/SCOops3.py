class MinimumBalanceError(Exception):
    pass

class Account:
    AccNumber = 1001

    def __init__(self, name, balance=1000):

        if balance < 1000:
            raise MinimumBalanceError('Account Cannot be Created')
        self.name = name
        self.balance = balance
        self.account_number = Account.AccNumber
        Account.AccNumber += 1

    def deposit(self, amt):
        self.balance += amt

    def withdraw(self, amt):
        if self.balance - amt < 1000:
            raise MinimumBalanceError('Amount cannot be withdrawn')
        self.balance -= amt

    def show_details(self):
        print('Account Number',self.account_number)
        print('Name',self.name)
        print('Balance',self.balance)


a1 = Account('John', 2000)
a1.withdraw(1500)
a1.show_details()


