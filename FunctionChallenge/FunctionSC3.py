

def count(phrase):
    lower = 0
    upper = 0

    for l in phrase:
        if l.islower():
            lower += 1
        elif l.isupper():
            upper = upper + 1
    return lower, upper


print(count('ABCI'))

