from tkinter import *
import pandas as pd
def show():
    df = pd.read_csv("C:\kolosyPython\movies.csv")
    budget_col = df[df["budget"] < float(budget.get())]

    mini = df[df["budget"] < 1000]
    mina = mini["movie_title"].values[0]

    tekst2.config(text=f"ilosc budzetow ponizej podanej kwoty to {len(budget_col)}, {mina}")


root = Tk()
root.title("Interface")
root.geometry("400x500")

tekst1 = Label(root, text="Podaj budżet filmu: ")
tekst1.grid(row=0, column=0)

budget = Entry(root)
budget.grid(row=0, column=1)

ok_button = Button(root, text="OK", fg="green", command=show)
ok_button.grid(row=1, column=0)

tekst2 = Label(root, text="ilosc budzetow ponizej podanej kwoty to ")
tekst2.grid(row=2, column=0)

root.mainloop()

