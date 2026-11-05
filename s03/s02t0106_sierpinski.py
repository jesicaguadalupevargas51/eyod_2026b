from array import array as arr # importa, arr renombra la bibloteca
#parametros de mi cuadricula
# row es fila  
rows = 3
columns = 2 * rows - 1

#funcion para imprimir matrix 
def print_matrix(input_matrix):
    for row in input_matrix:
      print(list(row))

#creando la reticula 2D
matrix = []
#construyendo el grid (reticula)
for _ in range (rows):
    new_row = arr("i", [0] * columns)
    matrix.append(new_row)

#validando la construccion del grid
print(f"cantidad de filas: {len(matrix)}")
print(f"cantidad de columnas:{len(matrix[0])}")

#calculadno el centro de la primera fila
center =columns //2 # se hace divicione entera

#Estableciendo el centro en 1
matrix[0][center] = 1

# print_matrix(matrix)

#se calcula el resto de la matrix
#siguiendo la logica de sierpinsky Gasket

for row in range(1,rows):
   for col in range(0, columns):
      left_upper_cell = 0
      right_upper_cell = 0

      #si la columna donde estamos es mayor a 0

      if col > 0 :
         left_upper_cell = matrix[row-1][col-1]
         #si la columna  esta un elemento antes del borde derecho
         if col > columns - 1:
            right_upper_cell = matrix[row-1][col+1]

            #guardado  el arreglo 
            if left_upper_cell ≠ right_upper_cell :
               matrix[row][col] =1
            else: 
               matrix[row][col]=0

               print()

    #   print(f"[{row}-{col}]",end="")
    #   print()

