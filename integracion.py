
from Automata.AutomaGeneral import initanAlysis


def analizarCodigo(codigo):
    codigoCopy = codigo.copy()
    for i in range(len(codigoCopy)):
        if(codigoCopy[i].__contains__("import")):
            codigoCopy[i]=""
    # resultadoAnalizisCiclos,listaErrores = initanAlysis(codigoCopy)
    print(initanAlysis(codigoCopy))
    # print(listaErrores)