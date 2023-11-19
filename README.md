# Reto_11
Holap, en este reto se da solucion al reto 11 propuesto 

1. Desarrolle un programa que permita realizar la suma/resta de matrices. El programa debe validar las condiciones necesarias para ejecutar la operación.
   
```pseudocode
  def ingresomatriz(N):   #instrucciones para construir la matriz
  matriz=[]
  filas= int(input("coloca el  numero de filas: "))
  columnas=int(input("coloca el numero de columnas: "))
  for i in range(filas):
    fila=[]
    for j in range(filas):
      valor= int(input("ingresa el valor: "))
      fila.append(valor)
    matriz.append(fila)
  return(matriz)

def sumamatriz(matriz1,matriz2):    #definicion de la suma a partir de dos matrices
  if len(m1) != len(m2) and len(m1[0]) != len(m2[0]):     #condicion que permite evaluar matrices de igual longitud
    print("la matriz no se puede operar, ya que no es igual")
  else:
    Matrizsuma=[]
    for i in range(len(m1)):
      fila=[]
      for j in range(len(m1)):
        fila.append(m1[i][j]+ m2[i][j])
      Matrizsuma.append(fila)
    return Matrizsuma

def restamatriz(m1,m2):    #definicion de la resta a partir de dos matrices
  if len(m1) != len(m2) and len(m1[0]) != len(m2[0]):   #condicion que permite evaluar matrices de igual longitud
    print("la matriz no se puede operar, ya que no es igual")
  else:
    Matrizresta=[]
    for i in range(len(m1)):
      fila=[]
      for j in range(len(m1)):
        fila.append(m1[i][j]- m2[i][j])
      Matrizresta.append(fila)
    return Matrizresta 

m1= ingresomatriz("1")  #creacion de primera matriz
m2= ingresomatriz("2")  #creacion de segunda matriz

print("Matriz 1:")          #impresion de la primera matriz  
for fila in m1:
    print(fila)

print("Matriz 2:")          #impresion de la segunda matriz
for fila in m2:
    print(fila)

resultadoSuma = sumamatriz(m1, m2)     #aplicacion de la suma con las matrices dadas
print("El resultado de la suma de las matrices es:")  #imprecion del resultado
for fila in resultadoSuma:
  print(fila)
    
resultadoResta = restamatriz(m1, m2)           #aplicacion de la resta con las matrices dadas     
print("El resultado de la resta de las matrices es:")  #imprecion del resultado
for fila in resultadoResta:
    print(fila)
    i +=1
```

2. Desarrolle un programa que permita realizar el producto de matrices. El programa debe validar las condiciones necesarias para ejecutar la operación.

```pseudocode
def ingresomatriz(N):   #instrucciones para construir la matriz
  matriz=[]
  filas= int(input("coloca el  numero de filas: "))
  columnas=int(input("coloca el numero de columnas: "))
  for i in range(filas):
    fila=[]
    for j in range(filas):
      valor= int(input("ingresa el valor: "))
      fila.append(valor)
    matriz.append(fila)
  return(matriz)


def multiplicacionmatriz(m1,m2):     #definicion de la resta a partir de dos matrices
  if len(m1) != len(m2) and len(m1[0]) != len(m2[0]):   #condicion que permite evaluar matrices de igual longitud
    print("la matriz no se puede operar, ya que no es igual")
  else:
      producto=[]
  for i in range(len(m1)):
      producto.append([])
      for j in range(len(m2[0])):
        producto[i].append(0)

  for i in range(len(m1)):
    for j in range(len(m2[0])):
      for k in range(len(m1[0])):
       producto[i][j] += m1[i][k] * m2[k][j]
  return producto


m1= ingresomatriz("1")  #creacion de primera matriz
m2= ingresomatriz("2")  #creacion de segunda matriz

print("Matriz 1:")     #impresion de la primera matriz       
for fila in m1:
    print(fila)

print("Matriz 2:")      #impresion de la segunda matriz
for fila in m2:
    print(fila)

resultadoproducto= multiplicacionmatriz(m1,m2)    #aplicacion del producto con las matrices dadas  
print("El resultado del producto de las matrices es:")  
for fila in resultadoproducto:
    print(fila)
```
    
3. Desarrolle un programa que permita obtener la matriz transpuesta de una matriz ingresada. El programa debe validar las condiciones necesarias para ejecutar la operación.

```pseudocode
def ingresomatriz(N):   #instrucciones para construir la matriz
  matriz=[]
  filas= int(input("coloca el  numero de filas: "))
  columnas=int(input("coloca el numero de columnas: "))
  for i in range(filas):
    fila=[]
    for j in range(filas):
      valor= int(input("ingresa el valor: "))
      fila.append(valor)
    matriz.append(fila)
  return(matriz)

def matriztranspuesta(m1):  # definicion de matriz transpuesta
    Mtranspuesta=[]
    for j in range(len(m1(0))):
      fila=[]
      for i in range(len(m1)):
        fila.append(m1[j][i])
      Mtranspuesta.append(fila)
    return Mtranspuesta

m1= ingresomatriz("1")  # matriz 1

print("Matriz 1:")            
for fila in m1:
    print(fila)

resultadotranspuesta= matriztranspuesta(m1)   #resultado
print("El resultado del producto de las matrices es:")  
for fila in resultadotranspuesta:
    print(fila)
```

4. Desarrollar un programa que sume los elementos de una columna dada de una matriz.

```pseudocode
def sumarColumna(m1, columna):   #definicion de suma de columnas
    if columna < 0 or columna >= len(m1[0]):     #condicion que permite evaluar matrices de igual longitud
        print("La columna ingresada no es válida.")
        return None
    suma = 0
    for fila in m1:       
        suma += fila[columna]
    return suma

def ingresomatriz(N): #instrucciones para construir la matriz
  matriz=[]
  filas= int(input("coloca el  numero de filas: "))
  columnas=int(input("coloca el numero de columnas: "))
  for i in range(filas):
    fila=[]
    for j in range(filas):
      valor= int(input("ingresa el valor: "))
      fila.append(valor)
    matriz.append(fila)
  return(matriz)

m1= ingresomatriz("1")  #matriz 1

print("Matriz 1:")            
for fila in m1:
    print(fila)

columna = int(input("Ingrese el número de la columna a sumar: "))

resultadoSuma = sumarColumna(m1, columna-1)    #parametros bajo los cuales trabaja la funcion

print("La suma de los elementos de la columna " +  str(columna) + " es: " + str(resultadoSuma))
```

5. Desarrollar un programa que sume los elementos de una fila dada de una matriz.

```pseudocode
def sumarfila(m1, fila):   #definicion de suma de filas
    if fila < 0 or fila >= len(m1[0]):     #condicion que permite evaluar matrices de igual longitud
        print("La fila ingresada no es válida.")
        return None
    suma = 0
    for h in m1[fila]:       
        suma += h
    return suma

def ingresomatriz(N):   #instrucciones para construir la matriz
  matriz=[]
  filas= int(input("coloca el  numero de filas: "))
  columnas=int(input("coloca el numero de columnas: "))
  for i in range(filas):
    fila=[]
    for j in range(filas):
      valor= int(input("ingresa el valor: "))
      fila.append(valor)
    matriz.append(fila)
  return(matriz)

m1= ingresomatriz("1")  #matriz 1

print("Matriz 1:")            
for fila in m1:
    print(fila)

fila = int(input("Ingrese el número de la fila a sumar: "))

resultadoSuma = sumarfila(m1, fila-1)     #parametros bajo los cuales trabaja la funcion

print("La suma de los elementos de la fila " +  str(fila) + " es: " + str(resultadoSuma )) #resultado
```

Gracias por leer el repo
