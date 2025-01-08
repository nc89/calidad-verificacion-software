import unittest
from ejercicio import length

class TestLength(unittest.TestCase):
    def test_mayor_a_cinco(self):
        resultado = length("Prueba")
        self.assertEqual(resultado, "Longer than 5")

    def test_menor_a_cinco(self):
        resultado = length([2, 3, 5, 2])
        self.assertEqual(resultado, "Less than 5")

if __name__ == '__main__':
    unittest.main()
