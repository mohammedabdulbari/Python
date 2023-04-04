
def planet(id):
    planets = {1:'Mercury', 2:'Venus', 3:'Earth', 4:'Mars', 5:'Jupiter', 6:'Saturn', 7:'Uranus', 8:'Neptune', 9:'Pluto'}
    return planets[id]



id = int(input('Enter Planet ID'))
p = planet(id)
print('Planet Name is:',p)

