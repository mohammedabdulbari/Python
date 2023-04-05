
class Rectangle:
    def __init__(self, l, b):
        self.length=l
        self.breadth=b

    def getLength(self):
        return self.length

    def setLength(self, l):
        self.length=l
    def area(self):
        return self.length * self.breadth
    def perimeter(self):
        return 2*(self.length+self.breadth)

r = Rectangle(10,5)
print(r.getLength())
r.setLength(15)
print(r.area())

