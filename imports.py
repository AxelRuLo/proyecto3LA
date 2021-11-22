import re
from unicodedata import normalize
# [a-zA-Z,]*|
def comprobacionImport(variable):
    trans_tab = dict.fromkeys(map(ord, u'\u0301\u0308'), None)
    variable =  normalize('NFKC', normalize('NFKD', variable).translate(trans_tab))
    print(variable)
    erVariableSimple = "(import[ ]([a-zA-Z]*)[ ]from[ ](['][a-zA-Z-/.]*[']))"
    erVariableSimpleAs = " |(import[ ]([*]([ ]as[ ][a-zA-Z]*))[ ]from[ ](['][a-zA-Z-/.]*[']))"
    erVariableLlaves = "|(import[ ][{]([a-zA-Z]+[,]{0,1}|[a-zA-Z]+[ ]as[ ][a-zA-Z]+[,]{0,1})*[}][ ]from[ ](['][a-zA-Z-/.]*[']))"

    validator = re.compile(erVariableSimple+erVariableSimpleAs+erVariableLlaves)
    match =validator.match(variable)
    try:
        valida = match.group()==variable
    except (TypeError, AttributeError):
        valida = False
    return  valida

def checarImports(cadena:str):
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

# checarImports("import re")
print(checarImports("import * as dis from 'module-name';"))