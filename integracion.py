from os import pardir
import imports
import consoles
import operaciones
import asignaciones
from Automata.AutomaGeneral import initanAlysis


def analizarCodigo(codigo):
    listaImports = []
    codigoCopy = codigo.copy()
    for i in range(len(codigoCopy)):
        if(codigoCopy[i].__contains__("import")):
            listaImports.append(codigoCopy[i].replace("\n",""))
            codigoCopy[i]=""
    listaCodigo,estado = initanAlysis(codigoCopy)
    print(listaCodigo)
    if(estado == False):
        return "tienes un error en {} checa tus llaves"
    if(type(estado)==list):
        # print("errores pero se puede seguir")
        contador = 0
        variableRetorno = "tienes error en las lineas"
        for i in estado:
            if(contador==0):
                variableRetorno = variableRetorno+f' {i[0]} a la {i[1]}'
            else:
                variableRetorno = variableRetorno+f' ,{i[0]} a la {i[1]}'
            contador= contador+1
        print(variableRetorno)
        return variableRetorno
    if(estado == True):
        print("sin errores pero se puede seguir")
        lenImport = len(listaImports)
        print(lenImport)
        if(lenImport>0):
            for elemento in listaImports:
                if(not imports.checarImports(elemento)):
                    return f'checar la linea que contiene: {elemento}'
        
        for elemento in listaCodigo:
            if(asignaciones.comprobarAsignaciones(elemento)==True or consoles.checarConsoles(elemento)==True or operaciones.touringMachine(elemento)):
                return f"no se encontraron problemas"
            else:
                return f'error en {elemento}'      