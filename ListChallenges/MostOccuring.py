
L1 = ['A', 'B', 'C', 'D', 'E', 'A', 'B', 'C', 'A', 'B', 'A']

result = []

for x in L1:
    cnt = L1.count(x)

    if (x, cnt) not in result:
        result.append((x,cnt))

print(result[0:2])