

import zipfile

origen = '1. Scripts.txt'

destino = 'comprimidoscriptsfile.zip'

archivo_zip = zipfile.ZipFile(destino, 'w')
archivo.write(origen)

# this changes my file 1. Scripts from 16 bytes to 1 bytes after compression
# destino er det nye navn filen får 
# origen er filen som bliver komprimeret