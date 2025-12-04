

print("Lista de la compra v0.1")

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
        
    elif opcion == 2: