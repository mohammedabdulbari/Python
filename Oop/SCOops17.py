
class CurrencyConverter:

    def __init__(self, name, rate):
        self.currency = name
        self.rate = rate

    def get_currency(self):
        return self.currency

    def get_rate(self):
        return self.rate

    def set_currency(self, name):
        self.currency = name

    def set_rate(self, rate):
        self.rate = rate

    def convert(self, amount):
        return self.currency + ' conversion is ' + str(self.rate * amount)


cc = CurrencyConverter('USD', 70)
print(cc.convert(100))

cc.set_currency('AUD')
cc.set_rate(50)

print(cc.convert(100))

