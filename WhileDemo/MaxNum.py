num_of_nos = int(input('Enter number of number'))

count = 0

max = int(input('Enter a num'))

while count < num_of_nos - 1:
    n = int(input('Enter a number'))
    if n > max:
        max = n
    count = count + 1

print('Max number is', max)
