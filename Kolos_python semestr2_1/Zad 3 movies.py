import pandas as pd
from tkinter import *
import pickle

def show():
    tytul_u = tytul.get()
    df = pd.read_csv("C:\kolosyPython\movies.csv", index_col=False)
    movie = df[df["movie_title"] == tytul_u]

    budget = movie["budget"].values[0]
    napis_show1.config(text=f"Budżet: {budget}")

    director = movie["director_name"].values[0]
    napis_show2.config(text=f"Reżyser: {director}")



def zapis_do_pikla():
    path = "C:\kolosyPython\Kolos_python semestr2_1" + "\dane_filmow.pickle"

    tytul_u = tytul.get()
    df = pd.read_csv("C:\kolosyPython\movies.csv", index_col=False)
    movie = df[df["movie_title"] == tytul_u]
    budget = movie["budget"].values[0]
    director = movie["director_name"].values[0]

    with open(path, "wb") as file:
        pickle.dump(f"Tytuł: {tytul_u}\nBudżet: {budget}\nReżyser: {director}\n\n", file)
        napis3.config(text=f"Zapis przeszedł pomyślnie")


root = Tk()
root.title("Interfejs")
root.geometry("500x500")

napis_tytul = Label(root, text="Podaj tytul filmu:")
napis_tytul.grid(row=0, column=0)

tytul = Entry(root, fg="pink")
tytul.grid(row=1, column=0)

ok = Button(root, text="OK", bg="yellow", command=show)
ok.grid(row=2, column=0)

napis_show1 = Label(root, text="budżet: ")
napis_show1.grid(row=3, column=0)

napis_show2 = Label(root, text="reżyser: ")
napis_show2.grid(row=4, column=0)

zapisz = Button(root, text="Zapisz", bg="yellow", command=zapis_do_pikla)
zapisz.grid(row=5, column=0)

napis3 = Label(root, text="")
napis3.grid(row=6, column=0)
root.mainloop()
