
class Customer:

    def __init__(self, name, phoneno):
        self.name = name
        self.phneno = phoneno

    def get_name(self):
        return self.name

    def get_phoneno(self):
        return self.phneno

    def set_phoneno(self, ph):
        self.phneno = ph


c1 = Customer('John', 7650984321)

print('Name:', c1.get_name())
print('Phone No:', c1.get_phoneno())

c1.set_phoneno(6789012345)

print('')
print('Name:', c1.get_name())
print('Phone No:', c1.get_phoneno())

