#importando clase node
from S02T0201_linked_list import Node 

#1 Creo funcion principal
def main():
    #2coloco el codigo ejecutable 
    test_node =Node("prueba")
    print(f"valor del nodo : {test_node.data}")

#evaluo el valor de __name__
if __name__ == "__main__":
    main()