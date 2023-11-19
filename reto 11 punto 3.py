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

def matriztranspuesta(m1):
    Mtranspuesta=[]
    for j in range(len(m1(0))):
      fila=[]
      for i in range(len(m1)):
        fila.append(m1[j][i])
      Mtranspuesta.append(fila)
    return Mtranspuesta

m1= ingresomatriz("1")

print("Matriz 1:")            
for fila in m1:
    print(fila)

resultadotranspuesta= matriztranspuesta(m1) 
print("El resultado del producto de las matrices es:")  
for fila in resultadotranspuesta:
    print(fila)