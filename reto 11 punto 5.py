def sumarfila(m1, fila):   
    if fila < 0 or fila >= len(m1[0]):     
        print("La fila ingresada no es válida.")
        return None
    suma = 0
    for h in m1[fila]:       
        suma += h
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

fila = int(input("Ingrese el número de la fila a sumar: "))

resultadoSuma = sumarfila(m1, fila-1)    

print("La suma de los elementos de la fila " +  str(fila) + " es: " + str(resultadoSuma ))