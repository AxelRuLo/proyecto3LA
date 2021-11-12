
from os import truncate
import re


def comprobacionVariable(variable):
    comillaSimple = "'"
    comillaDoble = '"'
    erVariable="([-]{0,1}[a-zA-Z0-9]([a-zA-Z0-9_])*)|"
    erComillasSimples = "|(["+comillaSimple+"]([a-zA-Z0-9!#$%&"+comillaDoble+"()*+,-./:;<=>?@[\]^_`{|}~])*["+comillaSimple+"])"
    erComillasDobles = "(["+comillaDoble+"]([a-zA-Z0-9!#$%&()"+comillaSimple+"'*+,-./:;<=>?@[\]^_`{|}~])*["+comillaDoble+"])"
    validator = re.compile(erVariable+erComillasDobles+erComillasSimples)
    match =validator.match(variable)
    try:
        valida = match.group()==variable
    except (TypeError, AttributeError):
        valida = False
    return  valida

def comprobacionAsignacion(variable):
    erVariable="(([ ])*[a-zA-Z]([a-zA-Z0-9_])*)"
    erAsignaciones = "((let|var|const)([ ]))*"
    erVariablesMultiples = erVariable+"(([,])"+erVariable+")*"
    validator = re.compile(erAsignaciones+erVariablesMultiples+"([ ]){0,1}")
    match =validator.match(variable)
    try:
        valida = match.group()==variable
    except (TypeError, AttributeError):
        valida = False
    return  valida

def parentesisCount(variable:str):
    numeroParentesisAbierto = variable.count("(")
    numeroParentesisCerrado = variable.count(")")
    nuevaVariable = variable.replace("(","").replace(")","").replace("ñ","n")
    return nuevaVariable, numeroParentesisAbierto, numeroParentesisCerrado

def touringGears(cinta:list):
    comprobacionOperador = False
    operadores = ["+","/","-","%","^^","*"]
    if(not comprobacionVariable(cinta[0])):
        print(cinta[0])
        return " error en una variable"
    for elemento in cinta:
        if(comprobacionOperador):
            validacionOperador = operadores.count(elemento)
            if(validacionOperador==0 and elemento.count("-")==0):
                print(elemento)
                return "un simbolo esta mal colocado o no existe"
            comprobacionOperador = False
        else:
            validacionVariable = comprobacionVariable(elemento)
            if(not validacionVariable):
                print(elemento)
                return "una variable no es valida"
            comprobacionOperador = True
            
    if(comprobacionOperador==False):
        return "error no se puede terminar con un operador"
    return "aceptado"

def llenarCinta(cintaAux:list):
    cinta = []
    for elemento in cintaAux:
        if (elemento != ""):
            cinta.append(elemento)
    return cinta

def touringGearsString(cinta:list):
    listaStrings = []
    for index in range(len(cinta)):
        if(cinta[index].count("'")>0 or cinta[index].count('"')>0):
            listaStrings.append(index)
    for index in listaStrings:
        if(index-1<0):
            if(cinta[index+1]!="+"):
                return False
        elif(index+1>len(cinta)-1):
            if(cinta[index+-1]!="+"):
                return False
        else:
            if(cinta[index+1]!="+" or cinta[index-1]!="+"):
                return False
    return True

def tratamientoStrings(cadena:str):
    cadenaTratada = cadena.replace("%"," % ").replace("/","  /  ").replace("**", "  ^^   ").replace("+","  +  ").replace("*","  *  ").replace("-","  - ").replace("  ","|")
    cadenaTratada = cadenaTratada.replace(" ","").replace("|"," ").replace("  "," ")
    cadenaSplit = cadenaTratada.split(" ")
    return cadenaSplit

def touringMachine(cadena):
    divicionAsignacion = cadena.split("=")
    print(divicionAsignacion)
    cadena = divicionAsignacion[1]
    cadenaAsignacion = divicionAsignacion[0]
    if(comprobacionAsignacion(cadenaAsignacion)==False or cadena==""):
        return "erro de sintaxis en la declaracion de variable"
    
    cadenaSplit = tratamientoStrings(cadena)
    print(cadenaSplit)
    cintaAuxiliar = []
    parentesisAbierto = 0
    parentesisCerrado = 0
    for variable in cadenaSplit:
        nuevaVariable,countParentesisAbireto,countParentesisCerrado=parentesisCount(variable) 
        cintaAuxiliar.append(nuevaVariable.replace(" ",""))
        parentesisAbierto = parentesisAbierto + countParentesisAbireto
        parentesisCerrado = parentesisCerrado + countParentesisCerrado
    cinta = llenarCinta(cintaAuxiliar)
    if(parentesisAbierto == parentesisCerrado):
        print("paso la prueba de los parentesis")
        resultado = touringGears(cinta)
        resultadoStrings = touringGearsString(cinta)
        if(resultadoStrings):
            print(resultado)
        else:
            print("error al cancatenar strings")
    else:
        print("no paso la prueba de los parentesis")
        return "Error en las operaciones de variables"
    return True

print(touringMachine(' value__ = "conchesumadre"+(55/2) * 5**2 + "tu jefa"'))






