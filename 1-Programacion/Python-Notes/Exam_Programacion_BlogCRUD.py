
# =====================================================================
# EXAMEN DE PROGRAMACIÓN - PANEL DE CONTROL DEL BLOG (CRUD EN CONSOLA)
# Autor: Oscar Sørensen
# Profesor: José Vicente Carratalá (CEAC)
# ---------------------------------------------------------------------
# Descripción oficial del examen:
# Crea un programa de consola que haga un CRUD sobre entradas del blog.
# Debe mostrar un mensaje de bienvenida, entrar en un bucle infinito,
# ofrecer un menú con cuatro opciones (CREATE, READ, UPDATE, DELETE),
# atrapar las opciones con if-elif, y procesar las operaciones contra
# la base de datos (SQLite o MySQL). El programa debe confirmar que
# puede gestionar las entradas correctamente.
# =====================================================================

import sqlite3

# --------------------------- CONEXIÓN A LA BASE DE DATOS ---------------------------
# Se crea (o abre) una base de datos local llamada blog.db
conexion = sqlite3.connect("blog.db")
cursor = conexion.cursor()

# Si no existe la tabla 'entradas', se crea con tres campos básicos
cursor.execute('''
CREATE TABLE IF NOT EXISTS entradas(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT NOT NULL,
    contenido TEXT NOT NULL,
    autor TEXT NOT NULL
);
''')
conexion.commit()

# --------------------------- FUNCIONES CRUD ---------------------------
def crear_entrada():
    print("\n--- Crear nueva entrada ---")
    titulo = input("Título: ")
    contenido = input("Contenido: ")
    autor = input("Autor: ")
    cursor.execute("INSERT INTO entradas (titulo, contenido, autor) VALUES (?, ?, ?)", (titulo, contenido, autor))
    conexion.commit()
    print("Entrada creada correctamente.")

def listar_entradas():
    print("\n--- Listar todas las entradas ---")
    cursor.execute("SELECT * FROM entradas")
    filas = cursor.fetchall()
    if filas:
        for fila in filas:
            print(f"ID: {fila[0]} | Título: {fila[1]} | Autor: {fila[3]}")
            print(f"Contenido: {fila[2]}\n")
    else:
        print("No hay entradas registradas.")

def actualizar_entrada():
    print("\n--- Actualizar una entrada ---")
    id_modificar = input("ID de la entrada a modificar: ")
    nuevo_titulo = input("Nuevo título: ")
    nuevo_contenido = input("Nuevo contenido: ")
    cursor.execute("UPDATE entradas SET titulo=?, contenido=? WHERE id=?", (nuevo_titulo, nuevo_contenido, id_modificar))
    conexion.commit()
    print("Entrada actualizada correctamente.")

def eliminar_entrada():
    print("\n--- Eliminar una entrada ---")
    id_eliminar = input("ID de la entrada a eliminar: ")
    cursor.execute("DELETE FROM entradas WHERE id=?", (id_eliminar,))
    conexion.commit()
    print("Entrada eliminada correctamente.")

# --------------------------- MENÚ PRINCIPAL ---------------------------
def menu():
    print("\n============================")
    print(" PANEL DE CONTROL DEL BLOG ")
    print("============================")
    print("1. Crear entrada")
    print("2. Listar entradas")
    print("3. Actualizar entrada")
    print("4. Eliminar entrada")
    print("5. Salir")

# --------------------------- PROGRAMA PRINCIPAL ---------------------------
print("Bienvenido al panel de control del blog.")

while True:
    menu()
    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        crear_entrada()
    elif opcion == "2":
        listar_entradas()
    elif opcion == "3":
        actualizar_entrada()
    elif opcion == "4":
        eliminar_entrada()
    elif opcion == "5":
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida. Intenta de nuevo.")

# Cerrar conexión antes de finalizar
conexion.close()
print("Conexión cerrada correctamente.")
# =====================================================================
# FIN DEL EXAMEN DE PROGRAMACIÓN - CRUD DEL BLOG
# =====================================================================
