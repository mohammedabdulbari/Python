from tkinter import *


def change(e):
    lstvar = Variable(value=dict1[var1.get()])
    lst1.delete(0, END)
    lst1['listvariable'] = lstvar


win = Tk()
win.geometry('400x300')

dict1 = {'Languages': ['C', 'C++', 'Java'],
         'Databases': ['Oracle', 'SQL Server', 'mysql', 'Mango DB'],
         'Clouds': ['AWS', 'SalesForce', 'MS Asure']}

var1 = StringVar(value='Languages')

opt1 = OptionMenu(win,  var1, *dict1.keys(), command=change)
opt1['fg'] = 'blue'

opt1.pack()

lstvar1 = Variable(value=dict1['Languages'])

lst1 = Listbox(win, listvariable=lstvar1)
lst1.pack()

win.mainloop()
