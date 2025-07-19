def fib_term(n):
    a, b = 0, 1

    for i in range(n+1):
        yield a
        a, b = b, a + b


if __name__ == "__main__":

    num = 10

    for term in fib_term(num):
        print(term, end=', ')
