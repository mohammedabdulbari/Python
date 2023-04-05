import random
from tkinter import *


def shuffle_list():
    random.shuffle(langs)
    lst1.delete(0, END)
    var1 = Variable(value=langs)
    lst1['listvariable']= var1


def show(e):
    lbl1['text']=lst1.get(lst1.curselection())


win = Tk()
win.geometry('400x300')

langs = ['C', 'C++', 'Java', 'Python', 'PHP', 'Swift']

var1 = Variable(value=langs)

lbl1 = Label(win, text='Select Item', font=('Ariel', 30), fg='yellow')
lbl1.pack()

lst1 = Listbox(win, listvariable=var1)
lst1.pack()
lst1.bind('<<ListboxSelect>>', show)

btn1 = Button(win, text='Shuffle', command=shuffle_list)
btn1.pack()

win.mainloop()
