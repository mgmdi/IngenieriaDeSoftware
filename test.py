import unittest
import seguros


class TestSeguro(unittest.TestCase):

    def test_calculoEdad(self):         
        '''Se realizan las siguientes pruebas no fronteras para verificar 
        que la edad se esta calculando correctamente'''
        #CASO 1
        self.assertEqual(seguros.calculoEdad("16/06/1997"), 21)
        #CASO 2 
        self.assertEqual(seguros.calculoEdad("16/06/1980"), 38)
        #CASO 3 
        self.assertEqual(seguros.calculoEdad("16/12/1998"), 19)
        #CASO 4
        self.assertEqual(seguros.calculoEdad("09/10/1998"), 20)
        #CASO 5 
        self.assertEqual(seguros.calculoEdad("01/01/1950"), 68)
        #CASO 6
        self.assertEqual(seguros.calculoEdad("15/06/1960"), 58)
        #CASO 7
        self.assertEqual(seguros.calculoEdad("25/07/1956"), 62)
        #CASO 8
        self.assertEqual(seguros.calculoEdad("30/12/1940"), 77)  


    def test_verificacionDatosNF(self):         #casos no frontera
        #CASO 1
        self.assertEqual(seguros.verificacionDatos(56,"f",800,False), "SI")
        #CASO 2
        self.assertEqual(seguros.verificacionDatos(70,"m",50,False), "NO")
        #CASO 3
        self.assertEqual(seguros.verificacionDatos(80,"f",1000,False), "SI")
        #CASO 4 
        self.assertEqual(seguros.verificacionDatos(50,"f",800,False), "NO")
        #CASO 5 
        self.assertEqual(seguros.verificacionDatos(40,"m",500,False), "NO")
        #CASO 6
        self.assertEqual(seguros.verificacionDatos(63,"f",800,False), "SI")
        #CASO 7 
        self.assertEqual(seguros.verificacionDatos(78,"f",600,False), "NO")
        #CASO 8 
        self.assertEqual(seguros.verificacionDatos(66,"m",800,False), "SI")


    def test_verificacionDatosF(self):
        """
        Funcion con casos frontera.
        Los casos frontera se definen como la minima edad y minimo numero de cotizaciones
        que se debe tener para optar por el seguro.
        Se considera la minima edad como 55 para hombres (con 5 anos maximos de disminucion por trabajo
        en medios insalubres) y 50 para las mujeres por la misma razon. 
        """
        #CASO 1
        self.assertEqual(seguros.verificacionDatos(55,"f",750,True), "SI")
        #CASO 2
        self.assertEqual(seguros.verificacionDatos(50,"f",750,True), "NO")
        #CASO 3
        self.assertEqual(seguros.verificacionDatos(60,"m",750,True), "SI")
        #CASO 4
        self.assertEqual(seguros.verificacionDatos(55,"m",750,True), "NO")


    def test_verificacionDatosM(self):
        '''
        Funcion para verificacion de datos con casos de Malicia 
        Los casos de malicia se definen como aquellos en donde los datos ingresados son invalidos y/o 
        arrojan excepciones/errores.
        Se considera caso invalido cuando el dato ingresado para indicar el sexo de la persona difiere de f/m.
        Asimismo se considera caso invalido (ERROR) cuando el numero de horas cotizadas ingresadas difiere de un digito (positivo).
        '''  
        #CASO 1 
        with self.assertRaises(SystemExit) as cm:
            seguros.verificacionDatos(56,"m","a5",1)
        self.assertEqual(cm.exception.code, 1) 

        #CASO 2
        with self.assertRaises(SystemExit) as cm:
            seguros.verificacionDatos(56,"m",[0],1)
        self.assertEqual(cm.exception.code, 1)  

        #CASO 2
        with self.assertRaises(SystemExit) as cm:
            seguros.verificacionDatos(56,"Q",800,1)
        self.assertEqual(cm.exception.code, 1) 

        #CASO 3
        with self.assertRaises(SystemExit) as cm:
            seguros.verificacionDatos("Ochenta","m",750,1)
        self.assertEqual(cm.exception.code, 1) 

        #CASO 4
        with self.assertRaises(SystemExit) as cm:
            seguros.verificacionDatos(-56,"m",700,7)
        self.assertEqual(cm.exception.code, 1)

if __name__ == '__main__':
    unittest.main()  