#Aquí he creado un sencillo programa en Python para llevar un registro de las comidas que ingiero durante mi rutina de gimnasio. De esta forma, puedo organizar mejor la comida y guardarla para más adelante. Este es un ejemplo práctico de cómo se puede utilizar la programación en situaciones cotidianas como la nutrición y el fitness.
#El programa utiliza una lista llamada "menú" para almacenar las comidas. Cada comida se guarda como un elemento simple en la lista. A través de un sistema de menús, puedo añadir nuevas comidas, ver la lista actual, guardar los datos en un archivo utilizando el módulo pickle y cargar los datos desde el archivo. Todas las operaciones se realizan utilizando estructuras de control básicas y conceptos vistos en clase.
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
        archivo = open("datos.bin", "wb")
        pickle.dump(menu, archivo)
        archivo.close()
        print("Guardado correctamente.")

    elif opcion == 4:
        archivo = open("datos.bin", "rb")
        menu = pickle.load(archivo)
        archivo.close()
        print("Datos cargados correctamente.")

        print("Comidas cargadas:")
        for elemento in menu:
            print(elemento)

            
#Con este ejercicio, practiqué cómo usar listas y almacenamiento de archivos en Python. Practiqué cómo guardar y cargar datos usando pickle, lo que me permite conservar la información entre ejecuciones del programa. Este conocimiento es útil para crear programas sencillos que gestionan datos reales en la vida cotidiana.