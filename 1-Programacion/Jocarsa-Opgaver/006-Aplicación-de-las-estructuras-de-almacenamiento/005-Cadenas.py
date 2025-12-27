#En esta tarea trabajo con cadenas, archivos CSV y expresiones regulares en Python. Divido mi nombre completo en partes, leo y proceso los datos de los clientes de un archivo CSV que creo y creo una expresión regular para validar las direcciones en español. Estas tareas muestran cómo la programación puede organizar y controlar información real, como los datos de los usuarios y los registros almacenados. En un gimnasio, este tipo de automatización ayudaría a registrar clientes más rápido y evitar errores al introducir sus datos.
#Utilizo split() para separar el texto del nombre, luego abro clientes.csv, leo sus líneas y divido cada campo con split(","), para que los datos queden estructurados. Después, creo un patrón de expresión regular que comprueba si una dirección tiene el texto de la calle, un número y un código postal de cinco dígitos, y lo pruebo con ejemplos válidos e inválidos. El código sigue las instrucciones y funciona correctamente.

#Part 1-4
nombre = "Oscar Sorensen"
print("Nombre completo:", nombre)

partido = nombre.split(" ")
print(partido)

print("----------------------------------------------------")

#Part 5
def leer_csv():
    archivo = open("clientes.csv","r")
    lineas = archivo.readlines()

    for linea in lineas:
        partidolineas = linea.split(",")
        print(partidolineas)

    archivo.close()

leer_csv()   

print("----------------------------------------------------")

#Part 6 & 7

import re

# Patron de direccion 
# Texto + numero + codigo postal de 5 cifras
patron_direccion = r'^[A-Za-zÁÉÍÓÚÜÑáéíóúüñ ]+\s+\d+\s+\d{5}$'

# Pruebas
direccion_mal = "Calle Mayor"
direccion_bien = "Calle Mayor 10 46001"

print(re.match(patron_direccion, direccion_mal))
print(re.match(patron_direccion, direccion_bien))

# Output:
"""
Nombre completo: Oscar Sorensen
['Oscar', 'Sorensen']
----------------------------------------------------
['id', 'nombre', 'apellidos', 'correo', 'telefono', 'direccion', 'ciudad', 'provincia', 'codigo_postal', 'empresa', 'NIF\n']
['1', 'Juan', 'Pérez', 'juan.perez@example.com', '612345678', 'Calle Mayor 10', 'Valencia', 'Valencia', '46001', 'TecnoSol', 'S-12345678Z\n']
----------------------------------------------------
None
<re.Match object; span=(0, 20), match='Calle Mayor 10 46001'>
"""

#Esta tarea me ayudó a practicar y comprender mejor cómo gestionar y validar datos en Python. Practiqué trabajando con texto, leyendo información CSV y utilizando expresiones regulares para controlar formatos. Estas herramientas son importantes porque se utilizan en sistemas reales para organizar datos y verificar la información introducida por los usuarios, lo que está directamente relacionado con lo que estamos aprendiendo en esta unidad.