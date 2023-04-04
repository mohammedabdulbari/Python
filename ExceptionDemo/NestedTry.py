

try:
    a = int(input('Enter first number'))
    b = int(input('Enter second number'))
    c = a // b
    print(c)
except ZeroDivisionError as e:
    print(e)
except ValueError:
    print('Value Error Outer')
