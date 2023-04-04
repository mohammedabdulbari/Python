import time
from tkinter import *


def myclock():
    watch = time.strftime('%-I:%M:%S')
    lbl1['text']=watch
    lbl1.after(100, myclock)


win = Tk()
win.geometry('400x200')
win.title('My Clock')

lbl1 = Label(win, bg='#ff5555', font=('Times new roman', 40))
lbl1.pack(fill=BOTH, expand=True)

myclock()
win.mainloop()

