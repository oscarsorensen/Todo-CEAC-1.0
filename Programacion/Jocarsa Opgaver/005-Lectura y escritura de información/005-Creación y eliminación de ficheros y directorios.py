"""
En este ejercicio aplico los conceptos de creación, eliminación y compresión de archivos en Python.
El objetivo es practicar el uso de las funciones open(), remove() y la clase ZipFile del módulo zipfile.
Estas operaciones son fundamentales para gestionar y empaquetar información dentro del sistema de archivos.
"""

import os
import zipfile

##parte 1 - creación y eliminación de archivos
with open("miarchivo.txt", "w", encoding="utf-8") as f: # Crear y escribir en un archivo
    f.write("Este es un archivo de prueba.")

print("Archivo 'miarchivo.txt' creado correctamente.")

os.remove("miarchivo.txt")
print("Archivo 'miarchivo.txt' eliminado correctamente.")



##parte 2 - compresión de archivos

origen = "crmca_crmcapitol (1).sql"   # archivo que quiero comprimir
destino = "basededatos.zip"           # nombre del archivo comprimido

with zipfile.ZipFile(destino, "w") as archivo_zip:
    archivo_zip.write(origen, arcname=os.path.basename(origen))

print(f"Archivo '{origen}' comprimido correctamente en '{destino}'.")
os.remove(origen)
print(f"Archivo original '{origen}' eliminado.")




"""
Con este ejercicio he aprendido a crear, escribir, eliminar y comprimir archivos con Python.
Comprendo cómo el módulo zipfile permite agrupar y reducir el tamaño de los datos, y cómo
las funciones open() y remove() me ayudan a gestionar el sistema de archivos de forma segura.
"""
