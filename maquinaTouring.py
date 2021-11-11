import re
from string import punctuation

def comprobacionVariable(variable):
    validator = re.compile("([-]{0,1}[a-zA-Z0-9]([a-zA-Z0-9_])*)")
    match =validator.match(variable)
    try:
        valida = match.group()==variable
    except (TypeError, AttributeError):
        valida = False
    return  valida

def stringCount(variable:str):
    comillasDobles = variable.count('"')
    comillasSimples = variable.count("'")

    return comillasSimples+comillasDobles
    
def parentesisCount(variable:str):
    numeroParentesisAbierto = variable.count("(")
    numeroParentesisCerrado = variable.count(")")
    nuevaVariable = variable.replace("(","").replace(")","").replace("ñ","n")
    return nuevaVariable, numeroParentesisAbierto, numeroParentesisCerrado, stringCount(variable)   

def touringGears(cinta:list):
    print(cinta)
    comprobacionOperador = False
    operadores = ["+","/","-","%","**","*"]
    if(not comprobacionVariable(cinta[0])):
        print(cinta[0])
        return " error en una variable"
    for elemento in cinta:
        if(comprobacionOperador):
            validacionOperador = operadores.count(elemento)
            if(validacionOperador==0):
                print(elemento)
                return "un simbolo esta mal colocado o no existe"
            comprobacionOperador = False
        else:
            validacionVariable = comprobacionVariable(elemento)
            if(not validacionVariable):
                print(elemento)
                return "una variable no es valida"
            comprobacionOperador = True
    return "aceptado"
                
    
    

def touringMachine():
    cadena  = "-3 - 1 + 'hola como estas perro desgraciado' + ''hola + (1/5*(1))"
    cadenaTratada = cadena.replace("/"," / ").replace("**", " ** ").replace("+"," + ").replace("*"," * ").replace("  "," ")
    cadenaSplit = cadenaTratada.split(" ")
    cinta = []
    parentesisAbierto = 0
    parentesisCerrado = 0
    comillas = 0
    for variable in cadenaSplit:
        nuevaVariable,countParentesisAbireto,countParentesisCerrado,countComillas=parentesisCount(variable) 
        cinta.append(nuevaVariable.replace(" ",""))
        parentesisAbierto = parentesisAbierto + countParentesisAbireto
        parentesisCerrado = parentesisCerrado + countParentesisCerrado
        comillas = comillas +countComillas

    print(comillas%2)
        
    # if(parentesisAbierto == parentesisCerrado):
    #     print("paso la prueba de los parentesis")
    #     resultado = touringGears(cinta)
    #     print(resultado)
    # else:
    #     print("no paso la prueba de los parentesis")
        
    #     return "Error en las operaciones de variables"
    



touringMachine()
# print(punctuation)