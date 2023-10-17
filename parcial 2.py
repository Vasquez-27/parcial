#Se importa la biblioteca random para generar valores aleatorios
import random
#Creamos la lista vacia con 50 elementos
x1=[]
#For donde se agrega a cada posicion de la lista un numero aleatorio entre 1 y 20
for i in range (0,50):
    x1.append( random.randint(1,20))
#Se imprime la lista final con 50 elementos aleatorios entre 1 y 20
print (x1)
#Vector 2 se crea vacio
x2=[]

for i in range(0,len(x1)) :
  #Si el elemento ya esta en el vector 2 no se agrega
  if x1[i] in x2:
    None
  #Si el elemento no esta en el vector 2, se agrega
  else:
    x2.append(x1[i])
print(x2)

#Vector 3 en donde cada elemento de la lista dice cuantas veces se repite cada elemento de x2 en x1
x3=[]
#for donde se agrega cada elemento a x3
#Count sirve para saber cuantas veces esta un elemento en una lista
for i in range(0,len(x2)):
  x3.append(x1.count(x2[i]))
print(x3)

#comentario para que el usuario ingrese un valor
print("ingrese un valor")
#el valor que ingrsa el usuario, para esto se usa la funcion input
valor= input()
#como el valor ingresa como una cadena, se usa la funcion int() para 12
# volverlo entero y se usa la funcion count para saber cuantas veces se repite el valor en el vector 1
repite= x1.count(int(valor))
#respuesta
print("El numero",valor, "se repite",repite,'veces en el vector 1')

#La funcion len devuelve el numero de elementos que tiene una lista
print("El vector 1 tiene", len(x1),"elementos")
print("El vector 2 tiene", len(x2),"elementos")
print("El vector 3 tiene", len(x3),"elementos")