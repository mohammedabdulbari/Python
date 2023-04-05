
class Calculator:

    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def sub(a, b):
        return a - b

    @staticmethod
    def mul(a, b):
        return a * b

    @staticmethod
    def div(a, b):
        return a / b


x = 10
y = 3

print(Calculator.add(x,y))
print(Calculator.div(x,y))

