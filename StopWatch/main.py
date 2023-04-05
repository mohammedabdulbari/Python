from tkinter import *

elapse_time = 0
flag = True

def start():
    global elapse_time, flag
    flag = True
    update_time()


def update_time():
    global elapse_time, flag
    if flag == True:
        elapse_time += 10
        milli = elapse_time % 1000
        sec = elapse_time // 1000
        min = sec // 60
        sec = sec % 60

        lbl1['text'] = f'{min:02d}:{sec:02d}:{milli:03d}'
        lbl1.after(10, update_time)


def stop():
    global flag
    flag = False

def reset():
    global elapse_time, flag
    elapse_time=0
    flag = False
    lbl1['text']='00:00:000'



win = Tk()
win.geometry('200x100')
win.title('Stop Watch')

lbl1 = Label(win, text='00:00:000', font=('Times new Roman', 45))
lbl1.grid(row=0, column=0, columnspan=3)

btn1 = Button(win, text='Start', command=start)
btn1.grid(row=1, column=0)

btn2 = Button(win, text='Stop', command=stop)
btn2.grid(row=1, column=1)

btn3 = Button(win, text='Reset', command=reset)
btn3.grid(row=1, column=2)


win.mainloop()
