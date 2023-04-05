from abc import ABC, abstractmethod

class Parent(ABC):
    @abstractmethod
    def show(self):
        pass

    def display(self):
        print('Parent Display')



class Child(Parent):
    def show(self):
        print('Show from Child')


c = Child()
c.show()
c.display()
