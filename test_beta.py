import unittest
import seguros

class TestBeta(unittest.TestCase):

    def test_calculoEdad(self):
     
        self.assertEqual(seguros.calculoEdad("16/12/1998"), 19)
        with self.assertRaises(SystemExit) as cm:
            seguros.calculoEdad("16061997")

        self.assertEqual(cm.exception.code, 1)

    def test_verificacionDatos(self):

        self.assertEqual(seguros.verificacionDatos(50,"f",800,15), "SI")
        with self.assertRaises(SystemExit) as cm:
            seguros.verificacionDatos(56,"l","m",15)

        self.assertEqual(cm.exception.code, 1)


if __name__ == '__main__':
    unittest.main() 