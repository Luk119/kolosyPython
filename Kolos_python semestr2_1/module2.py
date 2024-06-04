import unittest
import module1
class Testy(unittest.TestCase):
    def test_pow(self):
        self.assertEqual(module1.funkcja2([1, 4, 9]), [1, 2, 3], "Something went wrong")

unittest.main(exit=False)
