
from collections import Counter

inventory = Counter(apple=50, mango=100, banana=120, orange=70)


def update_inventory(order):
    inventory.subtract(order)


order = Counter(apple=10, banana=12, orange=5)
update_inventory(order)

print(inventory)



