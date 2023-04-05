
class Rectangle:
    data='hi'
    @classmethod
    def show(cls):
        cls.dat=10
        print(cls.dat)
        Rectangle.data = 'bye'

Rectangle.my='hello'

r = Rectangle()
r.show()
r1 = Rectangle()
r1.show()
Rectangle.show()
print(dir(r1))
print(Rectangle.dat,Rectangle.data,Rectangle.my)
