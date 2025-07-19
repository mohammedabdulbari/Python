
lst = [1, 2, 3, 4, 5, 6]

n = int(input('Enter Number of Rotations:'))

rotated = lst[n:] + lst[:n]

print('Rotated List:', rotated)
