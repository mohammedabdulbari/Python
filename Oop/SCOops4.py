
class Book:

    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def show_details(self):
        print('Title:',self.title)
        print('Author:', self.author)
        print('Price:', self.price)


b1 = Book('Python Crash Course', 'Eric Matthews', 1000)

b2 = Book('Learn Python', 'Mark Lutz', 500)

b1.show_details()
print('')
b2.show_details()


