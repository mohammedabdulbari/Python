
def invert(d):

    newd = {}
    for k, v in d.items():
        newd[v]=k

    return newd


d1 = {'a':10, 'b':20, 'c':30, 'd':40}

d2 = invert(d1)

print(d2)
