import unittest
def decor(funkcja):
    def wrapper(*args, **kwargs):
        if len(kwargs) > 0:
            print(f"liczę iloczyn liczb {kwargs.values()}")
            return funkcja(**kwargs)
        else:
            return funkcja(*args)
    return wrapper
@decor
def funkcja(*args, **kwargs):

    if len(args) > 0:
        if list(map(lambda x: isinstance(x, int), args)):
            suma = 0
            for arg in filter(lambda x: x % 2 == 1, args):
                suma += arg
            return suma


    else:
        if all(list(map(lambda x: isinstance(x, int), kwargs.values()))):
            i = 0
            iloczyn = 1
            lista = list(kwargs.values())
            while i < len(lista):
                iloczyn *= lista[i]
                i += 1
            return iloczyn

print(funkcja(10, 20, 31))
print(funkcja(a=2, b=10, c="g"))
print(funkcja(a=2, b=10, c=6))

class Testy(unittest.TestCase):
    def test_1(self):
        self.assertEqual(funkcja(a=2, b=10, c=6), 120, "Error")

    def test_2(self):
        self.assertEqual(funkcja(1, 2, 3, 4, 5), 9, "Error")