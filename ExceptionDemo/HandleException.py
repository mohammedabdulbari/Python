def div(a,b):
    if b == 0:
        raise ZeroDivisionError
    c= a // b
    return c

def helpDiv(a,b):
    try:
        c=div(a,b)
        return c
    except:
        pass
    finally:
        print('End of helpDiv')
x = 10
y = 0

try:
    z = helpDiv(x,y)
except:
    print('Error')
else:
    print(z)

