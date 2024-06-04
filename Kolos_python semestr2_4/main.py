"""
This module contains code for log in, allows for changing username, user surname and user password.
Module contains two classes:
    Logowanie class and Student class that inherits from Logowanie class

"""
import pickle
import os
class Logowanie:
    i = 0
    def __init__(self, haslo_u, login_u="admin"):
        self._pin = "0000"
        self.login = login_u
        self.haslo = haslo_u
        self.i += 1
    def __str__(self):
        """
        String representation of Logowanie class

        Returns: string representation of Logowanie class

        """
        return f"login = {self.login}, haslo = {self.haslo}, pin = {self._pin}"

    def zmienpin(self, pin_u):
        self._pin = pin_u


class Student(Logowanie):
    def __init__(self, login_student, imie_u, nazwisko_u):
        try:
            self.imie = str(imie_u)
            self.nazwisko = str(nazwisko_u)
            str(login_student)
        except TypeError as e:
            print(e)
        except NameError as e:
            print(e)

        super().__init__(None, login_student)

    def zmiendane(self, new_imie, new_nazwisko, new_haslo):
        self.imie = new_imie
        self.nazwisko = new_nazwisko
        self.haslo = new_haslo

        cur_path = os.getcwd()
        with open("dane_pickle.pickle", "ab") as file:
            pickle.dump(f"imie: {self.imie}, nazwisko: {self.nazwisko}, haslo: {self.haslo}", file)


s1 = Student("sebek123", "Sebastian", "Rosicki")
s1.zmiendane("kalllll", "kot", "password")
