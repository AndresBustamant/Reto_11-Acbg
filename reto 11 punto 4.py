def sumarColumna(m1, columna):   
    if columna < 0 or columna >= len(m1[0]):     
        print("La columna ingresada no es válida.")
        return None
    suma = 0
    for fila in m1:       
        suma += fila[columna]
    return suma

def ingresomatriz(N):
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

m1= ingresomatriz("1")

print("Matriz 1:")            
for fila in m1:
    print(fila)

columna = int(input("Ingrese el número de la columna a sumar: "))

resultadoSuma = sumarColumna(m1, columna-1)    

print("La suma de los elementos de la columna " +  str(columna) + " es: " + str(resultadoSuma))