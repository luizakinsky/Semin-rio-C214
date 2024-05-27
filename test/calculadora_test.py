import unittest
from src.calculadora import soma

class TestCalculadora(unittest.TestCase):

    def test_soma_positivos(self):
        self.assertEqual(soma(2, 3), 5)

    def test_soma_negativos(self):
        self.assertEqual(soma(-1, -1), -2)

    def test_soma_zero(self):
        self.assertEqual(soma(0, 0), 0)

if __name__ == '_main_':
    unittest.main()
