import re
# [a-zA-Z,]*|
def comprobacionImport(variable:str):
    variable = variable.strip()
    print(variable)
    erVariableSimple = "(import[\s]([a-zA-Z]*)[\s]from[\s][']([a-zA-Z/-]*)['])"
    erVariableSimpleAs = "|(import[\s]([*]([\s]as[\s][a-zA-Z]*))[\s]from[\s](['][a-zA-Z-/.]*[']))"
    erVariableLlaves = "|(import[\s][{]([\\s]*[a-zA-Z0-9]+[,]{0,1}[\s]*|[\s]*[a-zA-Z0-9]+[\s]as[\s][a-zA-Z]+[0-9]*[a-zA-Z][,]{0,1}[\s])*[}][\s]from[\s](['][0-9a-zA-Z-/.]*[']))"
    erVariableRequire = "|(import[\s][a-zA-Z]+[\s]*[=][ ]*(require)[(][']([a-zA-Z]+)['][)])"
    validator = re.compile(erVariableSimple+erVariableSimpleAs+erVariableLlaves+erVariableRequire)
    match =validator.match(variable)
    try:
        valida = match.group()==variable
    except (TypeError, AttributeError):
        valida = False
    return  valida

def checarImports(cadena:str):
    if(len(cadena)==0):
        return False
    cadena = cadena.strip()
    tamañoCadena = len(cadena)
    if(cadena[tamañoCadena-1]==";"):
        cadena = cadena[0:tamañoCadena-1]
    cadena = cadena.replace('"',"'")
    if(cadena.count("import")<1 or cadena.count(",,")>0):
        print("no es un import")
        return False
    if(not comprobacionImport(cadena)):
        return False
    cadenaArray = cadena.split(",")
    if(cadenaArray.count("import")>1 or cadenaArray.count("as")>1 or cadenaArray.count("from")>1):
        
        return False
    return True

# checarImports("import re"
# print(checarImports("import defaultExport from 'module-name';"))
# print(checarImports("import function1 from './modules/module.js';"))
print(comprobacionImport("import asdf from 'asdfasf'"))