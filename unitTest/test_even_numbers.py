import unittest
from ejercicio import even_numbers

class TestEvenNumbers(unittest.TestCase):
    def test_numeros_pares(self):
        resultado = even_numbers([1, 8, 3, 6, 12, 5])
        self.assertEqual(resultado, [8, 6, 12])

    def test_sin_pares(self):
        resultado = even_numbers([1, 3, 5])
        self.assertEqual(resultado, [])

if __name__ == '__main__':
    unittest.main()
