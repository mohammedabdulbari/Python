class Test:
    def __init__(s):
        s.a=10

    def fun(s):
        s.b=20


t1=Test()
t1.fun()
t1.c=30

print(dir(t1))