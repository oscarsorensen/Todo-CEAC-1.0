
import zipfile

origen = 'miarchivo.txt'

destino = 'comprimido.zip'

archivo_zip = zipfile.ZipFile(destino, 'w')
archivo.write(origen)