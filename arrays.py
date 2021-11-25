import re
import operaciones as operaciones
from unicodedata import normalize


def comprobacionVariableCorchete(variable):
    trans_tab = dict.fromkeys(map(ord, u'\u0301\u0308'), None)
    variable =  normalize('NFKC', normalize('NFKD', variable).translate(trans_tab))
    print(variable)
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

def corchetesCount(variable:str):
    numeroCorchetesAbierto = variable.count("[")
    numeroCorchetesCerrado = variable.count("]")
    return numeroCorchetesAbierto, numeroCorchetesCerrado

def checarArray(cadena:str):
    cadena = cadena.strip()
    print("entro a array")
    tamañoCadena = len(cadena)
    if(cadena[tamañoCadena-1]==";"):
        cadena = cadena[0:tamañoCadena-1]
    cadena2 = cadena.replace("'","@@").replace('"',"'").replace("@@",'"')
    print(cadena2)
    if(cadena.count("=")!=1):
        print("demasiados = no es una asignacion")
        return False
    cadenaSplit = cadena.split("=")[1].split(",")
    corchetesAbierto = 0
    corchetesCerrado = 0
    
    for elemento in cadenaSplit:
        countCorchetesAbireto,countCorchetesCerrado=corchetesCount(elemento)
        corchetesAbierto = corchetesAbierto + countCorchetesAbireto
        corchetesCerrado = corchetesCerrado + countCorchetesCerrado
        if(elemento.count("][")>0 or elemento.count("}{")>0):
            print("array mal asignado")
            return False
        
    if(corchetesAbierto!=corchetesCerrado or (corchetesCerrado==0 and corchetesAbierto==0)):
        print("no coinciden los corchetes")
        return False
    cadenaAnalizar = cadena.split("=")[1]
    cadenaAnalizar = cadenaAnalizar.replace("[","").replace("]","").replace("{","").replace("}","").replace(" ","")
    cadenaAnalizrSplit = cadenaAnalizar.split(",")
    for elemento in cadenaAnalizrSplit:
       if(comprobacionVariableCorchete(elemento)==False):
           if(not operaciones.touringMachine("var ="+elemento)):
               return False
    return True


