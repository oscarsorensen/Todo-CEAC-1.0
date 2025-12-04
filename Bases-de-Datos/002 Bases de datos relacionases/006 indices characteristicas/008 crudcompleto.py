import sqlite3

conexion = sqlite3.connect("empresa.db")
cursor = conexion.cursor()

print("Programa agenda SQlite v0.1 OscarSorensen")

while True:
    print("Escoge una opcion:\n1.- Crear cliente\n2.- Listar clientes\n3.- Actualizar clientes\n4.- Eliminar clientes\n5.- Salir del programa")
    opcion = int(input("Selecciona una opcion: "))

    if opcion == 1:
        nombre = input("Introduce el nombre del nuevo cliente: ")
        apellidos = input("Introduce los apellidos del nuevo cliente: ")
        email = input("Introduce el email del nuevo cliente: ")

        cursor.execute("""
            insert into clientes values(
                NULL, '""" + nombre + """','""" + apellidos + """','""" + email + """'
            );
        """)
        conexion.commit()

    elif opcion == 2:
        cursor.execute("select * from clientes;")
        filas = cursor.fetchall()
        for fila in filas:
            print(fila)

    elif opcion == 3:
        identificador = input("Introduce el identificador a actualizar: ")
        nombre = input("Introduce el nuevo nombre: ")
        apellidos = input("Introduce los nuevos apellidos: ")
        email = input("Introduce el nuevo email: ")
        cursor.execute("""
            update clientes set
                nombre = '""" + nombre + """',
                apellidos = '""" + apellidos + """',
                email = '""" + email + """'
            where Identificador = """ + identificador + """;
        """)
        conexion.commit()

    elif opcion == 4:
        identificador = input("Introduce el identificador a eliminar: ")
        cursor.execute("""
            delete from clientes where Identificador = """ + identificador + """;
        """)
        conexion.commit()

    elif opcion == 5:
        print("bye bye")
        conexion.close()
        exit()
