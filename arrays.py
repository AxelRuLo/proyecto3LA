import re
import operaciones as operaciones

def comprobacionVariableCorchete(variable):
    comillaSimple = "'"
    comillaDoble = '"'
    erNumeros = "([-]{0,1}[0-9]*[.,][0-9]*)"
    erVariable="|([-]{0,1}[a-zA-Z0-9]([a-zA-Z0-9_])*)|"
    erComillasSimples = "|(["+comillaSimple+"]([a-zA-Z0-9!#$%&()"+comillaDoble +")*+,-./:;<=>?@[\]^_`{|}~])*["+comillaSimple+"])"
    erComillasDobles  = "([" +comillaDoble +"]([a-zA-Z0-9!#$%&()"+comillaSimple+")*+,-./:;<=>?@[\]^_`{|}~])*["+comillaDoble +"])"
    validator = re.compile(erNumeros+erVariable+erComillasDobles+erComillasSimples+erNumeros+"|[1]*")
    match =validator.match(variable)
    try:
        valida = match.group()==variable
    except (TypeError, AttributeError):
        valida = False
    return  valida

def corchetesCount(variable:str):
    numeroCorchetesAbierto = variable.count("[")
    numeroCorchetesCerrado = variable.count("]")
    nuevaVariable = variable.replace("[","").replace("]","").replace("ñ","n")
    return nuevaVariable, numeroCorchetesAbierto, numeroCorchetesCerrado

def checarAsignacionCorchetes(cadena:str):
    cadena2 = cadena.replace("'","@@").replace('"',"'").replace("@@",'"')
    print(cadena2)
    if(cadena.count("=")!=1):
        print("demasiados = no es una asignacion")
        return False
    cadenaSplit = cadena.split("=")[1].split(",")
    corchetesAbierto = 0
    corchetesCerrado = 0
    
    for elemento in cadenaSplit:
        nuevaVariable,countCorchetesAbireto,countCorchetesCerrado=corchetesCount(elemento)
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
        
        
        
print("el resultado es: ",checarAsignacionCorchetes('hola = [1+"hola",2,3,4,4,[[1,"hola"],"hola13"],{}]'))
