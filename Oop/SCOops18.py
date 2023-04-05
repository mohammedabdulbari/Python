

class Computer:

    def __init__(self, name, make, os):
        self.name = name
        self.cpu = self.CPU(make)
        self.os = self.OS(os)

    def __str__(self):
        return 'Name: '+self.name + '\nMake: ' + self.cpu.get_make() + '\nOS Name: ' + self.os.get_name()

    class CPU:

        def __init__(self, make):
            self.make = make

        def get_make(self):
            return self.make

    class OS:

        def __init__(self, os):
            self.name = os

        def get_name(self):
            return self.name


c1 = Computer('PC101', 'Intel', 'Windows')
print(c1)