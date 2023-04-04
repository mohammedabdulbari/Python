a = int(input('Enter initial term'))
d = int(input('Enter common Difference'))
n = int(input('Enter Number of Terms'))

for t in range(a, a + n * d, d):
    print(t)