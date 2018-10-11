import datetime

def verificacionDatos(age,sex,weeksC,indicador):
    """
    Descripcion: funcion que dada la edad, el sexo y las semanas cotizadas de 
    un solicitante se verifica si cumple con los requisitos necesarios para
    el seguro social de IVSS
    Parametros: int age, string sex, int weeksC
    Valor de retorno: "Si" si cumple con los requerimientos
                    "No" en caso contrario
    """

    if (not(str(age).isdigit()) or sex.lower() not in ["m","f","femenino","masculino"] or 
    not(str(weeksC).isdigit())):
        print("Error, existe alguna discrepancia entre la edad, el sexo o las semanas")
        exit(1) 

    if(sex.lower() == "m" and int(age) >= 60 - indicador and int(weeksC)>=750):
        return("SI")
    elif(sex.lower() == "f" and int(age) >= 55 - indicador and int(weeksC)>=750):
        return("SI")
    else:
        return("NO")
   

def calculoEdad(fecha):
    """
    Descripcion: funcion que dada una fecha de nacimiento procesa el string y
    arroja la edad actual
    Parametros: string fecha en el formato XX/XX/XXXX
    Valor de retorno: int edad actual
    """
    
    fecha = fecha.split('/')
    if (len(fecha) != 3 or not(fecha[0].isdigit()) or not(fecha[1].isdigit()) or not(fecha[2].isdigit())):
        print("Existe alguna discrepancia en la fecha")
        exit(1)

    now = datetime.datetime.now()

    if(int(fecha[1])<= now.month):
        edad = int(now.year) - int(fecha[2])
    else:
        edad = int(now.year) - int(fecha[2]) - 1
  

    return edad

def main():
    """
    Descripcion: funcion que funciona como menu en la aplicacion. Toma los datos
    ya sea de consola o de un archivo de texto y llama a las funciones respectivas
    para su procesamiento
    Parametros: None
    Valor de retorno: None
    """
    opcion = input("Ingrese la opcion 1 para ingresar datos por consola, ingrese dos para cargar un archivo de texto: ")
    if(opcion == "1"):
        edad = calculoEdad(input("Imgrese fecha de nacimiento (XX/XX/XXXX): "))
        sexo = input("Ingrese su sexo: ")
        semCoti = input("Ingrese el numero de semanas cotizadas: ")
        descontEdad = input("Ha trabajado usted en medios insalubres o capaces de producir vejez prematura?")
        if descontEdad.lower() not in ["si","no"]:
            print("Error, la respuesta debe ser si o no")
            exit(1)
        if(descontEdad.lower() == "si"):
            numAnos = input("Indique el numero de anos que trabajo: ")
            print(verificacionDatos(edad,sexo,weeksC,int(numAnos) // 4))
            return
           
        print(verificacionDatos(edad,sexo,weeksC,0))
    elif(opcion == "2"):
        nombre = input("Ingrese nombre del archivo: ")
        file = open(nombre, "r")
        for line in file:
            datos = line.split()
            edad = calculoEdad(datos[0])
            if(len(datos) == 5 and datos[3].lower() == "si"):
                print(verificacionDatos(edad,datos[1],datos[2], (int(datos[4])//4)))
                return
            print(verificacionDatos(edad,datos[1],datos[2], 0))
    else:
        print("Error, debe ingresar 1 o 2")
       


if __name__ == '__main__':
    main() 