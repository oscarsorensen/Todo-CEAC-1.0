print("Lista de componentes PC v0.1")
import json

lista_de_la_compra = []   # keep variable name the same

##########   Adding this part myself, so the list doesnt dissapear every time i close the program.         #############
try:
    archivo = open("lista.json", "r")
    lista_de_la_compra = json.load(archivo)
    archivo.close()
except:
    lista_de_la_compra = []
#############################

while True:
    print("Seleccione una opcion:")
    print("1. Añadir componente")
    print("2. Ver lista de componentes")
    opcion = int(input("Ingrese el número de la opción deseada: "))
    
    if opcion == 1:
        print("Añadir componente")
        nombre = input("Ingrese el nombre del componente: ")
        cantidad = input("Ingrese la cantidad/unidades: ")  
        lista_de_la_compra.append({"nombre": nombre, "cantidad": cantidad})
        archivo = open("lista.json", "w")
        json.dump(lista_de_la_compra, archivo)
        archivo.close()
        
    elif opcion == 2:
        print("Lista de componentes:")
        for producto in lista_de_la_compra:
            print("Componente:", producto["nombre"])
            print("Unidades:", producto["cantidad"])
            print("-----------------------------")
