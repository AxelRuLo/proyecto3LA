from os import truncate
from tkinter.constants import FALSE
import arrays as array
import re


def comprobacionAsignaciones(variable):
    erVariable="([-]{0,1}[a-zA-Z]+[a-zA-Z0-9_]*)|([-]{0,1}[0-9]*[.,]{0,1}[0-9]*)"
    validator = re.compile(erVariable)
    match =validator.match(variable)
    try:
        valida = match.group()==variable
    except (TypeError, AttributeError):
        valida = False
    return  valida

def comprobarObjeto(variable):
    print("h",variable)
    comillaDoble = '"'
    erObjetos = "(new[\s][a-zA-Z]+[a-zA-Z0-9_]*[(][a-zA-Z0-9!\s#$%&()"+comillaDoble+")*+,'-./:;<=>?@[\]^_`{|}~]*[)])"
    validator = re.compile(erObjetos)
    match =validator.match(variable)
    try:
        valida = match.group()==variable
    except (TypeError, AttributeError):
        valida = False
    return  valida

def comprobarSimples(variable):
    comillaSimple = "'"
    comillaDoble = '"'
    erComillasSimples = "(["+comillaSimple+"]([a-zA-Z0-9!\s#$%&()"+comillaDoble +")*+,-./:;<=>?@[\]^_`{|}~])*["+comillaSimple+"])"
    validator = re.compile(erComillasSimples)
    match =validator.match(variable)
    try:
        valida = match.group()==variable
    except (TypeError, AttributeError):
        valida = False
    return  valida

def comprobarDobles(variable):
    print("h",variable)
    comillaSimple = "'"
    comillaDoble = '"'
    erComillasDobles  = "(["+comillaDoble +"]([a-zA-Z0-9!\s#$%&()"+comillaSimple+")*+,-./:;<=>?@[\]^_`{|}~])*["+comillaDoble+"])"
    validator = re.compile(erComillasDobles)
    match =validator.match(variable)
    try:
        valida = match.group()==variable
    except (TypeError, AttributeError):
        valida = False
    return  valida

def comprobarSinAsigancion(variable):
    erVariable="(let|const|var)([a-zA-Z]+[a-zA-Z0-9_]*)"
    validator = re.compile(erVariable)
    match =validator.match(variable)
    try:
        valida = match.group()==variable
    except (TypeError, AttributeError):
        valida = False
    return  valida


def comprobacionAsignacionesP1(variable):
    variable = variable.replace(" ","").replace("  ","")
    erVariable="(let|var|const){0,1}[a-zA-Z]+(([a-zA-Z_0-9.]*[a-zA-Z0-9_]+)|([a-zA-Z0-9_]))([,][a-zA-Z]+(([a-zA-Z_.0-9]*[a-zA-Z0-9_]+)|([a-zA-Z0-9_]*)))*"
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
        cadenaSplit = cadena.split(" = ")
        if(not comprobacionAsignacionesP1(cadenaSplit[0]) or len(cadena)<1 or cadena.count("=")==0):
            if(comprobarSinAsigancion(cadena)):
                return True
            return False
        if(comprobacionAsignaciones(cadenaSplit[1])==True or comprobarObjeto(cadenaSplit[1])==True or comprobarSimples(cadenaSplit[1])==True or comprobarDobles(cadenaSplit[1])==True):
            print("si jalo")
            return True
        else:
            print("checando array")
            return array.checarArray(cadena)
    except:
        return False
