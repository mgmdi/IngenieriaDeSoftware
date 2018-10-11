import unittest
import seguros
'''
Para ejecutar: python testFinal.py 
'''
class TestFinal(unittest.TestCase):
    '''
    Funcion que realiza la prueba de la ejecucion del programa completo.
    Los datos pueden ser ingresados mediante un archivo de texto o mediante consola.
    '''
    def test_programa(self):         
    
        #CASO 1  // Para ingresar datos que cumplen con los requisitos 
        self.assertEqual(seguros.main(),"SI")
        #CASO 2  // Para ingresar datos que no cumplan con los requisitos 
        self.assertEqual(seguros.main(),"NO")

if __name__ == '__main__':
    unittest.main()  