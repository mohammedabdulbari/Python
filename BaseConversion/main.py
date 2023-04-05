from tkinter import *
from tkinter.font import *


def update_label():
    if base_type.get() == 0:
        lbl1['text']=str(value)
    elif base_type.get() == 1:
        lbl1['text'] = str(bin(value))
    elif base_type.get() == 2:
        lbl1['text'] = str(oct(value))
    elif base_type.get() == 3:
        lbl1['text'] = str(hex(value))


win = Tk()
win.geometry('400x100')

fnt = Font(size=15)

value = 35

lbl1 = Label(win, text=str(value), font=('Times New Roman', 45), fg='yellow')
lbl1.grid(row=0, column=0, columnspan=4)

base_type=IntVar(value=0)

rbn1 = Radiobutton(win, text='Decimal', font=fnt, variable=base_type, value=0, command=update_label)
rbn1.grid(row=1, column=0)

rbn2 = Radiobutton(win, text='Binary', font=fnt, variable=base_type, value=1, command=update_label)
rbn2.grid(row=1, column=1)

rbn3 = Radiobutton(win, text='Octal', font=fnt, variable=base_type, value=2, command=update_label)
rbn3.grid(row=1, column=2)

rbn4 = Radiobutton(win, text='Hexa Decimal', font=fnt, variable=base_type, value=3, command=update_label)
rbn4.grid(row=1, column=3)

win.mainloop()
