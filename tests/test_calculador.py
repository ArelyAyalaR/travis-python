import unittest
from calculador.app import sumar, dividir, restar, multiplicar

class TestCalculador(unittest.TestCase):
     def test_sumar_correcta(self):
        result = sumar(1, 2)
        self.assertEqual(result, 3, "El resultado debería ser 3")

    def test_sumar_incorrecta(self):
        result = sumar(1, 2)
        self.assertNotEqual(result, 4, "El resultado no debería ser 4")

    def test_restar_correcta(self):
        result = restar(3, 4)
        self.assertEqual(result, -1, "El resultado debería ser -1")

    def test_restar_incorrecta(self):
        result = restar(3, 4)
        self.assertNotEqual(result, 2, "El resultado no debería ser 2")

    def test_multiplicar_correcta(self):
        result = multiplicar(3, 4)
        self.assertEqual(result, 12, "El resultado debería ser 12")

    def test_multiplicar_incorrecta(self):
        result = multiplicar(3, 4)
        self.assertNotEqual(result, 10, "El resultado no debería ser 10")

    def test_dividir_correcta(self):
        result = dividir(12, 3)
        self.assertEqual(result, 4, "El resultado debería ser 4")

    def test_dividir_incorrecta(self):
        result = dividir(12, 3)
        self.assertNotEqual(result, 5, "El resultado no debería ser 5")


if __name__ == "__main__":
    unittest.main()
