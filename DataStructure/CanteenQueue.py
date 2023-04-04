
from collections import deque

students = deque([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])


def serve_food():
    print('Students are Served in Order:', students)
    students.rotate(-1)


print('Breakfast')
serve_food()
print('Lunch')
serve_food()
print('Dinner')
serve_food()

