import unittest
from ejercicio import addit

class TestAddit(unittest.TestCase):
    def test_positivo(self):
        resultado = addit(3)
        self.assertEqual(resultado, 8)

    def test_negativo(self):
        resultado = addit(-3)
        self.assertEqual(resultado, 2)

if __name__ == '__main__':
    unittest.main()
