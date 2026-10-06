"""

1. Identifico el tamaño de la entrada "n"
el tamaño de la entrada es el numero 
de estudiantes.
2. Es ver cuanto crece el numero de
operaciones en el algoritmo conforme 
crece el tamaño de la entrada
Agrego las bigO identificadas
Teniendo en cuenta la Cota superior Asintotica 
O(n) + O(4) = O(n+4)= O(n)
"""

#creando una lista de estudiantes 
student_list_01 =["jordan","çurry","pipen","Shack"]
student_list_02 =["Mike","Saul","Walter","Jessy"]

#verificando la precencia de un estudiante 
def check_student(input_student, student_list):
    for student in student_list:
        if input_student ==student:#0(n)
             print("estudiante encontrado")#0(1)
             return student#0(1)
#si no encuentro al estudiante 
    print("Estudiante no encontrado")#0(1)
    return None#0(1)

#probando algoritmo
check_student("Walter", student_list_01)