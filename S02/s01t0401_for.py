"""
Escribir un programa que calculé 
la uma de los "n" números naturales.
por ejemplo si n=100, el programa 
calculaá la suma del 1 al 100
42
"""
#impostamos biblioteca time
import time 

#funcion que suma los 
#primeros "n" numeros naturales
def sum_of_n(n):
    total_sum=0
    #sumamos los "n" numeros 

#ciclo for 
    for number in range(1,n+1):
       total_sum = total_sum + number
    return total_sum
   #retornando el total de la suma
#variable para guardar 
# el data set
dataset = [] #[()]

#generando el contenido de data set
for repetition in range(1,11):

    #🕛 tomo el tiempo 1 
    timestamp_01 = time.time()

    #sumo los "n" numeros
    n = repetition*500
    #guardo el resultado en result
    result= sum_of_n(n)

    #🕐 tomando el tiempo final 
    timestamp_2 = time.time()

    #claculando el tiempo
    elapsed_time = round ((timestamp_2-timestamp_01) * 1e6,2)

    # agregar la tripleta de los
    # datos al dataset
    dataset.append( (n,elapsed_time,result) )

#imprimir el dataset
for tup in dataset:
    print (tup)