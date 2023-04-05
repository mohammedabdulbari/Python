
L1 = [10, 15, 6, 9, 12, 8, 4]

L2 = [14, 6, 19 , 4, 7, 10, 11]

L3 = []

for x in L1:
    if x in L2:
        L3.append(x)

print(L3)