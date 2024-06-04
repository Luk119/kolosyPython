# import pickle
# import pandas as pd
#
# # lista = ["ale", "jazda", "co", "za"]
# # lista.insert(1, "jaja")
# # lista.remove("jazda")
# # print("|".join(lista))
# #
# # slownik = {"Aga": 34, "Jula": 66}
# # print(*slownik.items())
# #
# # tupla = (3, 4, 5, 2, 4)
# # print(tupla)
# #
# # zbior = {1, 2, 1, 4, 5, 3, 0, 0}
# # zbior.remove(3)
# # print(zbior)
#
# # a = 1
# #
# # match a:
# #     case 1:
# #         print(1)
# #     case 2:
# #         print(2)
# #     case _:
# #         print("inne")
#
# # string = "Tu Heniek Ogór."
# #
# # with open("plik.pickle", "wb") as file:
# #     pickle.dump(string, file)
# #
# # with open("plik.pickle", "rb") as file:
# #     data = pickle.load(file)
# #     print(data)
#
# # dane = {
# #         "Imie": ["Seba", "Łukasz"],
# #         "Nazwisko": ["Ros", "Kun"],
# #         "Wiek": [21, 20]
# # }
# #
# #
# # df = pd.DataFrame(dane)
# # df.to_csv("imiona.csv", index=False)
# # print(df.head())
#
# # dfread = pd.read_csv("C:/kolosyPython/movies.csv")
# # print(dfread.head(5))
# #---------------------------------------------------
# # df = pd.read_csv("C:/kolosyPython/movies.csv")
# #
# # # oceny = df[df["imdb_score"] > 9]
# #
# # cb = df[
# #         (df["imdb_score"] > 9)
# #         &
# #         (df["country"] == "USA")]
# #
# # titles = df["movie_title"]
# # # print(oceny["movie_title"])
# # print("czarno biały z oceną > 9:", cb)
#
# #Dekorator
# # def dec(suma):
# #     def wrapper(*args):
# #         print("przed wykonaniem")
# #         print(suma(args[0], args[1]))
# #         print("Po wykonaniu")
# #         return 1
# #     return wrapper
# #
# # @dec
# # def suma(a, b):
# #     return a+b
# #
# # suma(3, 6)

#Zad 1a
# import os
# class Plik1:
#     """
#     Klasa reprezentująca plik.
#
#     Attributes:
#         nazwa_pliku (str): Nazwa pliku.
#
#     Methods:
#         __init__(): Inicjalizuje nowy obiekt klasy Plik1 z domyślną nazwą "NewFile".
#         __zmiana_nazwy(nowa_nazwa: str): Prywatna metoda zmieniająca nazwę pliku.
#         __str__(): Metoda specjalna zwracająca reprezentację tekstową obiektu.
#     """
#     def __init__(self, nazwa_pliku="NewFile"):
#         self.nazwa_pliku = nazwa_pliku
#
#     def __zmiana_nazwy(self, nowa_nazwa):
#         self.nazwa_pliku = nowa_nazwa
#     def __str__(self):
#         return f"Plik1: {self.nazwa_pliku}"
#
# pliczek = Plik1()
# print(pliczek)
#
# class Plik2(Plik1):
#     i = 0
#
#     def __init__(self, nazwa_folderu_user, nazwa_pliku):
#         super().__init__(nazwa_pliku)
#         self.nazwa_folderu = nazwa_folderu_user
#         # self.nazwa_pliku = nazwa_pliku
#
#     def zapisz_do_pliku(self, tekst):
#         with open(os.path.join(self.nazwa_folderu, self.nazwa_pliku)+".txt", "w") as file:
#             file.write(tekst)
#         Plik2.i += 1
#
#     @staticmethod
#     def ilosc_obiektow():
#         print(f"ilosc obiektow: {Plik2.i}")
#
#
# pliki = Plik2("C:/kolosyPython", "dane")
# pliki.zapisz_do_pliku("Zawartosc - pliki1")
#
# pliki2 = Plik2("C:/kolosyPython", "dane2")
# pliki2.zapisz_do_pliku("Zawartosc - pliki2")
#
# pliki3 = Plik2("C:/kolosyPython", "dane3")
# pliki3.zapisz_do_pliku("Zawartosc - pliki3")
#
# Plik2.ilosc_obiektow()

#Zad 4
import os
import pickle
class Prostokat:

    def __init__(self, bok_A_user = 1):
        self.bok_A = bok_A_user
        self._bok_B = 1

    def __str__(self):
        return f"Obiekt ma następujące parametry: {self.bok_A} x {self._bok_B}"

    def __repr__(self):
        return f"({self.bok_A}, {self._bok_B})"

    def __mul__(self, obiekt2):
        if isinstance(obiekt2, Prostokat):
            return self.pole() * obiekt2.pole()
        else:
            raise TypeError("wrong object type!")

    def pole(self):
        return self.bok_A * self._bok_B


k1 = Prostokat(10)
k2 = Prostokat(20)
print(repr(k1))
print(k1)
print("Pole: ", k1.pole())
print(k1 * k2)


class Prostopadloscian(Prostokat):
    ilosc_obiektow = 0
    def __init__(self, bok_A_user, wysokosc_H_user):
        super().__init__(bok_A_user)
        self.wysokosc_H = wysokosc_H_user
        Prostopadloscian.ilosc_obiektow += 1

    def __str__(self):
        return (f"Obiekt ma następujące parametry {self.bok_A} x {self._bok_B} x {self.wysokosc_H}\nLiczba obiektow:"
                f" {Prostopadloscian.ilosc_obiektow}")

    def pole(self):
        pole_pow = 2*(self.bok_A * self.wysokosc_H + self.bok_A * self._bok_B + self.wysokosc_H * self._bok_B)
        path = "C:\kolosyPython\Kolos_python semestr2_1" + "\prostopadloscian.pickle"
        if not os.path.exists(path):
            with open(path, "wb") as file:
                pickle.dump(f"pole powierzchni {Prostopadloscian.ilosc_obiektow} porostopadloscianu {pole_pow}", file)
        else:
            with open(path, "ab") as file:
                pickle.dump(f"pole powierzchni {Prostopadloscian.ilosc_obiektow} porostopadloscianu {pole_pow}", file)

        return pole_pow

    def __mul__(self, obiekt2):
        if isinstance(obiekt2, Prostopadloscian):
            return self.pole() * obiekt2.pole()
        else:
            raise TypeError("Invalid object type!")

p1 = Prostopadloscian(10, 20)
p2 = Prostopadloscian(5, 10)
print(p1 * p2)
print(p1)
p3 = Prostopadloscian(10, 10)
p1*p3
print(p3)