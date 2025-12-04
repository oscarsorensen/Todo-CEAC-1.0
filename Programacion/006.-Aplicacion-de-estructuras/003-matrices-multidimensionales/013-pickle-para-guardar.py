
import pickle
agenda = []

while True:
    print("Seleccione una opcion:")
    print("1. Insertar un registro")
    print("2. Leer registros")
    print("3. Guardar registros")
    print("4. Cargar registros")
    print("5. Salir")
    opcion = int(input("Ingrese el numero de la opcion: "))
    
    if opcion == 1:
        #insertar
        nombre = input("Ingrese el nombre: ")
        appelidos = input("Ingrese los apellidos: ")
        email = input("Ingrese el email: ")
        telefono = input("Ingrese el telefono: ")
        # añado a la agenda
        agenda.append([nombre, appelidos, email, telefono])
        
    elif opcion == 2:
        #print
        print(agenda)
        
    elif opcion == 3:
        #guardar
        archivo = open("agenda.bin", "wb")
        pickle.dump(agenda, archivo)
        archivo.close()
        
    elif opcion == 4:
        # cargar
        archivo = open("agenda.bin", "rb")
        agenda = pickle.load(archivo)
        archivo.close()
        print("Registros cargados:", agenda)

    
    elif opcion == 5:
        #salir
        print("Saliendo...")
        break