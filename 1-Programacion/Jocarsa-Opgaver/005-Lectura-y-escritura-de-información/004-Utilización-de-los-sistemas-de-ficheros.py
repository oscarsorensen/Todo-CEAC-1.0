"""
En este ejercicio aplico los conceptos de manejo de archivos y directorios en Python.
El objetivo es calcular el tamaño total de una carpeta y encontrar los archivos que 
ocupan más de un gigabyte. Esto me permite practicar el uso del módulo 'os' y las 
funciones listdir(), walk() y getsize().
"""

import os

carpeta = input("Indica una carpeta: ")

elementos = os.listdir(carpeta)

suma = 0

for elemento in elementos:
  ruta = os.path.join(carpeta, elemento)
  suma += os.path.getsize(ruta)

print("La carpeta ocupa:")
print(suma/(1024*1024),"MB")

import os

carpeta = input("Indica una carpeta: ")
grande = 1024*1024*1024 # 1 giga

for directorio, carpetas, archivos in os.walk(carpeta):
    for archivo in archivos:
        ruta = os.path.join(directorio, archivo)
        try:
            if os.path.getsize(ruta) > grande:
              print(ruta,os.path.getsize(ruta)/(1024*1024),"MB")
        except:
            pass


"""
Con este ejercicio he aprendido a recorrer carpetas con Python, calcular su tamaño
y detectar archivos grandes. Estos conocimientos pueden aplicarse en programas de 
mantenimiento o limpieza del sistema.
"""
