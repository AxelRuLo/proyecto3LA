from unicodedata import normalize
import Automata.AutomataEstructura as automata

llaves = []
subStringEvaluar = []

def recorrerLlaves():
    global llaves
    llaves = []
    countInicio = 0
    countFinal = 0

    for i in range(lineas):
        if(contents[i].__contains__("{")):
            countInicio = countInicio + 1
        if(contents[i].__contains__("}")):
            countFinal = countFinal +1
    if(countInicio == countFinal):
        codigo = contents.copy()
        for j in range(countInicio):
            llave = []
            inicio = 0
            for i in range(lineas):
                if(codigo[i].__contains__("{")):
                    inicio = inicio+1
                    if(inicio == 1):
                        llave.append(i)
                elif(codigo[i].__contains__("}")):
                    if(inicio == 1):
                        # quiere decir que es su llave de cierre
                        llave.append(i)
                    else:
                        inicio = inicio-1
            llaves.append(llave)
            codigo[llave[0]]= codigo[llave[0]].replace("{","")
            codigo[llave[1]]= codigo[llave[1]].replace("}","")
        return True
    else:
        return False

def convertString(value):
    str = ''
    for x in value:
        str += x 
    return str

def subStringConcatenacion():
    global subStringConcatenacion
    subStringEvaluar = []
    trans_tab = dict.fromkeys(map(ord, u'\u0301\u0308'), None)
    
    for valor in llaves:
        
        aux = contents[valor[0]:valor[1]+1]
        substr = aux[1:len(aux)-1]

        new_string = convertString(substr)
        new_string = new_string.rstrip('\n') #<-- eliminate line breaks
        
        new_string = new_string.replace('(', '').replace(')','').replace('{','').replace('}','').replace(' ', '').replace('\n', '')
        

            
        concat_string = contents[valor[0]] + new_string + contents[valor[1]]
        concat_string = concat_string.replace('\n', '').replace(" ","").replace('\t', '').replace('"', "'").replace("\\n","").replace("\\t","").replace("\\","")
        concat_string = concat_string.rstrip().lstrip()
        concat_string =  normalize('NFKC', normalize('NFKD', concat_string).translate(trans_tab))
        # print(concat_string)
        subStringEvaluar.append(concat_string)
    
    for val in range(len(subStringEvaluar)):
        resp = automata.comprobacion(subStringEvaluar[val])
        llaves[val].append(resp)   
    
def limpieza():
    limpiar = llaves.copy()
    codigo = contents.copy()

    for i in range (len(limpiar)):
        if(limpiar[i][2] != False):
            tipo_dato = limpiar[i][2][1]
            if(tipo_dato == "object"):
                for j in range(limpiar[i][0],limpiar[i][1]+1):
                    codigo[j]=""
                
            elif(tipo_dato == "switch"):
                for j in range(limpiar[i][0],limpiar[i][1]+1):
                    if(j == limpiar[i][0]):
                        codigo[j]=""
                    if(j == limpiar[i][1]):
                        codigo[j]=""
                    if(codigo[j].__contains__("case")):
                        codigo[j]=""
                    if(codigo[j].__contains__("default")):
                        codigo[j]=""
                    if(codigo[j].__contains__("break")):
                        codigo[j]=""

            elif(tipo_dato == "class"):
                for j in range(limpiar[i][0],limpiar[i][1]+1):
                    if(j == limpiar[i][0]):
                        codigo[j]=""
                    if(j == limpiar[i][1]):
                        codigo[j]=""
                    if(codigo[j].__contains__("{")):
                        codigo[j]=""
                    if(codigo[j].__contains__("}")):
                        codigo[j]=""

            else:
                for j in range(limpiar[i][0],limpiar[i][1]+1):
                    if(j == limpiar[i][0]):
                        codigo[j]=""
                    if(j == limpiar[i][1]):
                        codigo[j]=""
                        
    trans_tab = dict.fromkeys(map(ord, u'\u0301\u0308'), None)
    for j in range(len(codigo)):
        # codigo[j]=codigo[j].replace('\n', '').replace(" ","").replace('\t', '').replace('"', "'").replace("\\n","").replace("\\t","").replace("\\","")
        codigo[j] = codigo[j].rstrip().lstrip()
        codigo[j] =  normalize('NFKC', normalize('NFKD', codigo[j]).translate(trans_tab))
    while '' in codigo:
        codigo.remove('')
    return codigo

def catchError():
    list_errores =[]
    for valor in llaves:
        if(valor[2] == False):
            list_errores.append(valor)
    return list_errores
            
def initanAlysis(text_codigo):
    global contents
    contents = text_codigo
    
    global lineas
    lineas = len(contents)
    resp_llave=recorrerLlaves()
    if(resp_llave):
        
    # respuesta de llave puede traer verdadero o falso
    # Falso cuando hay error en llaves 
    # verdadero cuadno puede pasar a realizar la busqueda de resultados 
        subStringConcatenacion()
        list_errores=catchError()
        codigo = limpieza()
        if(len(list_errores)>0):
            return codigo,list_errores
        else:
            return codigo
    return resp_llave
