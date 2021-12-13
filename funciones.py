#calcular disimilaridad entre documentos 

import math

#metodo para leer archivo
#ingreso el ruta del archivo
#salida lista con lineas del archivo [linea1,linea2,...]
def leerArchivo(rutaArchivo):
  archivo = open(rutaArchivo,"r")
  lineas = []
  for linea in archivo:
    lineas.append(linea)
  archivo.close()
  return lineas




#Eliminar comentario 
#entrada linea
#salida linea sin comentario o linea vacia
def eliminarComentarioLinea(linea):
  #linea a retornar
  ln=''
  if(35!=ord(linea[0])):
    for caracter in linea:
      if(35==ord(caracter)):
        break
      else:
        ln+=caracter
  return ln

#l1 = '#h#hola jeje'
#l2 = 'if x==2: #se utiliza para'
#print(eliminarComentarioLinea(l1))
#print(eliminarComentarioLinea(l2))

#Eliminacion de comentarios
#El simbolo(#) es comentario, por tanto, en ascii es 35
#Entrada lista [linea1,linea2,...] de lineas del codigo
#Se eliminara los comentarios
def eliminarComentariosLineas(lineas):
  for i in range(len(lineas)):
    l1 = eliminarComentarioLinea(lineas[i])
    lineas[i] = l1
  return lineas

#separar con espacios caracteres ejemplo de: a=2 -> a = 2
#entrada linea
#salida [token1,token2,...]
def separarCaracteresLinea(linea):
  l1 = ''
  for caracter in linea:
    #mira si es letra de A(65) a Z(90) o a(97) a z(122) o 0(48) a 9(57) o espacio(32) o punto(46)
    n = ord(caracter)
    if( (n>=65 and n<=90) or (n>=97 and n<=122) or (n>=48 and n<=57) or (n==32)):
      l1+=caracter
      #print(caracter)
      #print('letra')
    else:
      l1 = l1 +' '+caracter+' ' 
    
  lista = l1.split()
    
  return lista

#separar con espacios caracteres ejemplo de: a=2 -> a = 2
#entrada lista de lineas [linea1,linea2]
#salida lista con listas [[tokens de linea 1],[tokens de linea 2],...]
def separarCaracteresLineas(lineas):
  lista = []
  for linea in lineas:
    l1 = separarCaracteresLinea(linea)
    lista.append(l1)
  return lista


#entrada [token1,token2,...]
#salida True si hay print, False si no hay
def eliminarPrints(lista):  
  bandera = 'print' in lista
  return bandera

#metodo para concatenar tokens en una sola lista
#entrada [[token1,token2,...],[token1,token2,...],...]
#salida [token1,token2,token3,token4,...]
def concatenarTokensEnUnaLista(listasLineas):
  listaT = []
  for l1 in listasLineas:
    #eliminar prints
    if eliminarPrints(l1)==False:
      #print(l1)
      listaT+=l1

  return listaT

  #metodo para normalizar codigo
#entrada ruta del codigo
#salida [token1,token2,... tokens del codigo]
def tokensNormalizadosCodigo(ruta):
  lineas = leerArchivo(ruta)
  lineas = eliminarComentariosLineas(lineas)
  lista = separarCaracteresLineas(lineas)
  listaT = concatenarTokensEnUnaLista(lista)
  return listaT


#metodo para leer archivos
#entrada [ruta de archivo 1, ruta de archivo 2, ...]
#salida [ [token1,token2,tokens de archivo 1...] [token1,token2, tokens de archivo 2...]]
def normalizacionCodigos(listaRutas):
  listaTokensCod = []
  for ruta in listaRutas:
    #print(ruta)
    listaTokensCod.append(tokensNormalizadosCodigo(ruta))
  
  return listaTokensCod

#rutas1 = ['juan1.py','juan2.py']
#l = normalizacionCodigos(rutas1)
#print(l)

#Proyecto similitud entre codigos

#importar algunas librerias
#eliminar caracteres especiales
#import re 

#import math

#cargar libreria pandas para el manejo de dataFrames
#import pandas as pd














#metodo para hacer lista de palabras sin repeticion -> diccionario
def creacionDiccionario(cnt):
  lpsr = []
  
  #concatenar listas que estan en cnt en una sola 
  for lista in cnt:
    lpsr = lpsr + lista  
  
  #eliminar tokens repetidos de la lista
  lpsr1 = list(set(lpsr))

  return lpsr1


#cuenta tokens que hay en un documento 
#entrada1 diccionario de palabras
#entrada2 documento normalizado
#retorna lista con numero de tokens que hay en el documento
def numeroTokensDoc(diccionario,documento):
  #lista de numero de tokens que hay en el documento
  lista = []
  for tokenDic in diccionario:
    #numero de tokens que hay en el documento con el token del diccionario
    n = 0
    for tokenDoc in documento:
      #si son iguales se suma n
      if(tokenDic == tokenDoc):
        n+=1
    lista.append(n)
  return lista

#creacion de bolsa de palabras 
#entrada1 diccionario
#entrada2 documentos normalizados en lista
#salida diccionario (key, lista con numero de tokens que hay en el documento)
def creacionBolsaPalabras(diccionario,documentosNormalizados):
  bolsaPalabras = {'diccionario':diccionario}
  numeroDoc = 0
  for docNormalizado in documentosNormalizados:
    bolsaPalabras[numeroDoc]=numeroTokensDoc(diccionario,docNormalizado)
    numeroDoc += 1
  
  return bolsaPalabras 



#metodo para pesar cada tf
def pesarTF(tf):
  if(tf>0):
    return math.log10(tf)+1
  else:
    return 0


#calculo de pesos en la bolsa de palabras
#entrada bolsa de Palabras
#salida bolsa de palabras pesada wtf
def calculoWTF(bolsaPalabras):
  #n es el numero de tokens
  n = len(bolsaPalabras[0])
  for key in bolsaPalabras:
    #escoge todos los valores menos el diccionario y df en ser el caso
    if(key!='diccionario' and key!='df'):
      i=0
      for j in range(n):
        #variable a transformar
        tf = pesarTF(bolsaPalabras[key][j])
        #cambiando valor por pesado
        bolsaPalabras[key][j] = tf

  return bolsaPalabras



#calcular el modulo de un vector
#entrada una lista con numeros
#salida, valor del modulo
def calcularModuloVector(lista):
  #suma de cuadrados por elemento de la lista
  suma = 0
  for i in lista:
    suma += ((i)**2)

  #sacar la raiz cuadrada de la suma 
  modulo = suma**(1/2)
  return modulo

#se hace la matriz de vector
#entrada diccionar tf_idf
#salida diccionario con vectores normalizados
def normalizarVectores(bolsa):
  #numero de tokens 
  n = len(bolsa[0])
  
  for key in bolsa:
    if(key!='diccionario'):
      vector = bolsa[key]
      modulo = calcularModuloVector(vector)
      for j in range(n):
        uv = vector[j]/modulo
        bolsa[key][j]=uv
  
  return bolsa

#encontrar similitud entre dos vectores
#entrada dos vectores
#salida valor de similitud
def similitud(v1,v2):
  suma = 0
  n = len(v1)
  for i in range(n):
    suma += v1[i]*v2[i]
  return suma

#calcular triangular superior
#entrada lista de vectores
#retorna lista de valores de triangular superior (listas de las columnas)
def triangularSuperior(lista):
  triangular=[]
  n = len(lista)
  
  for i in range(1,n):
    columna = []
    for j in range(0,(i)):
      sim = similitud(lista[i],lista[j])
      columna.append(sim)
    triangular.append(columna)

  return triangular

#calcular triangular superior ingresando la bolsa de palabras vectorizada
#entrada bolsa de tf_idf en diccionario
#salida lista con listas de columnas de triangular superior
def calculoTriangularConVectores(vect):
  lista = []
  for key in vect:
    if(key!='diccionario'):
      lista.append(vect[key])
  tS = triangularSuperior(lista)
  return tS 


#reutilizando codigo llamando a metodos para dar como resultado 
#triangular superior de matriz de similitud con metodo vectorial
#entrada lista con documentos 
def calcularDisimilitudVectorial(listaRutas):
  #paso 1 normalizar las cadenas
  cadNorm = normalizacionCodigos(listaRutas)
  #paso 2 creacion del diccionario de tokens
  dic = creacionDiccionario(cadNorm)
  #paso 3 creacion bolsa de palabras
  bP = creacionBolsaPalabras(dic, cadNorm)
  #paso 4 pesado de palabras 
  wtf = calculoWTF(bP)
 
  #paso 5 calculo de vectorizacion de tf_idf
  vect = normalizarVectores(wtf)
  #paso 6 calcular matriz de disimilitud, triangular superior
  ts1 = calculoTriangularConVectores(vect)
  #retornar triangular superior
  return ts1














#obtener primera fila de comparaciones
#se obtiene la comparacion entre d0 con d1, d0 con d2,...
#entrada triangular superior
#salida lista con comparacion [d0 con d1, d0 con d2, ...]
def obtenerFilaComparacionConD0(triangularVectorial):
  fila = []
  for i in triangularVectorial:
    #print(i[0])
    fila.append(i[0])
  return fila

#eliminar en la triangular la comparacion con d0
#entrada triangular superior [[d0-d1],[d0-d2,d1-d2]]
#salida triangular superior [[d1-d2],[....]]
def eliminarComparacionConD0(triangularVectorial):
  triangularVectorial.pop(0)
  for lista in triangularVectorial:
    lista.pop(0)
  return triangularVectorial


#encontrar distancia entre dos disimilitudes
#entrada dos valores
#salida valor de la distancia
def distancia(v1,v2):
  distancia = v2 - v1
  if distancia<0:
    distancia = distancia * (-1)
  return distancia

#calcular triangular superior
#entrada lista de vectores
#retorna lista de valores de triangular superior (listas de las columnas)
def triangularSuperiorDistancia(lista):
  triangular=[]
  n = len(lista)
  
  for i in range(1,n):
    columna = []
    for j in range(0,(i)):
      sim = distancia(lista[i],lista[j])
      columna.append(sim)
    triangular.append(columna)

  return triangular



#crear metodo para definir si dos codigos son similares en forma
#se pondra 1 si son similares en forma, y 0 si no son similares
#se tiene en cuenta que si en comparacion entre documentos es mayor a 0.70 y
#si en distancia de similitud con documento base  

#metodo para definir si son similares entre el valor de similitud y valor de distancia
#entrada (valorSimilitud,valorDistancia)
#salida Es similar, No es similar
def similarEnForma(valorSimilitud,valorDistancia):
  mns = 'No es similar'
  if((valorSimilitud>0.999999) and (valorDistancia<0.0000001)):
    mns = 'Igual'
  elif(valorSimilitud>=0.70):
    if(valorDistancia<=0.01):
      mns = 'Es similar'
  return mns

#entrada: triangular distnacia, triangular Vectorial
#salida: triangular con: [Similar o No similar]
def crearTriangularSimilarEnForma(triangularDistancia,triangularVectorial):
  n = len(triangularDistancia)
  triangularSimilar = []
  for i in range(n):
    elementoTriangular = []
    for j in range(len(triangularDistancia[i])):
      #calcular mns
      mns = similarEnForma(triangularVectorial[i][j],triangularDistancia[i][j])
      elementoTriangular.append(mns)
    triangularSimilar.append(elementoTriangular)
  return triangularSimilar





#####################
#Jaccard

####Jaccard

#cuenta tokens que hay en un documento 1 si esta en el documento, 0 si no esta 
#entrada1 diccionario de palabras
#entrada2 documento normalizado
#retorna lista con numero de tokens(1 o 0) que hay en el documento
def presenciaTokensDoc(diccionario,documento):
  #lista de numero (0,1) de tokens que hay en el documento
  lista = []
  for tokenDic in diccionario:
    #numero de tokens que hay en el documento con el token del diccionario
    n = 0
    for tokenDoc in documento:
      #si son iguales se suma n
      if(tokenDic == tokenDoc):
        n+=1
      #si es uno sale del bucle por que ya existe ese token en el documento
      if(n==1):
        break
    lista.append(n)
  return lista

#creacion de bolsa de palabras binaria
#entrada1 diccionario
#entrada2 documentos normalizados en lista
#salida diccionario (key, lista con numero de tokens que hay en el documento)
def creacionBolsaPalabrasBinaria(diccionario,documentosNormalizados):
  bolsaPalabras = {'diccionario':diccionario}
  numeroDoc = 0
  for docNormalizado in documentosNormalizados:
    bolsaPalabras[numeroDoc]=presenciaTokensDoc(diccionario,docNormalizado)
    numeroDoc += 1
  
  return bolsaPalabras 

#metodo para calcular jaccard de dos documentos 
#entrada dos listas 
#salida jaccard 
def calculoJaccard(l1,l2):
  #numero para interseccion
  overlap= 0
  #numero de no interseccion
  noI = 0
  #numero de elementos de lista
  n = len(l1)
  i = 0 
  for i in range(n):
    #si es uno en ambos casos se suma a overlap
    #si es uno en cualquiera se suma en noI
    #si ambos son ceros no suma
    suma = l1[i]+l2[i]
    if(suma==2):
      overlap+=1
    elif(suma==1):
      noI+=1
  
  #se calcula el jaccard
  #para determinar jaccard se divide las intersecciones 
  #por el total de elementos(los que se interseccionan y 
  #los que no se interseccionan)
  jaccard = overlap/(noI+overlap)

  return jaccard

#calcular triangular superior para comparacion de Jaccard
#entrada lista de binarios
#retorna lista de valores de triangular superior (listas de las columnas)
def triangularSuperiorJaccard(lista):
  triangular=[]
  n = len(lista)
  
  for i in range(1,n):
    columna = []
    for j in range(0,(i)):
      sim = calculoJaccard(lista[i],lista[j])
      columna.append(sim)
    triangular.append(columna)

  return triangular

#calcular triangular superior jaccard ingresando la bolsa de palabras binaria
#entrada bolsa binaria en variable diccionario
#salida lista con listas de columnas de triangular superior
def calculoTriangularJaccard(bolsaBinaria):
  lista = []
  for key in bolsaBinaria:
    if(key!='diccionario'):
      lista.append(bolsaBinaria[key])
  tS = triangularSuperiorJaccard(lista)
  return tS 



#recoleccionando los metodos para sacar directamente la comparacion de 
#jaccard de la matriz la triangular superior en listas
#entrada lista de documentos
def calcularDisimilitudJaccard(listaRutas):
 #paso 1 normalizar las cadenas
  cadNorm = normalizacionCodigos(listaRutas)
  #paso 2 creacion del diccionario de tokens
  dic = creacionDiccionario(cadNorm)
  #Paso 3, creacion de bolsa de palabras binaria
  bolsaPalabrasBinaria = creacionBolsaPalabrasBinaria(dic, cadNorm)
  #Paso 4, calcular la comparacion de jaccard 
  #Saca una triangular superior de la comparacion
  triangularBinaria = calculoTriangularJaccard(bolsaPalabrasBinaria)

  return triangularBinaria



######################


##########
#manejo de suma de triangular como dataframe
######Parte de pasar de una lista de columnas(listas) a un dataFrame

##parte de disimilitud
##########
#manejo de suma de triangular como dataframe
######Parte de pasar de una lista de columnas(listas) a un dataFrame


#######metodo general
##Devolver en lista de listas ejemplo [[fila1],[fila2],...]
def retornarFilasEnListas(matriz):
  filas = []
  n = len(matriz)
  for i in range(n):
    fila = []
    for j in range(n):
      fila.append(matriz[j][i])
    filas.append(fila)    
  return filas

#############Jaccard y Vectorial

#crear matriz con 1 diagonal principal
def crearMatriz1DiagonalP(n):
  matriz = []
  for i in range(n):
    fila=[]
    for j in range(n):
      if(i==j):
        fila.append(1)
      else:
        fila.append(0)
    matriz.append(fila)
  return matriz

#entrada lista con columnas de matriz superior (matriz triangular superios)
#salida dataframe como matriz de disimilitud
def retornarDataFrameMatrizDisimilitud(mts):
  #se definen el numero de filas y columnas (al ser [n x n])
  #se suma 1 al tener columnas unicamente de triangular superior
  n = len(mts) + 1
  #se crea matriz -> lista con listas (columnas) con unos
  #matriz = [[0,1,2],[10,11,12],[20,21,22]]
  matriz = crearMatriz1DiagonalP(n)
  for i in range(1,n):
      for j in range(0,i):
        matriz[i][j] = (mts[(i-1)][j])

  for j in range(1,n):
    for i in range(0,j):
      matriz[i][j]=matriz[j][i]

  #creando diccionario para crear el dataframe
  dic={}
  i=0
  for columna in matriz:
    dic[i]=columna
    i+=1
  #crear dataframe 
  df = pd.DataFrame(dic)
  #print(df)
  return df



#entrada lista con columnas de matriz superior (matriz triangular superios)
#salida columnas ejemplo [[fila1],[fila2],...]
def retornarFilasDisimilitudVectorial(mts):
  #se definen el numero de filas y columnas (al ser [n x n])
  #se suma 1 al tener columnas unicamente de triangular superior
  n = len(mts) + 1
  #se crea matriz -> lista con listas (columnas) con unos
  #matriz = [[0,1,2],[10,11,12],[20,21,22]]
  matriz = crearMatriz1DiagonalP(n)
  for i in range(1,n):
      for j in range(0,i):
        matriz[i][j] = (mts[(i-1)][j])

  for j in range(1,n):
    for i in range(0,j):
      matriz[i][j]=matriz[j][i]
 
  df = retornarFilasEnListas(matriz)
  #print(df)
  return df



##############Distancias entre documentos en comparacion con documento base
#parte de distancias 
#crear matriz con 0 diagonal principal
def crearMatriz1DiagonalPrincipal0(n):
  matriz = []
  for i in range(n):
    fila=[]
    for j in range(n):
      if(i==j):
        fila.append(0)
      else:
        fila.append(0)
    matriz.append(fila)
  return matriz

#entrada lista con columnas de matriz superior (matriz triangular superios)
#salida dataframe como matriz de disimilitud
def retornarDataFrameMatrizDistancia(mts):
  #se definen el numero de filas y columnas (al ser [n x n])
  #se suma 1 al tener columnas unicamente de triangular superior
  n = len(mts) + 1
  #se crea matriz -> lista con listas (columnas) con unos
  #matriz = [[0,1,2],[10,11,12],[20,21,22]]
  matriz = crearMatriz1DiagonalPrincipal0(n)
  for i in range(1,n):
      for j in range(0,i):
        matriz[i][j] = (mts[(i-1)][j])

  for j in range(1,n):
    for i in range(0,j):
      matriz[i][j]=matriz[j][i]

  #creando diccionario para crear el dataframe
  dic={}
  i=0
  for columna in matriz:
    dic[i]=columna
    i+=1
  #crear dataframe 
  df = pd.DataFrame(dic)
  #print(df)
  return df


#entrada lista con columnas de matriz superior (matriz triangular superios)
#salida columnas ejemplo [[fila1],[fila2],...]
def retornarFilasDMarizDistancia(mts):
  #se definen el numero de filas y columnas (al ser [n x n])
  #se suma 1 al tener columnas unicamente de triangular superior
  n = len(mts) + 1
  #se crea matriz -> lista con listas (columnas) con unos
  #matriz = [[0,1,2],[10,11,12],[20,21,22]]
  matriz = crearMatriz1DiagonalPrincipal0(n)
  for i in range(1,n):
      for j in range(0,i):
        matriz[i][j] = (mts[(i-1)][j])

  for j in range(1,n):
    for i in range(0,j):
      matriz[i][j]=matriz[j][i]
 
  df = retornarFilasEnListas(matriz)
  #print(df)
  return df

##########


#parte de similitud en forma 
#crear matriz con 'Similar' en diagonal principal
def crearMatriz1DiagonalPrincipalSimilar(n):
  matriz = []
  for i in range(n):
    fila=[]
    for j in range(n):
      if(i==j):
        fila.append('Igual')
      else:
        fila.append(0)
    matriz.append(fila)
  return matriz

#entrada lista con columnas de matriz superior (matriz triangular superios)
#salida dataframe como matriz de similaridad o no similaridad
def retornarDataFrameMatrizSimilar(mts):
  #se definen el numero de filas y columnas (al ser [n x n])
  #se suma 1 al tener columnas unicamente de triangular superior
  n = len(mts) + 1
  #se crea matriz -> lista con listas (columnas) con unos
  #matriz = [[0,1,2],[10,11,12],[20,21,22]]
  matriz = crearMatriz1DiagonalPrincipalSimilar(n)
  for i in range(1,n):
      for j in range(0,i):
        matriz[i][j] = (mts[(i-1)][j])

  for j in range(1,n):
    for i in range(0,j):
      matriz[i][j]=matriz[j][i]

  #creando diccionario para crear el dataframe
  dic={}
  i=0
  for columna in matriz:
    dic[i]=columna
    i+=1
  #crear dataframe 
  df = pd.DataFrame(dic)
  #print(df)
  return df


#entrada lista con columnas de matriz superior (matriz triangular superios)
#salida columnas ejemplo [[fila1],[fila2],...]
def retornarFilasDMarizSimilar(mts):
  #se definen el numero de filas y columnas (al ser [n x n])
  #se suma 1 al tener columnas unicamente de triangular superior
  n = len(mts) + 1
  #se crea matriz -> lista con listas (columnas) con unos
  #matriz = [[0,1,2],[10,11,12],[20,21,22]]
  matriz = crearMatriz1DiagonalPrincipalSimilar(n)
  for i in range(1,n):
      for j in range(0,i):
        matriz[i][j] = (mts[(i-1)][j])

  for j in range(1,n):
    for i in range(0,j):
      matriz[i][j]=matriz[j][i]
 
  df = retornarFilasEnListas(matriz)
  #print(df)
  return df


def imprimirFilas(filas):
  for i in filas:
    print(i)

#metodo 
#entrada nombre de archivos ([nombre1,nombre2,...])
#salida [raiz/nombre1,raiz/nombre2]
def definiendoRutaExacta(nombres,raiz):
  dir = []
  for ruta in nombres:
    direccion = str(raiz) + str(ruta)
    #print(direccion)
    dir.append(direccion)
  return dir



#metodo para crear encabezado
#entrada lista de filas
#salida lista ejemplo ['c1','c2','c3',...]
def crearEncabezadoMatriz(filas):
  filaEncabezado = []
  filaEncabezado.append('')
  n = len(filas)
  for i in range(n):
    nombreCol = 'c'+str(i+1)
    filaEncabezado.append(nombreCol)
  return filaEncabezado


#metodo que define el nombre de la matriz
#1: Modelo Espacio Vectorial
#2: Modelo de Jaccard
#3: Moledo para ver si es similar en forma
def nombreMatriz(tipo):
  nombre = ''
  if(tipo==1):
    nombre='Modelo Espacio Vectorial'
  if(tipo==2):
    nombre='Modelo de Jaccard'
  if(tipo==3):
    nombre='Moledo para ver si es similar en forma'
  return nombre

#metodo para agregar encabezado en cada fila 
#ejemplo[[c1,x,x,...],[c2,x,x,...],...]
#filas 
def insertarEncabezadoAFilas(filas):
  n = len(filas)
  for i in range(n):
    mns = 'c'+str(i+1)
    filas[i].insert(0,mns)


#metodo para redondear con n decimales 
#valores de las filas 
#entrada filas [[fila1],[fila2],...]
#salida valores redondeados
def redondearFilas(filas):
  nFilas = len(filas)
  nCol = len(filas[0])
  for i in range(nFilas):
    for j in range(nCol):
      filas[i][j] = round(filas[i][j],5)

#metodo para obtener filas en listas de cada matriz
#matriz vectorial, matriz jaccard, matriz similar
#entrada (nombre de archivos, raiz(ejemplo ../uploads/) ,que tipo de matriz desea calcular)
#tipo de matriz: 1->Vectoria, 2->Jaccard, 3->Similar
def calcularMatrizSimlitud(nombresArchivos,raiz,tipo):
  #se definen las rutas exactas de los archivos
  listaRutas = definiendoRutaExacta(nombresArchivos,raiz)

  filas = []

  #calculando matriz dependiendo del tipo
  #1 Vectorial
  if(tipo==1):
    triangularVectorial = calcularDisimilitudVectorial(listaRutas)
    triangularVectorial = eliminarComparacionConD0(triangularVectorial)
    filas = retornarFilasDisimilitudVectorial(triangularVectorial)
    redondearFilas(filas)
  #2 Jaccard
  if(tipo==2):
    triangularJaccard = calcularDisimilitudJaccard(listaRutas)
    triangularJaccard = eliminarComparacionConD0(triangularJaccard)
    filas = retornarFilasDisimilitudVectorial(triangularJaccard)
    redondearFilas(filas)
  #3 Si es similar o no (matriz)
  if(tipo==3):
    triangularVectorial = calcularDisimilitudVectorial(listaRutas)
    #obtener la fila 0
    fila = obtenerFilaComparacionConD0(triangularVectorial)
    #eliminar fila 0
    triangularVectorial = eliminarComparacionConD0(triangularVectorial)
    #calcular triangular superior de similitudes
    triangularDistancia = triangularSuperiorDistancia(fila)
    #calcular triangular si es SIMILAR o NO SIMILAR
    triangularSimilar = crearTriangularSimilarEnForma(triangularDistancia,triangularVectorial)
    filas = retornarFilasDMarizSimilar(triangularSimilar)

  insertarEncabezadoAFilas(filas)
  return filas

###########Manejo de nombres de archivos###################
#Se obtendra [nombre,formato]
def obtenerNombreFormato(nombre_archivo):
  lista = []
  nombre = ''
  formato = ''
  bandera = True
  for caracter in nombre_archivo:
    cod = ord(caracter)
    
    if cod == 46 and bandera==True:
      bandera = False
    if bandera == True:
      nombre += caracter
    else:
      formato += caracter
  return [nombre,formato]  




def agregarArchivoLista(lista,nombre_archivo):
  nombre = nombre_archivo
  i = 1
  bandera = True
  l = obtenerNombreFormato(nombre_archivo)
  
  while bandera:
    if nombre in lista: 
      i+=1
      nombre = l[0] + str(i) + l[1]      
    else:
      bandera = False
  return nombre



  