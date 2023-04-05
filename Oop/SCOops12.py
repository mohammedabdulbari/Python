
class Cat:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print('My name is ' + self.name + '. My age is ' + str(self.age))

    def make_sound(self):
        print('mew mew')


class Dog:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print('My name is ' + self.name + '. My age is ' + str(self.age))

    def make_sound(self):
        print('bow wow')



def my_pet(pet):
    pet.info()
    pet.make_sound()


c = Cat('Kitty', 2)
d = Dog('Tommy', 3)

my_pet(d)
