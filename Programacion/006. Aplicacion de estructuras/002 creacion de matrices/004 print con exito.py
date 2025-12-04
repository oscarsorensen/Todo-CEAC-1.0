import pickle
menu = []

while True:
    print("Opciones: ")
    print("1. Introducir nueva comida en el menu")
    print("2. Listar comidas en el menu")
    print("3. Guardar en archivo")
    print("4. Carcar datos de archivo")
    
    opcion = int(input("Selecciona una opcion (1, 2, 3 o 4): "))
    
    if opcion == 1:
        comida = input("Introduce el nombre de la comida: ")
        menu.append(comida)
    
    elif opcion == 2:
        print("Comidas hasta el momento:")
        for elemento in menu:
            print(elemento)

    elif opcion == 3:
        archivo = open("datos.txt", "wb")
        pickle.dump(menu, archivo)
        archivo.close()
        print("Guardado correctamente.")

    elif opcion == 4:
        archivo = open("datos.txt", "rb")
        menu = pickle.load(archivo)
        archivo.close()
        print("Datos cargados correctamente.")
        