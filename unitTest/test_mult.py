import unittest
from ejercicio import mult

class TestMult(unittest.TestCase):
    def test_positivo(self):
        resultado = mult(3)
        self.assertEqual(resultado, 24)

    def test_cero(self):
        resultado = mult(0)
        self.assertEqual(resultado, 0)

if __name__ == '__main__':
    unittest.main()
