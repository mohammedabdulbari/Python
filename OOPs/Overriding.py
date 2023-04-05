
class iPhone6:
    def home(self):
        print('home button is pressed')


class iPhoneX(iPhone6):
    def home(self):
        print('home is touched')
        super().home()


i6 = iPhone6()
i6.home()

ix = iPhoneX()
ix.home()


