
n = int(input('Enter a Number'))
counter = 0

while n > 0:
    n = n // 10
    counter += 1

print('Number of Digits are', counter)
