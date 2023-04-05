
cardno = input('Enter Card No')

lastDigits = cardno[15::]

four = '*' * 4 + ' '

dispno = four * 3 + lastDigits

print(dispno)