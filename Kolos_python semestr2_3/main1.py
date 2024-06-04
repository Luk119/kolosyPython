from tkinter import *
from tkinter import messagebox


def show():
    if var.get() == 1:
        messagebox.showinfo("Info", "Info i ch")
    else:
        messagebox.showwarning("Error", "error i ch")

root = Tk()
root.title("interface")
root.geometry("600x600")

var = IntVar(value=0)

var2 = IntVar(value=0)
var3 = IntVar(value=0)

suwak = Scale(root, from_=0, to=10, orient=HORIZONTAL)

rb = Radiobutton(root, text="1", variable=var, value=1)
rb.grid(row=2, column=0)

rb2 = Radiobutton(root, text="1", variable=var, value=2)
rb2.grid(row=2, column=1)

cb = Checkbutton(root, variable=var2)
cb.grid(row=0, column=0)

cb2 = Checkbutton(root, variable=var3)
cb2.grid(row=0, column=1)

ok = Button(root, text="OK", command=show).grid(row=3, column=0)
root.mainloop()