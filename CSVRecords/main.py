from tkinter import *
from tkinter.font import *
import csv


def show_data(e):
    i = enames.index(var1.get())
    id_var.set(data[i][0])
    name_var.set(data[i][1])
    sal_var.set(data[i][2])


def update():
    i = enames.index(var1.get())
    data[i][0] = id_var.get()
    data[i][1] = name_var.get()
    data[i][2] = sal_var.get()


def save():
    file_csv.close()
    write_csv = open('Employees.csv', 'w', newline='')
    wrtr = csv.writer(write_csv)
    wrtr.writerow(headings)
    wrtr.writerows(data)
    write_csv.close()
    win.quit()


win = Tk()
win.geometry('800x250')
fnt = Font(family='Times new Roman', size=25)

file_csv = open('Employees.csv', 'r')
reader = csv.reader(file_csv)

headings = next(reader)
data = [row for row in reader]

enames = [row[1] for row in data]

var1 = StringVar(value=enames[0])
opt1 = OptionMenu(win, var1, *enames, command=show_data)

lst_label = Label(win, text='Employee List', font=fnt)
id_label = Label(win, text='Employee ID', font=fnt)
name_label = Label(win, text='Name', font=fnt)
sal_label = Label(win, text='Salary', font=fnt)

id_var = StringVar()
name_var = StringVar()
sal_var = StringVar()

id_entry = Entry(win, textvariable=id_var, font=fnt)
name_entry = Entry(win, textvariable=name_var, font=fnt)
sal_entry = Entry(win, textvariable=sal_var, font=fnt)

update_button = Button(win, text='Update', command=update, font=fnt)
save_button = Button(win, text='Save & Exit', command=save, font=fnt)

lst_label.grid(row=0, column=0)
opt1.grid(row=0, column=1)
id_label.grid(row=1, column=0)
id_entry.grid(row=1, column=1)
name_label.grid(row=1, column=2)
name_entry.grid(row=1, column=3)
sal_label.grid(row=2, column=0)
sal_entry.grid(row=2, column=1)
update_button.grid(row=3, column=0, columnspan=2)
save_button.grid(row=3, column=2, columnspan=2)


win.mainloop()
