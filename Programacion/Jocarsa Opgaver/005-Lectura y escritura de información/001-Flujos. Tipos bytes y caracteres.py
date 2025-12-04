
"""
En este ejercicio aplico los conceptos de lectura y escritura de archivos en Python.
La idea es crear una pequeña agenda digital para guardar nombres y correos electrónicos.
Esto me permite practicar la persistencia de datos y la manipulación básica de archivos.
"""

# Escribir un nuevo contacto
with open("agenda.txt", "a", encoding="utf-8") as archivo:
    archivo.write(input("Introduce el nombre del contacto: ") + "," +
                  input("Introduce el email del contacto: ") + "\n")

print("\nContacto guardado correctamente.\n")

# Leer y mostrar todos los contactos
print("Contactos guardados en la agenda:")
with open("agenda.txt", "r", encoding="utf-8") as archivo:
    for linea in archivo:
        nombre, email = linea.strip().split(",")
        print("Nombre:", nombre, "| Email:", email)

"""
Con este ejercicio he aprendido a leer y escribir información en archivos de texto,
guardando los datos de forma permanente. Comprendo cómo estas técnicas pueden aplicarse
en programas reales que necesiten registrar información de contactos, rutinas o recetas.
"""
