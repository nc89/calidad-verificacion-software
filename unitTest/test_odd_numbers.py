import unittest
from ejercicio import odd_numbers

class TestOddNumbers(unittest.TestCase):
    def test_numeros_impares(self):
        resultado = odd_numbers([1, 8, 3, 6, 12, 5])
        self.assertEqual(resultado, [1, 3, 5])

    def test_sin_impares(self):
        resultado = odd_numbers([2, 4, 6])
        self.assertEqual(resultado, [])

if __name__ == '__main__':
    unittest.main()
