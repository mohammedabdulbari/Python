from tkinter import *
from PIL import Image, ImageTk

win = Tk()
win.geometry('600x400')

can1 = Canvas(win, width=600, height=400, bg='yellow')
can1.pack()

can1.create_arc(100, 100, 200, 200, fill='red', outline='black', width=10, start=90, extent=45)

img1 = ImageTk.PhotoImage(Image.open("test.png"))
can1.create_image(10,10, image=img1, anchor=NW)

btn1 = Button(win, text='Click Me')

can1.create_window(200, 200, window=btn1)

win.mainloop()
