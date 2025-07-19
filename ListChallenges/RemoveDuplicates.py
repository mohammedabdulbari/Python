
L1 = [3, 5, 7, 9, 3, 6, 5, 2, 3, 7, 10]

res = []

for element in L1:
    if element not in res:
        res.append(element)

print(res)
