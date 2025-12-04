print("Lista de la compra v0.1")
import json

lista_de_la_compra = []

while True:
    print("Seleccione una opcion:")
    print("1. Añadir producto")
    print("2. Ver lista de la compra")
    opcion = int(input("Ingrese el número de la opción deseada: "))
    
    if opcion == 1:
        print("Añadir producto")
        nombre = input("Ingrese el nombre del producto: ")
        cantidad = input("Ingrese la cantidad: ")  
        lista_de_la_compra.append({"nombre": nombre, "cantidad": cantidad})
        archivo = open("lista.json", "w")             # abrir archivo en modo escritura
        json.dump(lista_de_la_compra, archivo)        # guardar lista en json
        archivo.close()                               # cerrar archivo
        
    elif opcion == 2:
        print("Lista de la compra:")
        for producto in lista_de_la_compra:
            print("Producto:", producto["nombre"])
            print("Cantidad:", producto["cantidad"])
            print("-----")

#The json file ends up in "la raiz". i delete it after testing.