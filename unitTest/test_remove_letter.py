import unittest
from ejercicio import remove_letter

class TestRemoveLetter(unittest.TestCase):
    def test_remover_letra(self):
        resultado = remove_letter("a", "Hola esto es una prueba")
        self.assertEqual(resultado, "Hol esto es un prueb")

    def test_no_remover(self):
        resultado = remove_letter("x", "Hola")
        self.assertEqual(resultado, "Hola")

if __name__ == '__main__':
    unittest.main()
