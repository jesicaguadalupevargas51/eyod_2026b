#Array
#from arrar import *
import array as arr

#creaio de un arreglo
# i: entero con signo
#I : entero sin sgno 
# f : Numero decimal 
# d : Numero decimal doble 
# u : Caracteres unicode
my_array = arr.array ("i", [10,22,300,3,7,40,55,80,700,654,34])

#interaccion automatica 
#for num in my_array :
#     print(num) 

#acceso indivial a los elementos
# print(my_array[0])#primer elemento
# print(my_array[1])#segudo elemento
# print(my_array[1])#tercer elemento

#print(len(my_array))

# iterar por indices
#for i in range (len(my_array)):
#     if my_array[i]% 2 ==0:
#         print(f"elemento Num {i+1}:{my_array[i]}")
#     print(f"{i+1}:{my_array[i]}")

#BUSQUEDA DE UN ELEMENTO
num_to_search = 200 

#modificando un valor
# backet notation 
my_array[7]= 200

try:
 print(f"Localizacion {num_to_search}: {my_array.index
                                       (num_to_search)}")

except:
  print("⚠️numero no encontrado!!!")

#Asignamos valor en
try: 
  my_array[100]= 3
except: 
   print("⚠️indice no existe!!!")
