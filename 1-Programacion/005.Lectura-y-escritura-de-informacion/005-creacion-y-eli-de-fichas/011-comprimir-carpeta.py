

import os
import zipfile

origen = "archivos"
destino = "archivos.zip"

archivo_zip = zipfile.ZipFile(destino, "w", zipfile.ZIP_DEFLATED)
for directorio, carpetas, archivos in os.walk(origen):
    for nombre_archivo in archivos:
        rutaarchivo = os.path.join(directorio, nombre_archivo)
        rutarelativa = os.path.relpath(rutaarchivo, origen)
        archivo_zip.write(rutaarchivo, rutarelativa)
        
archivo_zip.close()
    