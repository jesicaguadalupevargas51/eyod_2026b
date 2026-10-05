"""
Escribir un programa que calculé 
la uma de los "n" números naturales.
por ejemplo si n=100, el programa 
calculaá la suma del 1 al 100
42
"""
#importar la biblioteca de tiempo 
import time 

#crear las variables para
#el problema 
n= 100
the_sum = 0

#tomando el tiempo 1
timestamp_01 = time.time()

#iniciando la suma 
# 100
while(n > 0 ):
    the_sum = the_sum + n  # 100 +99 + 98 + .. + 1
    n = n-1

#tomamos el t2
timestamp_02 =time.time()

# imprimimos la solucion 
print(f"la suma es{the_sum}")

#calculamos el tiempo
elapsed_time = round((timestamp_02-timestamp_01) * 1e6,2)
print(f"Tiempo de ejecucion: {elapsed_time} us")

