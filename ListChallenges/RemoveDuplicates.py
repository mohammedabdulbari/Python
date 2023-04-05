
L1 = [3, 5, 7, 9, 3, 6, 5, 2, 3, 7, 10]

L2 = []

for x in L1:
    if x not in L2:
        L2.append(x)

print(L2)
