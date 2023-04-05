
class Arith:
    def sum(self, a, b, c=None):
        s = a + b
        if c==None:
            return s
        else:
            return s + c


a = Arith()
print(a.sum(5,10,3))

print(a.sum(8, 9))

