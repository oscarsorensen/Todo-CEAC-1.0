
# ============================================================================
# PROGRAMACIÓN — RESUMEN COMPLETO (UNIDADES 001–007) — Estilo Jocarsa
# Autor: Oscar Sørensen
# Nota: Comentarios explicativos en ENGLISH, con palabras clave en ESPAÑOL.
# Regla de estilo: código sencillo, directo, sin atajos modernos.
# - Sin type hints avanzados, sin f-strings (usar concatenación y format).
# - Nombres simples: cliente, entrada, producto, matematicas, etc.
# - Menús con while True + if/elif, listas en memoria, pickle/JSON, SQLite.
# ============================================================================

# ---------------------------------------------------------------------------
# INTRODUCCIÓN (introducción)
# ---------------------------------------------------------------------------
# Purpose (EN): This file is a complete, always-useful manual of everything
# learned up to the exam. It follows the same straightforward style as class.
# Use Ctrl/Cmd+F to find Spanish keywords (e.g., 'clase', 'constructor').
# ---------------------------------------------------------------------------

# ============================================================================
# UNIDAD 001 — VARIABLES, TIPOS Y OPERADORES (variables, tipos, operadores)
# ============================================================================
# Theory (EN):
# - Variables hold values. Python chooses the internal type automatically.
# - Common types: int, float, str, bool. Convert with int(), float(), str(), bool().
# - Operators: + - * / // % **; Comparisons: == != < <= > >=; Logical: and or not.
# - Always use names that describe the intent.
# Palabras clave (ES): variables, tipos de datos, operadores.
# ---------------------------------------------------------------------------

# Ejemplo 1 — variables básicas (variables)
edad = 24                 # int
altura = 1.80             # float
nombre = "Oscar"          # str
es_estudiante = True      # bool

# Ejemplo 2 — operadores aritméticos (operadores)
suma = 4 + 3              # 7
resta = 10 - 5            # 5
producto = 6 * 7          # 42
division = 8 / 2          # 4.0
entera = 8 // 3           # 2
modulo = 8 % 3            # 2
potencia = 2 ** 3         # 8

# Ejemplo 3 — conversiones (conversión)
numero_str = "15"
numero_int = int(numero_str)       # 15
numero_float = float("3.14")       # 3.14
texto_numero = str(123)            # "123"

# print("Suma:", suma, " Potencia:", potencia)

# ============================================================================
# UNIDAD 002 — CONDICIONALES Y BUCLES (if, elif, else, bucle while, bucle for)
# ============================================================================
# Theory (EN):
# - Use if/elif/else to choose between branches (condicionales).
# - Use while when you repeat until a condition changes; use for to iterate a range.
# - Keep loops simple and avoid infinite loops unless you want a menu.
# Palabras clave (ES): if, elif, else, bucle while, bucle for.
# ---------------------------------------------------------------------------

# Ejemplo 1 — condicional (condicionales)
def clasificar_numero(n):
    if n < 0:
        return "negativo"
    elif n == 0:
        return "cero"
    else:
        return "positivo"

# Ejemplo 2 — bucle for (bucle for)
for i in range(3):
    pass
    # print("i =", i)

# Ejemplo 3 — bucle while (bucle while)
contador = 3
while contador > 0:
    # print("contador =", contador)
    contador = contador - 1

# ============================================================================
# UNIDAD 003 — FUNCIONES Y EXCEPCIONES (funciones, try/except)
# ============================================================================
# Theory (EN):
# - Functions (funciones) group reusable actions. Use return to send a result.
# - Use try/except to handle errors without stopping the program.
# - Validate and convert user input safely.
# Palabras clave (ES): funciones, parámetros, retorno, try, except, ValueError.
# ---------------------------------------------------------------------------

# Ejemplo 1 — función simple (funciones)
def sumar(a, b):
    return a + b

# Ejemplo 2 — entrada segura (try/except)
def leer_entero(texto):
    valor = 0
    try:
        valor = int(texto)
    except ValueError:
        valor = 0
    return valor

# print("Suma 2+3 =", sumar(2,3))
# print("Entero de 'abc' =", leer_entero("abc"))

# ============================================================================
# UNIDAD 004 — CLASES, PROPIEDADES Y CONSTRUCTORES (clase, propiedades, constructor)
# ============================================================================
# Theory (EN):
# - A class (clase) defines properties (propiedades/atributos) and methods (métodos).
# - __init__ is the constructor (constructor) where you initialize properties.
# - Keep names clear, and keep state consistent.
# Palabras clave (ES): clase, propiedades, constructor, método, self.
# ---------------------------------------------------------------------------

# Ejemplo 1 — clase Matemáticas (clase)
class Matematicas:
    def __init__(self):
        self.numero = 0  # propiedad

    def suma(self, a, b):
        return a + b

# Ejemplo 2 — clase Entrada (blog) (clase, constructor)
class Entrada:
    def __init__(self, titulo, contenido, autor):
        # propiedades
        self.titulo = titulo
        self.contenido = contenido
        self.autor = autor

    def resumen(self):
        return self.titulo + " — " + self.autor

# e = Entrada("Hola", "Contenido", "Oscar")
# print(e.resumen())

# Ejemplo 3 — clase Cliente (propiedades)
class Cliente:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email

# ============================================================================
# UNIDAD 005 — ARCHIVOS: TEXTO, JSON, PICKLE (archivos, json, pickle, persistencia)
# ============================================================================
# Theory (EN):
# - Text files are good for simple logs or exporting data.
# - JSON is readable and portable; it stores lists/dicts as text.
# - Pickle stores Python objects in binary (persistencia rápida y sencilla).
# Palabras clave (ES): archivos, lectura/escritura, json, pickle, persistencia.
# ---------------------------------------------------------------------------

# TEXTO (texto)
def guardar_texto(ruta, texto):
    f = open(ruta, "w")
    f.write(texto)
    f.close()

def leer_texto(ruta):
    f = open(ruta, "r")
    contenido = f.read()
    f.close()
    return contenido

# JSON (json)
import json

def guardar_json(ruta, datos):
    f = open(ruta, "w")
    json.dump(datos, f, ensure_ascii=False, indent=2)
    f.close()

def leer_json(ruta):
    f = open(ruta, "r")
    datos = json.load(f)
    f.close()
    return datos

# PICKLE (pickle, persistencia)
import pickle

def guardar_pickle(ruta, objeto):
    f = open(ruta, "wb")
    pickle.dump(objeto, f)
    f.close()

def leer_pickle(ruta):
    try:
        f = open(ruta, "rb")
        obj = pickle.load(f)
        f.close()
        return obj
    except FileNotFoundError:
        return None

# Ejemplo — guardar una lista de clientes en pickle (pickle)
def ejemplo_pickle_clientes():
    clientes = []
    clientes.append(Cliente("Ana", "ana@example.com"))
    clientes.append(Cliente("Luis", "luis@example.com"))
    guardar_pickle("clientes.bin", clientes)
    cargados = leer_pickle("clientes.bin")
    # for c in cargados:
    #     print(c.nombre, c.email)

# ============================================================================
# UNIDAD 006 — MENÚ + CRUD EN CONSOLA (menú, CRUD, bucle infinito, if/elif)
# ============================================================================
# Theory (EN):
# - A typical console app has: welcome, while True, menu with options, if/elif.
# - Store items in a list (memoria). For persistence, save to pickle each change.
# Palabras clave (ES): menú, bucle infinito, CRUD, if/elif, lista, persistencia.
# ---------------------------------------------------------------------------

# Modelo de datos simple para CRUD (entrada)
class EntradaCRUD:
    def __init__(self, titulo, contenido, autor):
        self.titulo = titulo
        self.contenido = contenido
        self.autor = autor

# Mini-CRUD en memoria con persistencia pickle (CRUD)
def app_crud_memoria_pickle():
    print("Bienvenido al panel de control (memoria + pickle).")
    entradas = leer_pickle("entradas.bin")
    if entradas is None:
        entradas = []  # lista de objetos EntradaCRUD

    while True:  # bucle infinito
        print("")
        print("1) Crear   2) Listar   3) Actualizar   4) Eliminar   5) Salir")
        opcion = input("Opción: ").strip()

        if opcion == "1":  # CREATE
            t = input("Título: ")
            c = input("Contenido: ")
            a = input("Autor: ")
            entradas.append(EntradaCRUD(t, c, a))
            guardar_pickle("entradas.bin", entradas)
            print("Entrada creada.")
        elif opcion == "2":  # READ
            if len(entradas) == 0:
                print("Sin entradas.")
            else:
                for i, e in enumerate(entradas):
                    numero = i + 1
                    print(str(numero) + ". " + e.titulo + " — " + e.autor)
        elif opcion == "3":  # UPDATE
            idx_texto = input("Número de entrada a modificar: ")
            if idx_texto.isdigit():
                idx = int(idx_texto) - 1
                if idx >= 0 and idx < len(entradas):
                    e = entradas[idx]
                    nuevo_titulo = input("Nuevo título (ENTER para mantener): ")
                    nuevo_contenido = input("Nuevo contenido (ENTER para mantener): ")
                    nuevo_autor = input("Nuevo autor (ENTER para mantener): ")
                    if nuevo_titulo != "":
                        e.titulo = nuevo_titulo
                    if nuevo_contenido != "":
                        e.contenido = nuevo_contenido
                    if nuevo_autor != "":
                        e.autor = nuevo_autor
                    guardar_pickle("entradas.bin", entradas)
                    print("Entrada actualizada.")
                else:
                    print("Índice fuera de rango.")
            else:
                print("Entrada no válida.")
        elif opcion == "4":  # DELETE
            idx_texto = input("Número de entrada a eliminar: ")
            if idx_texto.isdigit():
                idx = int(idx_texto) - 1
                if idx >= 0 and idx < len(entradas):
                    entradas.pop(idx)
                    guardar_pickle("entradas.bin", entradas)
                    print("Entrada eliminada.")
                else:
                    print("Índice fuera de rango.")
            else:
                print("Entrada no válida.")
        elif opcion == "5":
            print("Saliendo...")
            break
        else:
            print("Opción no válida.")

# ============================================================================
# UNIDAD 007 — INTEGRACIÓN CON BASE DE DATOS (SQLite) (base de datos, sqlite)
# ============================================================================
# Theory (EN):
# - SQLite is a file-based relational database. Ideal for small console apps.
# - Steps: connect, ensure table, do CRUD with parameterized queries, close.
# Palabras clave (ES): base de datos, conectar, tabla, SELECT, INSERT, UPDATE, DELETE.
# ---------------------------------------------------------------------------

import sqlite3

def conectar_sqlite():
    con = sqlite3.connect("blog.db")
    cur = con.cursor()
    return con, cur

def asegurar_tabla_entradas():
    con, cur = conectar_sqlite()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS entradas(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        titulo TEXT NOT NULL,
        contenido TEXT NOT NULL,
        autor TEXT NOT NULL
    );
    """)
    con.commit()
    con.close()

def crear_entrada_sqlite(titulo, contenido, autor):
    con, cur = conectar_sqlite()
    cur.execute("INSERT INTO entradas (titulo, contenido, autor) VALUES (?, ?, ?)", (titulo, contenido, autor))
    con.commit()
    con.close()

def listar_entradas_sqlite():
    con, cur = conectar_sqlite()
    cur.execute("SELECT id, titulo, autor, contenido FROM entradas ORDER BY id ASC")
    filas = cur.fetchall()
    con.close()
    return filas

def actualizar_entrada_sqlite(id_num, nuevo_titulo, nuevo_contenido):
    con, cur = conectar_sqlite()
    cur.execute("UPDATE entradas SET titulo=?, contenido=? WHERE id=?", (nuevo_titulo, nuevo_contenido, id_num))
    con.commit()
    con.close()

def eliminar_entrada_sqlite(id_num):
    con, cur = conectar_sqlite()
    cur.execute("DELETE FROM entradas WHERE id=?", (id_num,))
    con.commit()
    con.close()

# Menú CRUD conectado a SQLite (menú, CRUD, base de datos)
def app_crud_sqlite():
    asegurar_tabla_entradas()
    print("Bienvenido al panel de control (SQLite).")
    while True:
        print("")
        print("1) Crear   2) Listar   3) Actualizar   4) Eliminar   5) Salir")
        opcion = input("Opción: ").strip()

        if opcion == "1":
            t = input("Título: ")
            c = input("Contenido: ")
            a = input("Autor: ")
            crear_entrada_sqlite(t, c, a)
            print("Entrada creada.")
        elif opcion == "2":
            filas = listar_entradas_sqlite()
            if len(filas) == 0:
                print("Sin entradas.")
            else:
                for fila in filas:
                    # fila = (id, titulo, autor, contenido)
                    print("ID:" + str(fila[0]) + " | " + fila[1] + " — " + fila[2])
                    print(fila[3])
                    print("")
        elif opcion == "3":
            id_texto = input("ID a modificar: ")
            if id_texto.isdigit():
                id_num = int(id_texto)
                nt = input("Nuevo título: ")
                nc = input("Nuevo contenido: ")
                actualizar_entrada_sqlite(id_num, nt, nc)
                print("Entrada actualizada.")
            else:
                print("ID no válido.")
        elif opcion == "4":
            id_texto = input("ID a eliminar: ")
            if id_texto.isdigit():
                id_num = int(id_texto)
                eliminar_entrada_sqlite(id_num)
                print("Entrada eliminada.")
            else:
                print("ID no válido.")
        elif opcion == "5":
            print("Saliendo...")
            break
        else:
            print("Opción no válida.")

# ---------------------------------------------------------------------------
# PLANTILLA MYSQL (opcional) (mysql.connector) — Solo si el entorno lo permite
# ---------------------------------------------------------------------------
# Comentado a propósito; usar si hay MySQL y mysql-connector-python instalado.
"""
import mysql.connector

conexion = mysql.connector.connect(
    host="localhost",
    user="useroscar",
    password="tu_password",
    database="BlogDB"
)
cursor = conexion.cursor()
cursor.execute("SELECT * FROM entradas;")
filas = cursor.fetchall()
print(filas)
conexion.close()
"""

# ============================================================================
# CONCLUSIÓN (conclusión)
# ============================================================================
# Summary (EN):
# - You now have one place with all core patterns you learned in Units 001–007.
# - All examples are simple, in the same style as class, and ready to reuse.
# - For persistence, you can pick between pickle or SQLite depending on context.
# - Use search with Spanish keywords to jump to any topic quickly.
# ---------------------------------------------------------------------------

# FIN DEL ARCHIVO
# ============================================================================
