import pandas as pd
from tkinter import *
import os


def show():
    df = pd.read_csv("C:\kolosyPython\movies.csv")
    title = tytul.get()
    movie = df[df["movie_title"] == title]
    budget = movie["budget"].values[0]
    director = movie["director_name"].values[0]

    napis2.config(text=f"budżet: {budget}")
    napis3.config(text=f"reżyser: {director}")


def zapisz():
    """
    Function zapisz takes budget and director from movie.csv and
    saves values: budget(float) and director(str) to the txt file

    Args: None
    Returns: Nothing

    """
    df = pd.read_csv("C:\kolosyPython\movies.csv")
    title = tytul.get()
    movie = df[df["movie_title"] == title]
    budget = movie["budget"].values[0]
    director = movie["director_name"].values[0]

    if os.path.exists("C:\kolosyPython\Kolos_python semestr2_2\dane.txt"):
        with open("C:\kolosyPython\Kolos_python semestr2_2\dane.txt", "a") as file:
            file.write(f"{budget}\n{director}\n")
    else:
        with open("C:\kolosyPython\Kolos_python semestr2_2\dane.txt", "w") as file:
            file.write(f"Budżety i reżyserzy filmów:\n{budget}\n{director}\n")


root = Tk()
root.title("Interface")
root.geometry("500x500")

napis1 = Label(root, text="Podaj tytuł:")
napis1.grid(row=0, column=0)

tytul = Entry(root)
tytul.grid(row=1, column=0)

przycisk1 = Button(root, text="OK", command=show)
przycisk1.grid(row=2, column=0)

napis2 = Label(root, text="budżet: ")
napis2.grid(row=3, column=0)

napis3 = Label(root, text="reżyser: ")
napis3.grid(row=4, column=0)

przycisk2 = Button(root, text="Zapisz", command=zapisz)
przycisk2.grid(row=5, column=0)

root.mainloop()
