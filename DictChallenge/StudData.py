
Students = {}

for i in range(3):
    name = input('Enter name')
    roll = int(input('Enter Roll'))
    dept = input('Enter Dept')

    Students[name]={'Roll':roll,'Name':name,'Dept':dept}


print(Students)

