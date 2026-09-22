"""
Escribir un programa que calculé 
la uma de los "n" números naturales.
por ejemplo si n=100, el programa 
calculaá la suma del 1 al 100
42
"""
#impostamos biblioteca time
import time 

#creando el tiempo inicial 
timestamp_01 = time.time()

#programa que calcule la suma
# de los "n" números naturales 

n= 100
total_sum = 0 

#ciclo for 
for number in range(1,n+1):
    total_sum = total_sum = 0 + number
        #1: sum <-0 + 1
        # sum = 1
        # 2: sum<-1 + 2
        # sum = 3
        # 3: sum< -3 + 3
        # ...
        #100: sum <-sum(-1) + 100

print(f"la suma de 1 hasta {n} es: {total_sum}")
    #actualizacion del programa de suma

    #tomando el tiempo final 
timestamp_2 = time.time()

#impresion de tiempo de ejecucion 
print(f"tiempo de ejecucion: {(timestamp_2-timestamp_01) * 1e6:.2f} μs")
    