from tkinter.constants import FALSE
import arrays as array
import re


def comprobacionAsignaciones(variable):
    print(variable)
    comillaSimple = "'"
    comillaDoble = '"'
    erNumeros = "([-]{0,1}[0-9]*[.,][0-9]*)"
    erVariable="|([-]{0,1}[a-zA-Z0-9]([a-zA-Z0-9_])*)|"
    erComillasSimples = "|(["+comillaSimple+"]([a-zA-Z0-9!\s#$%&()"+comillaDoble +")*+,-./:;<=>?@[\]^_`{|}~])*["+comillaSimple+"])"
    erComillasDobles  = "([" +comillaDoble +"]([a-zA-Z0-9!\s#$%&()"+comillaSimple+")*+,-./:;<=>?@[\]^_`{|}~])*["+comillaDoble +"])"
    validator = re.compile(erNumeros+erVariable+erComillasDobles+erComillasSimples)
    match =validator.match(variable)
    try:
        valida = match.group()==variable
    except (TypeError, AttributeError):
        valida = False
    return  valida

def comprobacionAsignacionesP1(variable):
    variable = variable.replace(" ","").replace("  ","")
    erVariable="(let|var|const){0,1}[a-zA-Z]+[0-9]*[a-zA-Z_0-9]*([,][a-zA-Z]+[0-9]*[a-zA-Z_]*)*"
    validator = re.compile(erVariable)
    match =validator.match(variable)
    try:
        valida = match.group()==variable
    except (TypeError, AttributeError):
        valida = False
    return  valida

def comprobarAsignaciones(cadena:str):
    cadena = cadena.replace(";","")
    try:
        print(cadena)
        cadenaSplit = cadena.split(" = ")
        if(not comprobacionAsignacionesP1(cadenaSplit[0]) or len(cadena)<1 or cadena.count("=")==0):
            return False
        if(comprobacionAsignaciones(cadenaSplit[1])):
            print("si jalo")
            return True
        else:
            print("checando array")
            return array.checarArray(cadena)
    except:
        return False



        
print(comprobarAsignaciones("const getFac = 'ESP8266';"))

    