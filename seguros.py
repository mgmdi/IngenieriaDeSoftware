import datetime

def verificacionDatos(age,sex,weeksC):
    """
    Descripcion: funcion que dada la edad, el sexo y las semanas cotizadas de 
    un solicitante se verifica si cumple con los requisitos necesarios para
    el seguro social de IVSS
    Parametros: int age, string sex, int weeksC
    Valor de retorno: "Si" si cumple con los requerimientos
                    "No" en caso contrario
    """

    if(sex.lower() == "m" and int(age) >= 60 and int(weeksC)>=750):
        return("SI")
    elif(sex.lower() == "f" and int(age) >= 55 and int(weeksC)>=750):
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
    now = datetime.datetime.now()
    edad = int(now.year) - int(fecha[2])

    return edad

def main():
    """
    Descripcion: funcion que funciona como menu en la aplicacion. Toma los datos
    ya sea de consola o de un archivo de texto y llama a las funciones respectivas
    para su procesamiento
    Parametros: None
    Valor de retorno: None
    """


if __name__ == '__main__':
    main() 