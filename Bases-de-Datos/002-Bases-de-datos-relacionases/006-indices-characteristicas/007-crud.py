import sqlite3

conexion = sqlite3.connect("empresa.db")
cursor = conexion.cursor()

print("Programa agenda SQlite v0.1 OscarSorensen")

while True:
    print("Escoge una opcion:\n1.- Crear cliente\n2.- Listar clientes")
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
