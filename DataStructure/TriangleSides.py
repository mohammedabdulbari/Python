
import math

angle = int(input('Enter Angle'))
hyp = int(input('Enter Hypotenuse'))

angle = math.radians(angle)

opp = math.sin(angle) * hyp
adj = math.cos(angle) * hyp

print('Opposite', opp)
print('Adjacent', adj)
