global contents
path = "./doc.txt"
file = open(path, "r")
contents = file.readlines()
lineas = len(contents)
file.close()


llaves = []

def recorrerLlaves():
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
        print(llaves)
    else:
        print("error de sintaxis ")

def convertString(value):
    str = ''
    for x in value:
        str += x 
    return str

#  while(i < 10){ifi%2console.log'Numero PAR'elseconsole.log'Numero IMPAR'i++console.log(i)}
def subStringConcatenacion():
    
    subStringEvaluar = []
    for valor in llaves:
        
        aux = contents[valor[0]:valor[1]+1]
        substr = aux[1:len(aux)-1]

        new_string = convertString(substr)
        new_string = new_string.rstrip('\n') #<-- eliminate line breaks
        
        new_string = new_string.replace('(', '').replace(')','').replace('{','').replace('}','').replace(' ', '').replace('\n', '')
        # print(substr)

        concat_string = contents[valor[0]] + new_string + contents[valor[1]]
        concat_string = concat_string.replace('\n', '').replace(" ","").replace('\t', '').replace('"', "'")
        concat_string = concat_string.rstrip().lstrip()
        print(concat_string)
        subStringEvaluar.append(concat_string)
        
recorrerLlaves()
subStringConcatenacion()