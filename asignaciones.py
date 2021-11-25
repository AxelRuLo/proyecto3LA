import arrays as array
import re

from operaciones import comprobacionVariable

def comprobacionAsignaciones(variable):
    comillaSimple = "'"
    comillaDoble = '"'
    erNumeros = "([-]{0,1}[0-9]*[.,][0-9]*)"
    erVariable="|([-]{0,1}[a-zA-Z0-9]([a-zA-Z0-9_])*)|"
    erComillasSimples = "|(["+comillaSimple+"]([a-zA-Z0-9!#$%&()"+comillaDoble +")*+,-./:;<=>?@[\]^_`{|}~])*["+comillaSimple+"])"
    erComillasDobles  = "([" +comillaDoble +"]([a-zA-Z0-9!#$%&()"+comillaSimple+")*+,-./:;<=>?@[\]^_`{|}~])*["+comillaDoble +"])"
    validator = re.compile(erNumeros+erVariable+erComillasDobles+erComillasSimples+"|(1)*")
    match =validator.match(variable)
    try:
        valida = match.group()==variable
    except (TypeError, AttributeError):
        valida = False
    return  valida

def comprobacionAsignacionesP1(variable):
    variable = variable.replace(" ","").replace("  ","")
    print(variable)
    erVariable="(let|var|const){0,1}[a-zA-Z]+[0-9]*[a-zA-Z_]*([,][a-zA-Z]+[0-9]*[a-zA-Z_]*)*"
    validator = re.compile(erVariable)
    match =validator.match(variable)
    try:
        valida = match.group()==variable
    except (TypeError, AttributeError):
        valida = False
    return  valida

def comprobarAsignaciones(cadena:str):
    
    try:
        cadenaSplit = cadena.split(" = ")
        if(not comprobacionAsignacionesP1(cadenaSplit[0]) or len(cadena)<1 or cadena.count("=")==0):
            return False

    except:
        pass



        
print(comprobarAsignaciones("vari == "))

    