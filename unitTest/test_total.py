from ejercicio import total
import unittest

class TestCalculaSumatoriaArray(unittest.TestCase):    
    def test_suma_positivos(self):
        resultado = total([1, 2, 3, 4])
        self.assertEqual(resultado, 10)

    def test_suma_negativos(self):
        resultado = total([-1, -2, -3, -4])
        self.assertEqual(resultado, -10)

if __name__ == '__main__':
    unittest.main()