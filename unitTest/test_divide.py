import unittest
from ejercicio import divide

class TestDivide(unittest.TestCase):
    def test_division_simple(self):
        resultado = divide(8, 2)
        self.assertEqual(resultado, 4)

    def test_division_decimal(self):
        resultado = divide(5, 2)
        self.assertEqual(resultado, 2.5)

if __name__ == '__main__':
    unittest.main()
