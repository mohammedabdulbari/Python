class Cuboid:
    def __init__(self, l=1, b=1, h=1):
        print(id(self))
        self.length = l
        self.breadth = b
        self.height = h

    def lidarea(self):
        return self.length * self.breadth

    def total(self):
        return 2 * (self.length * self.breadth + self.breadth * self.height + self.length * self.height)

    def volume(self):
        print(id(self))
        return self.length * self.breadth * self.height


c1 = Cuboid()
c2 = Cuboid(10)
c3 = Cuboid(10, 5)
c4 = Cuboid(10, 5, 3)





c1 = Cuboid(10, 5, 3)
print(id(c1))
c1.volume()

c2 = Cuboid(20, 15, 10)
print(id(c2))
c2.volume()