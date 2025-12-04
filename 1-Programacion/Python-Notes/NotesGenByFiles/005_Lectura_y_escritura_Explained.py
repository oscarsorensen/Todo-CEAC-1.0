# ==========================================
# UNIT 005 — Lectura y escritura de información (Reading and Writing Information)
# Keywords: (archivos, ficheros, lectura, escritura, pickle, binarios, json, persistencia)
# ==========================================

# ---------- 1) TEXT FILES ----------
# Files can be opened in text mode using open(filename, mode, encoding).

# 'w' -> write (overwrites existing file)
with open("example.txt", "w", encoding="utf-8") as f:
    f.write("First line\nSecond line")

# 'a' -> append (adds to end of file)
with open("example.txt", "a", encoding="utf-8") as f:
    f.write("\nAppended line")

# 'r' -> read
with open("example.txt", "r", encoding="utf-8") as f:
    for line in f:
        print("Line:", line.strip())


# ---------- 2) JSON (structured text) ----------
import json
data = {"name": "Oscar", "year": 2025}
with open("data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

with open("data.json", "r", encoding="utf-8") as f:
    result = json.load(f)
print("JSON loaded:", result)


# ---------- 3) PICKLE (binary files) ----------
import pickle
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def __repr__(self):
        return f"Product({self.name!r}, {self.price!r})"

products = [Product("Shaker", 9.99), Product("Bottle", 5.5)]

# Save binary
with open("products.bin", "wb") as f:
    pickle.dump(products, f)

# Load binary
with open("products.bin", "rb") as f:
    loaded = pickle.load(f)
print("Loaded from binary:", loaded)


# ---------- 4) FILESYSTEM OPERATIONS ----------
import os
print("Files in current folder:", os.listdir("."))

# Calculate total size of all files
total = 0
for root, dirs, files in os.walk("."):
    for fname in files:
        try:
            total += os.path.getsize(os.path.join(root, fname))
        except OSError:
            pass
print("Total bytes:", total)


# ---------- 5) ERROR HANDLING ----------
try:
    with open("maybe.txt", "r", encoding="utf-8") as f:
        print(f.read())
except FileNotFoundError:
    print("File not found -> creating new one.")
    with open("maybe.txt", "w", encoding="utf-8") as f:
        f.write("Created automatically.")


# ---------- 5B) MÉTODOS ESTÁTICOS (static methods) ----------
# Static methods belong to the class, not to individual objects.

class Entrenamiento:
    @staticmethod
    def calcular_puntuacion(series, repeticiones):
        return series * repeticiones

# Uso
resultado = Entrenamiento.calcular_puntuacion(4, 10)
print("Puntuación del entrenamiento:", resultado)

# ---------- 5C) MENÚ CRUD SIMPLE ----------
# Combine insert/list options inside a while-loop menu.

while True:
    print("\n1) Insertar cliente  2) Listar clientes  3) Salir")
    opcion = input("> ")

    if opcion == "1":
        insert_client()
    elif opcion == "2":
        list_clients()
    elif opcion == "3":
        print("Programa finalizado.")
        break
    else:
        print("Opción no válida.")



# ---------- 6) EXAM TIPS ----------
# - Know open() modes: r, w, a, rb, wb.
# - Understand difference between text and binary files.
# - Use pickle for saving/loading Python objects.
# - Handle missing files using try/except.
