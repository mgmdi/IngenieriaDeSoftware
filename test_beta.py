import unittest
import seguros

class TestBeta(unittest.TestCase):

    def test_calculoEdad(self):
     
        self.assertEqual(seguros.calculoEdad("16/06/1997"), 21)

    def test_verificacionDatos(self):

        self.assertEqual(seguros.verificacionDatos(56,"f",800), "SI")

if __name__ == '__main__':
    unittest.main() 