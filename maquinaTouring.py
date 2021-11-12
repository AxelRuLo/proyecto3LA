import re
from string import punctuation

# ([-]{0,1}[a-zA-Z0-9]([a-zA-Z0-9_])*)|
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


def parentesisCount(variable:str):
    numeroParentesisAbierto = variable.count("(")
    numeroParentesisCerrado = variable.count(")")
    nuevaVariable = variable.replace("(","").replace(")","").replace("ñ","n")
    return nuevaVariable, numeroParentesisAbierto, numeroParentesisCerrado

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
    

def touringMachine():
    cadena  = "-35 - variable - 3 + 'holacomo estas perro desgraciado' - (-1/5*(-1))"
    cadenaTratada = cadena.replace("%"," % ").replace("/","  /  ").replace("**", "  **  ").replace("+","  +  ").replace("*","  *  ").replace("-","  - ").replace("  ","|").replace("   ","?").replace(" ","").replace("|"," ")
    print(cadenaTratada)
    cadenaSplit = cadenaTratada.split(" ")
    cintaAuxiliar = []
    parentesisAbierto = 0
    parentesisCerrado = 0
    for variable in cadenaSplit:
        nuevaVariable,countParentesisAbireto,countParentesisCerrado=parentesisCount(variable) 
        cintaAuxiliar.append(nuevaVariable.replace(" ",""))
        parentesisAbierto = parentesisAbierto + countParentesisAbireto
        parentesisCerrado = parentesisCerrado + countParentesisCerrado
    cinta = llenarCinta(cintaAuxiliar)
    print(cinta)
    

        
    if(parentesisAbierto == parentesisCerrado):
        print("paso la prueba de los parentesis")
        resultado = touringGears(cinta)
        print(resultado)
    else:
        print("no paso la prueba de los parentesis")
        
        return "Error en las operaciones de variables"
    



touringMachine()
# print(punctuation)





