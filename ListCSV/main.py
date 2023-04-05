from tkinter import *
import csv


def show_data(e):
    i = headings.index(var1.get())
    col = [row[i] for row in data]
    lst1.delete(0, END)
    lst1['listvariable'] = Variable(value=col)


win = Tk()
win.geometry('400x300')

file_csv = open('Employees.csv', 'r')
reader = csv.reader(file_csv)

headings = next(reader)
data = []
for t in reader:
    data.append(t)

var1 = StringVar(value=headings[0])
opt1 = OptionMenu(win, var1, *headings, command=show_data)
opt1.pack()

eids = [row[0] for row in data]

lstvar1 = Variable(value=eids)
lst1 = Listbox(win, listvariable=lstvar1)
lst1.pack()

win.mainloop()
