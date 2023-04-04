from tkinter import *
from tkinter.font import *


def update_label():
    b = ['bold' if varbold.get() == 1 else 'normal'][0]
    i = ['italic' if varitalic.get() == 1 else 'roman'][0]
    fnt = Font(family='Times new Roman', size=45, weight=b, slant=i, underline=varunderline.get())
    lbl1['font'] = fnt


win = Tk()
win.geometry('400x300')

lbl1 = Label(win, text='Hello World', font=('Times new Roman', 45))
lbl1.grid(row=0, column=0, columnspan=3)

varbold = IntVar(value=0)
chk1 = Checkbutton(win, text='Bold', onvalue=1, offvalue=0, variable=varbold, command=update_label)
chk1.grid(row=1, column=0)

varitalic = IntVar(value=0)
chk2 = Checkbutton(win, text='Italic', onvalue=1, offvalue=0, variable=varitalic, command=update_label)
chk2.grid(row=1, column=1)

varunderline = IntVar(value=0)
chk3 = Checkbutton(win, text='Underline', onvalue=1, offvalue=0, variable=varunderline, command=update_label)
chk3.grid(row=1, column=2)

win.mainloop()
