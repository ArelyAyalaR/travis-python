import unittest
from calculador.app import sumar, dividir, restar, multiplicar

class TestCalculador(unittest.TestCase):
    def test_sumar(self):
        result = sumar(1,2)
        self.assertEqual(result, 3, "El resultado debería ser 3")

    def test_restar(self):
        result1 = restar(3,4)
        self.assertEqual(result1, -1, "El resultado debería ser -1")

    def test_multiplicar(self):
        result = multiplicar(3,4)
        self.assertEqual(result, 12, "El resultado debería ser 12")

    def test_dividir(self):
        result = dividir(12,3)
        self.assertEqual(result, 4, "El resultado debería ser 4")


if __name__ == "__main__":
    unittest.main()
