import unittest
def multi(*args):
    if len(args) == 1 and isinstance(args[0], list):
        nieparzyste = list(filter(lambda x: x % 2 == 1, args[0]))
        wynik = list(map(lambda x: x * x, nieparzyste))
        return wynik

    elif len(args) > 1:
        i = len(args)-1
        iloczyn = 1
        while i >= 0:
            iloczyn *= args[i]
            i -= 1
        return iloczyn


def dekorator(func):
    def wrapper(a, b, action):
        if action == "dodawanie":
            return func(a, b, "dodawanie")
        elif action == "odejmowanie":
            return a - b
    return wrapper


@dekorator
def calculator(a, b, action):
    return a + b


def licz(a):
    if a == 1:
        multi([1, 2, 3, 4])
    else:
        calculator(2, 4)


class Testy(unittest.TestCase):
    def test1(self):
        self.assertEqual(calculator(2, 2, "dodawanie"), 4, "Cos nie tak")

    def test2(self):
        self.assertEqual(calculator(3, 4, "odejmowanie"), -1, "Cos nie tak")