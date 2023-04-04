from tkinter import *


win = Tk()
win.geometry('600x400')

f1 = LabelFrame(win, text='Frame 1', bg='red', width=300)
f1.pack(side=LEFT, fill=Y)

f2 = LabelFrame(win, text='Frame 2', bg='green', width=300)
f2.pack(side=RIGHT, fill=Y)


b1 = Button(f1, text='Button 1')
b2 = Button(f1, text='Button 2')
b3 = Button(f1, text='Button 3')
b4 = Button(f1, text='Button 4')
b1.grid(row=0, column=0)
b2.grid(row=0, column=1)
b3.grid(row=1, column=0)
b4.grid(row=1, column=1)


b11 = Checkbutton(f2, text='Button 11')
b12 = Checkbutton(f2, text='Button 12')
b13 = Checkbutton(f2, text='Button 13')
b14 = Checkbutton(f2, text='Button 14')
b11.pack()
b12.pack()
b13.pack()
b14.pack()



win.mainloop()




















'''
f1 = LabelFrame(win, text='Buttons Frame', bg='red', width=300)
f1.pack(side=LEFT, fill=Y)
f2 = LabelFrame(win, text='Frame 2', bg='green', width=300)
f2.pack(side=RIGHT, fill=Y)

b1 = Button(f1, text='Button 1')
b2 = Button(f1, text='Button 2')
b3 = Button(f1, text='Button 3')
b4 = Button(f1, text='Button 4')
b1.grid(row=0, column=0)
b2.grid(row=0, column=1)
b3.grid(row=1, column=0)
b4.grid(row=1, column=1)

'''