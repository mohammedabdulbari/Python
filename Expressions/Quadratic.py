import math

a = int(input('Enter a value'))
b = int(input('Enter b value'))
c = int(input('Enter c value'))
root1 = (-b + math.sqrt(b**2 - 4 * a * c))/(2 * a)
root2 = (-b - math.sqrt(b**2 - 4 * a * c))/(2 * a)
print('Roots are ', root1, root2)
