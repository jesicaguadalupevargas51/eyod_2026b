from array import array as arr # importa, arr renombra la bibloteca
#parametros de mi cuadricula
# row es fila  
rows = 1
columns = 2 * rows - 1

#creando la reticula 2D
matrix = []

#construyendo el grid (reticula)
for _ in range (rows):
    new_row = arr("i", [0] * columns)
    matrix.append(new_row)

#validando la construccion del grid
print(f"cantidad de filas: {len(matrix)}")
print(f"cantidad de columnas:{len(matrix[0])}")

for row in matrix:
  print(list(row))