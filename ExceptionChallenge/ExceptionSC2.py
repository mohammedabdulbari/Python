
class AccountBalanceException(Exception):
    pass

balance = 10000

def withdraw(amt):
    global balance

    if balance - amt < 5000:
        raise AccountBalanceException('Minimum Balace should be 5000')
    else:
        balance = balance - amt
        print('Remaining balance is',balance)


try:
    withdraw(6000)
except AccountBalanceException as e:
    print(e)