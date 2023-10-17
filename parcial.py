import random
#Se crea la matriz vacia M1
M1=[]
#Se crea el for donde se van a agregar filas y columnas a la matriz
for f in range (0,5):
  #Se agrega una nueva fila
  M1.append([])
  for c in range (0,5):
    #Dentro de la fila c se agregan 5 numeros aleatorios de 100 a 200
    M1[f].append(random.randint(100,200))
#Se imprime la matriz
print(M1)

#Se crea matriz vacia M2
M2=[]

for f in range (0,5):
  M2.append([])
  #Aqui se define por que numero se va a elevar cada columna, si es impar la columna se eleva por 2, si es par se eleva por 4.
  if (f+1) % 2 == 0:
    elevar=4
  else:
    elevar=2

  for c in range (0,5):
    #Aqui se agrega a las filas de la Matriz M2 cada columna de M1 elevado a la 2 o a la 4 dependiendo si la columna es par o impar
    M2[f].append(M1[c][f]**elevar)

#Se imprime la matriz M2
print(M2)

#Vector de la suma de las filas de la matriz 1
VSM1=[]
for i in range(0, 5):
  #La funcion sum() devuelve la suma de los elementos de una fila
  VSM1.append(sum(M1[i]))
print(VSM1)

#Vector de la suma de los elementos de cada columna de la matriz 2
VSM2=[]
for f in range(0, 5):
  #Se crea la variable sum que va a ser la sumatoria de los elementos de cada columna de la matriz 2
  suma=0
  for c in range (0,5):
    #Se hace la sumatoria de cada elemento cada columna de la matriz 2
    suma=suma+M2[c][f]
  #se guarda el vector VSM2 la sumatoria de cada columna de la matriz 2
  VSM2.append(suma)

print(VSM2)

#se crea la M3 que es la matriz diferencia entre M2-M1
M3=[]
#Con los dos for anidados se recorren las matrices en filas y columnas y se realiza la resta
for f in range(0,5):
  resta=0
  M3.append([])
  for c in range(0,5):
#se realiza la resta de Matrices entre M2-M1 en cada posicion y el resultado se guarda en resta
    resta= M2[f][c]-M1[f][c]
    #se guarda el resultado de la resta en la matriz M3
    M3[f].append(resta)

print(M3)

#Matriz de mmultiplicar una matriz por un numero
M4=[]
#numero por el cual multiplicamos la matriz
numero=2
for f in range (0,5):
  multiplicacion=0
  M4.append([])
  for c in range (0,5):
    multiplicacion=numero*M1[f][c]
    M4[f].append(multiplicacion)
print (M4)

#Suma de diagonal de matriz 1
SD=0
for f in range (0,5):
  SD=SD+M1[f][f]
print (SD)

#Suma de diagonal inversa de matriz 2
SI=0
for f in range (0,5):
    SI=SI+M2[((4-f))][f]
print(SI)

MPr=[[1,2],[3,4]]
MPr2=[[1,1],[0,2]]

#Multiplicacion de dos matrices
Mmultiplicacion=[[0,0],[0,0]]
for f in range(0,2):
  for c in range(0,2):
    suma=0
    for m in range(0,2):
      multiplicacion=(MPr[f][m]*MPr2[m][c])
      suma=suma+multiplicacion
    Mmultiplicacion[f][c]=suma
print(Mmultiplicacion)

media=0
for f in range(0,2):
  media+=sum(Mmultiplicacion[f])
media=media/4
print(media)

#Multiplicacion de dos matrices con M1 y M2
Mmultiplicacion2=[[0]*5]*5
for f in range(0,5):
  for c in range(0,5):
    suma=0
    for m in range(0,5):
      multiplicacion=(M1[f][m]*M2[m][c])
      suma=suma+multiplicacion
    Mmultiplicacion2[f][c]=suma
print(Mmultiplicacion2)

media=0
for f in range(0,2):
  media+=sum(Mmultiplicacion[f])
media=media/4
print(media)
