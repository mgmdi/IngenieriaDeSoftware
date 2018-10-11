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

    if (not(str(age).isdigit()) or sex.lower() not in ["m","f","femenino","masculino"] or 
    not(str(weeksC).isdigit())):
        print("Error, existe alguna discrepancia entre la edad, el sexo o las semanas")
        exit(1) 

    
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


if __name__ == '__main__':
    main() 