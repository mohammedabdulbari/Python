

food = ['pizza', 'nuggets', 'hotdog', 'noodles', 'pasta', 'burger']

letter = input('Enter a Letter')

for x in food:
    if x.startswith(letter):
        print(x)

