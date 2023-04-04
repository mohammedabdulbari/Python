from tkinter import *


def change_color(e):
    r = red_var.get()
    g = green_var.get()
    b = blue_var.get()
    color_lbl['bg'] = f'#{r:02x}{g:02x}{b:02x}'


win = Tk()
win.geometry('300x200')

color_lbl = Label(win, text='', bg='black', width=30)
color_lbl.grid(row=0, column=0, columnspan=2)

red_lbl = Label(win, text='Red')
green_lbl = Label(win, text='Green')
blue_lbl = Label(win, text='Blue')

red_lbl.grid(row=1, column=0)
green_lbl.grid(row=2, column=0)
blue_lbl.grid(row=3, column=0)

red_var = IntVar(value=0)
green_var = IntVar(value=0)
blue_var = IntVar(value=0)

red_scale = Scale(win, orient=HORIZONTAL, variable=red_var, from_=0, to=255, command=change_color)
green_scale = Scale(win, orient=HORIZONTAL, variable=green_var, from_=0, to=255, command=change_color)
blue_scale = Scale(win, orient=HORIZONTAL, variable=blue_var, from_=0, to=255, command=change_color)

red_scale.grid(row=1, column=1)
green_scale.grid(row=2, column=1)
blue_scale.grid(row=3, column=1)

win.mainloop()
