from tkinter import *


def myhandler(txt):
    if txt.isalpha():
        return False
    else:
        return True



win = Tk()
win.geometry('600x400')

handl = (win.register(myhandler), '%S')

var1 = StringVar(value='1234')
ent1 = Entry(win, textvariable=var1, validate='key', validatecommand=handl)
ent1.pack()


win.mainloop()