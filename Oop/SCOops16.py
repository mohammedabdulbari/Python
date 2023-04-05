
class English:

    def greeting(self):
        print('Hello')


class French:

    def greeting(self):
        print('Bonjour')


def greet(language):
    language.greeting()


e = English()
greet(e)

print('')

f= French()
greet(f)
