"""
Generators 

los generadores son funciones que pueden
pausar su ejecucion.

cuando se invoca una funcion generadora
devueve un objeto generador (aka Interador).

El codigo dentro de una funcion no se ejecuta 
de inmediato, solo se copila.

la funcion se ejecuta unicamente cuando 
iteras(repetir) sobre el generador.

"""
#yield (producir)
def my_generator():
    yield 1
    yield 2
    yield 3
    yield 4

#se invoca funcion generadora
my_iterator = my_generator()

#se itera manualmente sobre el generador
# print(next(my_iterator)) #imprime 1
# print(next(my_iterator)) #imprime 2
# print(next(my_iterator)) #imprime 3
# print(next(my_iterator)) #imprime 4
# print(next(my_iterator)) #imprime ?

#los iteradores se puede iterar con un for
for value in my_iterator:
   print(value)