
# ============================================================================
# EXAM RESUMEN — PROGRAMACIÓN (UNIDADES 001–007)  —  Oscar Sørensen
# Profesor: José Vicente Carratalá (CEAC)
# Objetivo: Referencia rápida, organizada y lista para copiar/pegar en examen.
# Estructura: resumen teórico (EN) + palabras clave (ES) + ejemplos claros.
# ============================================================================
#
# HOW TO USE THIS FILE
# - Press Ctrl/Cmd+F and search Spanish keywords in parentheses.
# - Each unit has: brief theory, then minimal but complete code samples.
# - All samples run independently. Copy only the block you need.
#
# TABLE OF CONTENTS
#  1) Unit 001 — Variables, Types, Operators (variables, tipos, operadores)
#  2) Unit 002 — Conditionals & Loops (if, elif, while, for)
#  3) Unit 003 — Functions & Exceptions (funciones, try/except)
#  4) Unit 004 — Classes & Constructors (clases, propiedades, constructor)
#  5) Unit 005 — Files: Text, JSON, Pickle (archivos, json, pickle)
#  6) Unit 006 — Menu & CRUD (menú, CRUD, bucle infinito)
#  7) Unit 007 — DB Integration with SQLite (base de datos, sqlite)
#     + Optional MySQL connector template (mysql.connector)
#  8) Appendix — Common Patterns & Tips (bucle while True, validación)
#
# ============================================================================
# 1) UNIT 001 — VARIABLES, TYPES, OPERATORS (variables, tipos, operadores)
# ----------------------------------------------------------------------------
# Theory (EN):
# - A variable stores a value. Python is dynamically typed, but you should name
#   things clearly to show intent. Basic types: int, float, str, bool.
# - Operators: + - * / // % **  and comparison: == != < <= > >=.
# - Casting: int("5"), float("3.14"), str(123), bool(0).
#
# Keywords (ES): variables, tipos de datos, operadores aritméticos, conversión.
#
# Example:
x = 5              # int
y = 2.5            # float
nombre = "Oscar"   # str
activo = True      # bool
suma = x + 3
es_mayor = x > 3
# print(suma, es_mayor, nombre, activo)

# ============================================================================
# 2) UNIT 002 — CONDITIONALS & LOOPS (if, elif, while, for)
# ----------------------------------------------------------------------------
# Theory (EN):
# - Use if/elif/else to branch logic (condicionales).
# - Use while for repeated actions with unknown count; for for known collections.
# - Always ensure while loops move toward a stopping condition.
#
# Keywords (ES): if, elif, else, bucle while, bucle for, condición.
#
# Examples:
def classify_number(n: int) -> str:
    # (if/elif/else)
    if n < 0:
        return "negativo"
    elif n == 0:
        return "cero"
    else:
        return "positivo"

def count_down(start: int):
    # (bucle while)
    while start > 0:
        # print(start)
        start -= 1

for i in range(3):   # (bucle for)
    pass             # print(i)

# ============================================================================
# 3) UNIT 003 — FUNCTIONS & EXCEPTIONS (funciones, try/except)
# ----------------------------------------------------------------------------
# Theory (EN):
# - A function (def) encapsulates behavior. Return values with return.
# - Use try/except to catch runtime errors (manejo de excepciones).
# - Validate and convert user input safely.
#
# Keywords (ES): funciones, parámetros, retorno, try, except, ValueError.
#
# Examples:
def add(a: float, b: float) -> float:
    return a + b

def safe_int(text: str, default: int = 0) -> int:
    try:
        return int(text)
    except ValueError:
        return default

# ============================================================================
# 4) UNIT 004 — CLASSES & CONSTRUCTORS (clases, propiedades, constructor)
# ----------------------------------------------------------------------------
# Theory (EN):
# - A class (clase) defines a blueprint with properties (atributos) and methods.
# - __init__ is the constructor (constructor) that initializes properties.
# - Use clear method names and keep state consistent.
#
# Keywords (ES): clase, propiedades, __init__, método, self.
#
# Examples:
class Entrada:
    def __init__(self, titulo: str, contenido: str, autor: str):
        self.titulo = titulo            # propiedad
        self.contenido = contenido
        self.autor = autor

    def resumen(self) -> str:
        return f"{self.titulo} — {self.autor}"

# e = Entrada("Hola", "Contenido", "Oscar")
# print(e.resumen())

# ============================================================================
# 5) UNIT 005 — FILES: TEXT, JSON, PICKLE (archivos, json, pickle)
# ----------------------------------------------------------------------------
# Theory (EN):
# - Text files are great for logs or simple exports.
# - JSON (texto estructurado) is human-readable and interoperable.
# - Pickle (binario) is the simplest way to persist Python objects (persistencia).
#
# Keywords (ES): archivos, lectura/escritura, json, pickle, persistencia.
#
# TEXT example:
def save_text(path: str, text: str) -> None:
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)

def read_text(path: str) -> str:
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

# JSON example:
import json
def save_json(path: str, data) -> None:
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def read_json(path: str):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

# PICKLE example (persistencia binaria):
import pickle
def save_pickle(path: str, obj) -> None:
    with open(path, "wb") as f:
        pickle.dump(obj, f)

def load_pickle(path: str):
    try:
        with open(path, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return None

# ============================================================================
# 6) UNIT 006 — MENU & CRUD (menú, CRUD, bucle infinito)
# ----------------------------------------------------------------------------
# Theory (EN):
# - A console CRUD has: welcome message, infinite loop (bucle infinito),
#   a menu (menú) with four options, and if/elif to route actions.
# - Data can live in memory (list) or be persisted with pickle.
#
# Keywords (ES): menú, bucle while True, CRUD, if/elif, lista en memoria.
#
# Minimal in‑memory CRUD for 'Entrada':
def ejemplo_crud_memoria():
    print("Bienvenido al panel de control (memoria).")
    entradas: list[Entrada] = []

    while True:  # (bucle infinito)
        print("\n1) Crear  2) Listar  3) Actualizar  4) Eliminar  5) Salir")
        opcion = input("Opción: ").strip()

        if opcion == "1":  # CREATE
            t = input("Título: ")
            c = input("Contenido: ")
            a = input("Autor: ")
            entradas.append(Entrada(t, c, a))
            print("Creada.")
        elif opcion == "2":  # READ
            if not entradas:
                print("Sin entradas.")
            for i, e in enumerate(entradas, start=1):
                print(f"{i}. {e.resumen()}")
        elif opcion == "3":  # UPDATE
            idx = input("Número de entrada a modificar: ")
            if idx.isdigit() and 1 <= int(idx) <= len(entradas):
                e = entradas[int(idx)-1]
                e.titulo = input("Nuevo título: ") or e.titulo
                e.contenido = input("Nuevo contenido: ") or e.contenido
                e.autor = input("Nuevo autor: ") or e.autor
                print("Actualizada.")
            else:
                print("Índice no válido.")
        elif opcion == "4":  # DELETE
            idx = input("Número de entrada a eliminar: ")
            if idx.isdigit() and 1 <= int(idx) <= len(entradas):
                entradas.pop(int(idx)-1)
                print("Eliminada.")
            else:
                print("Índice no válido.")
        elif opcion == "5":
            print("Saliendo...")
            break
        else:
            print("Opción no válida.")

# ============================================================================
# 7) UNIT 007 — DB INTEGRATION WITH SQLITE (base de datos, sqlite)
# ----------------------------------------------------------------------------
# Theory (EN):
# - SQLite is a file-based relational DB ideal for console apps in exams.
# - Steps: connect → ensure table → CRUD with parameterized queries.
#
# Keywords (ES): base de datos, tabla, conectar, SELECT, INSERT, UPDATE, DELETE.
#
# SQLite CRUD for 'entradas' (blog.db):
import sqlite3

def ensure_db():
    con = sqlite3.connect("blog.db")
    cur = con.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS entradas(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        titulo   TEXT NOT NULL,
        contenido TEXT NOT NULL,
        autor     TEXT NOT NULL
    );
    """)
    con.commit()
    return con, cur

def crear_sqlite(titulo: str, contenido: str, autor: str) -> None:
    con, cur = ensure_db()
    cur.execute("INSERT INTO entradas (titulo, contenido, autor) VALUES (?, ?, ?)", (titulo, contenido, autor))
    con.commit()
    con.close()

def listar_sqlite() -> list[tuple]:
    con, cur = ensure_db()
    cur.execute("SELECT id, titulo, autor, contenido FROM entradas ORDER BY id ASC")
    filas = cur.fetchall()
    con.close()
    return filas

def actualizar_sqlite(id_: int, nuevo_titulo: str, nuevo_contenido: str) -> None:
    con, cur = ensure_db()
    cur.execute("UPDATE entradas SET titulo=?, contenido=? WHERE id=?", (nuevo_titulo, nuevo_contenido, id_))
    con.commit()
    con.close()

def eliminar_sqlite(id_: int) -> None:
    con, cur = ensure_db()
    cur.execute("DELETE FROM entradas WHERE id=?", (id_,))
    con.commit()
    con.close()

# Minimal menu wired to SQLite:
def ejemplo_crud_sqlite():
    print("Bienvenido al panel de control (SQLite).")
    while True:
        print("\n1) Crear  2) Listar  3) Actualizar  4) Eliminar  5) Salir")
        opcion = input("Opción: ").strip()

        if opcion == "1":
            t = input("Título: ")
            c = input("Contenido: ")
            a = input("Autor: ")
            crear_sqlite(t, c, a)
            print("Creada.")
        elif opcion == "2":
            filas = listar_sqlite()
            if not filas:
                print("Sin entradas.")
            for (i, t, a, c) in filas:
                print(f"ID:{i} | {t} — {a}\n{c}\n")
        elif opcion == "3":
            i = int(input("ID a modificar: ") or "0")
            nt = input("Nuevo título: ")
            nc = input("Nuevo contenido: ")
            actualizar_sqlite(i, nt, nc)
            print("Actualizada.")
        elif opcion == "4":
            i = int(input("ID a eliminar: ") or "0")
            eliminar_sqlite(i)
            print("Eliminada.")
        elif opcion == "5":
            print("Saliendo...")
            break
        else:
            print("Opción no válida.")

# ----------------------------------------------------------------------------
# Optional: MySQL connector template (mysql.connector) — not executed here.
# Keywords (ES): mysql.connector, conectar, cursor, SELECT, INSERT.
# (Use only if your exam PC has MySQL and connector installed.)
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
print(cursor.fetchall())
conexion.close()
"""

# ============================================================================
# 8) APPENDIX — COMMON PATTERNS & TIPS (patrones comunes, consejos)
# ----------------------------------------------------------------------------
# Theory (EN):
# - Infinite loop + menu (bucle while True + menú): central to the exam.
# - Always validate numeric input before converting to int.
# - Handle exceptions around file/DB operations to avoid crashes.
#
# Keywords (ES): while True, menú, validar entrada, try/except.
#
def read_int(prompt: str, default: int = 0) -> int:
    text = input(prompt).strip()
    try:
        return int(text)
    except ValueError:
        return default

# Example pattern (skeleton):
def menu_skeleton():
    while True:
        print("\n1) Opción A  2) Opción B  3) Salir")
        op = input("Opción: ")
        if op == "1":
            pass
        elif op == "2":
            pass
        elif op == "3":
            break
        else:
            print("Opción no válida.")

# END OF FILE
# ============================================================================
