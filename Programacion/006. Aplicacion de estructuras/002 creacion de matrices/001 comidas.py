menu = []

while True:
    print("Opciones: ")
    print("1. Introducir nueva comida en el menu")
    print("2. Listar comidas en el menu")
    opcion = int(input("Selecciona una opcion (1 o 2): "))
    
    if opcion == "1":
    
    comida = input("Entroduce el nombre de la comida: ")
    menu.append(comida)
    
    elif opcion == "2":
        print("Tu comida hasla el momento es: ")
        for elemento in menu:
            print("elemento")
            
        