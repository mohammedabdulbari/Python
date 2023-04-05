
class Angle:

    def __init__(self, deg):
        self.degree = deg

    def __add__(self, ang):
        sum = Angle(self.degree + ang.degree)
        return sum

    def __str__(self):
        return 'Degree ' + str(self.degree)


a1 = Angle(30)
a2 = Angle(45)

a3 = a1 + a2

print(a3)