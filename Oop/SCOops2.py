import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius * self.radius

    def perimeter(self):
        return 2 * math.pi * self.radius
    

c1 = Circle(7)
print('Area:',c1.area())
print('Perimeter:',c1.perimeter())
