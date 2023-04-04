
def sum0(L):

    s = 0

    for e in L:
        if e % 10 == 0:
            s += e
    return s


L = [100, 123, 200, 234, 350]

print(sum0(L))
