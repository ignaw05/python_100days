from tkinter import *

def button_clicked():
    mile = int(entry1.get())
    mile *= 1.609
    text4.configure(text=f"{mile}")

root = Tk()
root.title("Mile to Km Converter")
root.minsize(width=300,height=100)

entry1 = Entry()
entry1.configure(width=20)
entry1.grid(column=1,row=0)

label1 = Label(text="Miles")
label1.grid(column=2,row=0)

button1 = Button(text="Calculate", command=button_clicked)
button1.grid(column=1,row=2)

text2 = Label(text="is equal to")
text2.grid(column=0,row=1)

text3 = Label(text="Km")
text3.grid(column=2,row=1)

text4 = Label(text=0)
text4.grid(column=1,row=1)



root.mainloop()

# def add(*args):
#     total = 0
#     for n in args:
#         total += n
#     return total
#
# def calculate(**kwargs):
#     n = 0
#     n += kwargs["add"]
#     n *= kwargs["mult"]
#     return n

