
while True:
    print("Dime lo que quieres hacer")
    print("1. Introduce un nuevo contacto")
    print("2. Leer todos los contactos")
    opcion = input("Escoge tu opcion (1 o 2): ")
    opcion = int(opcion)
    if opcion == 1:
        nombre = input("Dime el nombre del contacto")
        email = input("Dime el email del contacto")
        archivo = open("agenda.txt", "a")  # A = Append
        archivo.write(nombre + "," + email + "\n")
        archivo.close()
    elif opcion == 2:
        archivo = open("agenda.txt", "r")
        lineas = archivo.readlines()
        for linea in lineas:
            print(linea)
        archivo.close()
    