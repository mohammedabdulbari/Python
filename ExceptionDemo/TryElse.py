


def div(a,b):
    try:
        c = a // b
        return c
    except ZeroDivisionError as err:
        raise ZeroDivisionError
    finally:
        print('finally block')

z=div(10,0)
print(z)


