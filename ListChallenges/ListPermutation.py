
import itertools as it

lst = ['A', 'B', 'C', 'D']

perms = it.permutations(lst, r=2)

perm_list = list(perms)

print('Permutations')

for t in perm_list:
    print(t)
    
