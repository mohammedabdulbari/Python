
roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

number = input('Enter roman number in upper cases')

deci_num = 0

i= 0

while i < len(number):
    if i+1 < len(number) and roman[number[i]] < roman[number[i+1]]:
        deci_num += roman[number[i+1]] - roman[number[i]]
        i += 2
    else:
        deci_num += roman[number[i]]
        i += 1


print(deci_num)