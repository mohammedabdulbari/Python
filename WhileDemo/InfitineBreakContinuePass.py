count = 0

while count < 10:
    n = int(input('Enter a number'))
    if n % 3 != 0:
        print(n)
    count += 1

    if n % 3 == 0:
        pass
    else:
        print(n)

