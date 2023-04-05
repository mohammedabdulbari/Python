
class Robot:

    def __init__(self, name):
        self.name = name

    def say_hi(self):
        print('Hi, I am '+self.name)


class PoliceRobot(Robot):

    def say_hi(self):
        print('Hi, this is '+self.name+'. I am here to help you')


r1 = PoliceRobot('RoboCop')
r1.say_hi()