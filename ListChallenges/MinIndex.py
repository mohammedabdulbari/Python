
L1 = ['pizza', 'nuggets', 'hotdog', 'noodles', 'pasta', 'burger']

L2 = ['burger', 'hotdog', 'noodles', 'pasta', 'nuggets', 'pizza']

index1 = 10
index2 = 10

for i in range(len(L1)):
    indx = L2.index(L1[i])

    if i + indx < index1 + index2:
        index1 = i
        index2 =indx

print(L1[index1],index1+index2)

