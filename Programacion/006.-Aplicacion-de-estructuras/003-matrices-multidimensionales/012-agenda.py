
agenda = []

while True:
    nombre = input("Ingrese el nombre: ")
    appelidos = input("Ingrese los apellidos: ")
    email = input("Ingrese el email: ")
    telefono = input("Ingrese el telefono: ")
    # añado a la agenda
    agenda.append([nombre, appelidos, email, telefono])
    print(agenda)