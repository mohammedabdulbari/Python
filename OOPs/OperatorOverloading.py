
class Rational:
    def __init__(self, p=1, q=1):
        self.p=p
        self.q=q

    def __add__(self, other):
        s = Rational()
        s.p = self.p * other.q + self.q * other.p
        s.q = self.q * other.q
        return s

    def __str__(self):
        return str(self.p) + '/' + str(self.q)



r1 = Rational(2,3)
r2 = Rational(2,5)

sum = r1+r2
print(sum)
