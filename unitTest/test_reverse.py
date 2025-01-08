import unittest
from ejercicio import reverse

class TestReverse(unittest.TestCase):
    def test_simple(self):
        resultado = reverse("casa")
        self.assertEqual(resultado, "asac")

    def test_vacio(self):
        resultado = reverse("")
        self.assertEqual(resultado, "")

if __name__ == '__main__':
    unittest.main()
