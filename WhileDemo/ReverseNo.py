n = int(input('Enter a Number'))

rev = 0

while n > 0:
    r = n % 10
    n = n // 10
    rev = rev * 10 + r

print('Reverse number is', rev)
print(n)
