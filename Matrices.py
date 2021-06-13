#LISTAS ANIDADAS
#LISTA DE M LISTAS,DONDE CADA UNA TIENE EL MISMO NUM DE ELEMENTOS n
#PRIMER ELEMNTO ES 0, FILA*COLUMNA
matrix = [[1,2,3],[3,4,5],[6,7,8]]
print (matrix)

for row in matrix: #MOSTRAR MATRIZ COMPLETA
    print (row)

for i in matrix: #MOSTRAR ELEMENTOS EN COLUMNA,DOS BUCLES
    for j in i:
        print(j)

#MOSTRAR MATRIZ EN FORMA DE TABLA,SIN COMAS NO CLAUDATORS POR MEDIO

m=len(matrix) #filas
n=len(matrix[0]) #columnas

for i in range (m):
    for j in range (n):
        print(matrix[i][j], end = "")
    print ("")


n = int (input("numero de filas"))
m = int (input("numero de columnas"))
p = int (input("numero de columnas segunda matriz"))

A= []
print ("matriz")