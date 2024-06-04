import unittest


def calculator(*args):
    if len(args) == 1 and isinstance(args[0], list):
        return list(map(lambda x: 2*x, args[0]))
    else:
        suma = 0
        for arg in args:
            suma += arg
        return suma


class Testy(unittest.TestCase):

    def test_calculator_lista(self):
        self.assertEqual(calculator([1, 2, 3, 4, 5]), [2, 4, 6, 8, 10], "Error lista")
    def test_calculator_suma(self):
        self.assertEqual(calculator(1, 2, 3, 4, 5), 15, "Error suma")


unittest.main(exit=False)
