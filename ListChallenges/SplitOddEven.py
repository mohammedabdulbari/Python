
nums = [4, 8, 3, 5, 10, 7, 2, 9, 13, 6]

odd = [x for x in nums if x % 2 != 0]

even = [x for x in nums if x % 2 == 0]

print('Odd:', odd)

print('Even:', even)
