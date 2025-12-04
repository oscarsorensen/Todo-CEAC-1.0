import zipfile
import os

carpeta = "1. Scripts"

for directorio, carpetas, archivos in os.walk(carpeta):
    for nombre_archivo in archivos:
        origen = os.path.join(directorio, nombre_archivo)
        destino = os.path.join(directorio, nombre_archivo + ".zip")
        archivo_zip = zipfile.ZipFile(destino, "w", compression=zipfile.ZIP_DEFLATED)
        archivo_zip.write(origen, arcname=nombre_archivo)
        archivo_zip.close()

print("Comprimido:", destino)

#dette comprimerer alt i mappen 1. Scripts. Individuelt. Ikke skide praktisk.
