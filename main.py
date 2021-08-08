import tkinter
from tkinter import *
window = Tk()
window.minsize(width=300, height=200)
window.config(padx=20, pady=50)
window.title("Welcome to my unit converter")

def conversion():
    converted_num = float(text_input.get()) * 1.6
    num_coverted.config(text=int(converted_num))

#Miles Label
miles = Label(text="Miles")
miles.grid(column=2, row=0)

#Num converted
num_coverted = Label()
num_coverted.grid(column=1, row=1)

#Km Kabel
km = Label(text="Km")
km.grid(column=2, row=1)

#is_equal_to Label
is_equal_to = Label(text="is equal to")
is_equal_to.grid(column=0, row=1)

#input box
text_input = Entry(width=10)
text_input.grid(column=1, row=0)

#calculate button
calculate = Button(text="Calculate", command=conversion)
calculate.grid(column=1, row=2)

window.mainloop()

