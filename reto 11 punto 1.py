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

def sumamatriz(matriz1,matriz2):
  if len(m1) != len(m2) and len(m1[0]) != len(m2[0]):
    print("la matriz no se puede operar, ya que no es igual")
  else:
    Matrizsuma=[]
    for i in range(len(m1)):
      fila=[]
      for j in range(len(m1)):
        fila.append(m1[i][j]+ m2[i][j])
      Matrizsuma.append(fila)
    return Matrizsuma

def restamatriz(m1,m2):
  if len(m1) != len(m2) and len(m1[0]) != len(m2[0]):
    print("la matriz no se puede operar, ya que no es igual")
  else:
    Matrizresta=[]
    for i in range(len(m1)):
      fila=[]
      for j in range(len(m1)):
        fila.append(m1[i][j]- m2[i][j])
      Matrizresta.append(fila)
    return Matrizresta 

m1= ingresomatriz("1")
m2= ingresomatriz("2")

print("Matriz 1:")            
for fila in m1:
    print(fila)

print("Matriz 2:")          
for fila in m2:
    print(fila)

resultadoSuma = sumamatriz(m1, m2)                 
print("El resultado de la suma de las matrices es:")  
for fila in resultadoSuma:
  print(fila)
    
resultadoResta = restamatriz(m1, m2)                
print("El resultado de la resta de las matrices es:")  
for fila in resultadoResta:
    print(fila)