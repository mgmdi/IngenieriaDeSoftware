import unittest
import seguros

class TestBeta(unittest.TestCase):

    def test_calculoEdad(self):
     
        self.assertEqual(seguros.calculoEdad("16061997"), 21)

    def test_verificacionDatos(self):

        self.assertEqual(seguros.verificacionDatos(56,"l","m"), "SI")

if __name__ == '__main__':
    unittest.main() 