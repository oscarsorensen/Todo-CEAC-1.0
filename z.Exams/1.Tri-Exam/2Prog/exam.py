"""
En este ejercicio, desarrollaré una mini aplicación de consola en Python que me permita gestionar datos de clientes mediante operaciones CRUD conectadas a mi base de datos MySQL; utilizaré la base de datos que creé en el examen de Bases de datos.El objetivo es practicar la interacción entre un programa Python y una base de datos real, aplicando instrucciones SQL básicas para crear, leer, actualizar y eliminar registros.Este ejercicio muestra cómo se combina la lógica de control (bucles y if-elif) con el uso de bibliotecas externas.La biblioteca mysql.connector se utiliza para establecer la conexión con MySQL, autenticándose con el usuario useroscar y la base de datos portafolioexamen.A continuación, se crea la tabla clients con su clave principal Identifier y los campos nombre, apellidos y correo electrónico.La aplicación muestra un mensaje de bienvenida y un menú de opciones numeradas del 1 al 5.Mediante un bucle while True, el usuario puede seleccionar la operación deseada y, dependiendo de la opción elegida, se ejecutan las sentencias SQL correspondientes:INSERT INTO para añadir un nuevo cliente.SELECT FROM para listar todos los registros.UPDATE SET WHERE para modificar los datos de un cliente específico.DELETE FROM para eliminar un registro por ID.Las decisiones se controlan con estructuras if-elif, y cada operación se confirma con connection.commit() para guardar los cambios en la base de datos.
"""


import mysql.connector

# Conexión a MySQL usando el usuario con permisos
connection = mysql.connector.connect(
    host="localhost",
    user="useroscar",
    password="Oscar081100!",
    database="portafolioexamen"
)

cursor = connection.cursor()

# Crear la tabla si no existe (solo piezas, no categorías)
cursor.execute("""
CREATE TABLE IF NOT EXISTS piezasportafolio (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(150),
    descripcion TEXT,
    fecha VARCHAR(50),
    categoria_id INT
);
""")
connection.commit()

print("=== GESTOR DE PIEZAS DEL PORTAFOLIO (MySQL) ===")
print("Bienvenido al gestor de piezas conectado a la base de datos MySQL.")

while True:
    print("""
1. Crear nueva pieza
2. Listar piezas
3. Actualizar pieza
4. Eliminar pieza
5. Salir
""")

    option = input("Elige una opción: ")

    if option == "1":
        title = input("Título: ")
        descripcion = input("Descripción: ")
        fecha = input("Fecha (YYYY-MM-DD): ")
        categoria_id = input("ID de categoría (1 (Fotografía), 2 (Diseño Gráfico), 3 (Desarrollo Web)): ")
        cursor.execute("""
        INSERT INTO piezasportafolio (title, descripcion, fecha, categoria_id)
        VALUES (%s, %s, %s, %s);
        """, (title, descripcion, fecha, categoria_id))
        connection.commit()
        print("Pieza añadida correctamente.")

    elif option == "2":
        cursor.execute("SELECT * FROM piezasportafolio;")
        rows = cursor.fetchall()
        if not rows:
            print("No hay piezas registradas.")
        else:
            for row in rows:
                print(row)

    elif option == "3":
        pieza_id = input("ID de la pieza a actualizar: ")
        title = input("Nuevo título: ")
        descripcion = input("Nueva descripción: ")
        fecha = input("Nueva fecha (YYYY-MM-DD): ")
        categoria_id = input("Nuevo ID de categoría (1 (Fotografía), 2 (Diseño Gráfico), 3 (Desarrollo Web): ")
        cursor.execute("""
        UPDATE piezasportafolio
        SET title = %s, descripcion = %s, fecha = %s, categoria_id = %s
        WHERE id = %s;
        """, (title, descripcion, fecha, categoria_id, pieza_id))
        connection.commit()
        print("Pieza actualizada correctamente.")

    elif option == "4":
        pieza_id = input("ID de la pieza a eliminar: ")
        cursor.execute("DELETE FROM piezasportafolio WHERE id = %s;", (pieza_id,))
        connection.commit()
        print("Pieza eliminada correctamente.")

    elif option == "5":
        print("Saliendo del programa. ¡Hasta luego!")
        break

    else:
        print("Opción inválida. Intenta de nuevo.")

connection.close()


"""
El ejercicio me ha ayudado a practicar el uso de Python como lenguaje para interactuar con una base de datos MySQL. Ya tenía algunos datos en ella, pero practiqué cómo crear una nueva tabla y utilizarla.
Se ha verificado cómo se pueden ejecutar operaciones CRUD desde una aplicación de consola, combinando sentencias SQL con estructuras de control y funciones de conexión.
El resultado final es un programa funcional y reutilizable que demuestra los fundamentos del desarrollo de software conectado a bases de datos reales.
Es fácil ver cómo se puede implementar esto en un escenario real, en el que necesitaría crear y utilizar una base de datos. Ha sido una tarea muy práctica y especialmente útil para comprender mejor cómo utilizar los diferentes lenguajes juntos.
"""