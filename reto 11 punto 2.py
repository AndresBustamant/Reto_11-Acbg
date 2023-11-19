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


def multiplicacionmatriz(m1,m2):
  if len(m1) != len(m2) and len(m1[0]) != len(m2[0]):
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


m1= ingresomatriz("1")
m2= ingresomatriz("2")

print("Matriz 1:")            
for fila in m1:
    print(fila)

print("Matriz 2:")          
for fila in m2:
    print(fila)

resultadoproducto= multiplicacionmatriz(m1,m2) 
print("El resultado del producto de las matrices es:")  
for fila in resultadoproducto:
    print(fila)