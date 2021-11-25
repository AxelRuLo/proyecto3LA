import re


def comprobacionConsole(variable):
    variable = variable.replace(" ","").replace("  ","")
    comillaDoble = '"'
    erVariableContenido = "[(]((((["+comillaDoble+"])[a-zA-Z0-9*+%(),-.'/:;<=>?@[\]^_`{|}~]*(["+comillaDoble+"]))|((['])[a-zA-Z0-9*+()%,-."+comillaDoble+"/:;<=>?@[\]^_`{|}~]*(['])))[,]{0,1}|([-]{0,1}[0-9]*[.]{0,1}[0-9])[,]{0,1}|([a-zA-Z]+[0-9_a-zA-Z])([(][)]){0,1}[,]{0,1}|((([-]{0,1}[0-9]+[.]{0,1}[0-9]*|[-]{0,1}[a-zA-Z]+[0-9]*[a-zA-Z0-9_]*)[/*%+-]{0,1})+))*[)]"
    erConsole = "(console.assert())|"
    erConsole = erConsole+"(console.count("+erVariableContenido+"))|"
    erConsole = erConsole+"(console.debug("+erVariableContenido+"))|"
    erConsole = erConsole+"(console.dir("+erVariableContenido+"))|"
    erConsole = erConsole+"(console.dirxml("+erVariableContenido+"))|"
    erConsole = erConsole+"(console.error("+erVariableContenido+"))|"
    erConsole = erConsole+"(console.groupCollapsed([(]['][a-zA-Z0-9]+['][)]))|"
    erConsole = erConsole+"(console.group([(](['][a-zA-Z0-9]+['])*[)]))|"
    erConsole = erConsole+"(console.groupEnd([(](['][a-zA-Z0-9]+['])*[)]))|"
    erConsole = erConsole+"(console.info("+erVariableContenido+"))|"
    erConsole = erConsole+"(console.log("+erVariableContenido+"))|"
    erConsole = erConsole+"(console.table("+erVariableContenido+"))|"
    erConsole = erConsole+"(console.time("+erVariableContenido+"))|"
    erConsole = erConsole+"(console.warn("+erVariableContenido+"))|"
    erConsole = erConsole+"(alert("+erVariableContenido+"))"

    validator = re.compile(erConsole)
    match =validator.match(variable)
    try:
        valida = match.group()==variable
    except (TypeError, AttributeError):
        valida = False
    return  valida

def checarConsoles(cadena:str):
    tamañoCadena = len(cadena)
    if(cadena[tamañoCadena-1]==";"):
        cadena = cadena[0:tamañoCadena-1]
    resultado = comprobacionConsole(cadena)
    return resultado


print(checarConsoles("                        console.log('{ str: Algn texto, id: 5  }',var);"))