
archivo = open("clientes.csv", "r")

lineas = archivo.readlines()

print (lineas)

for linea in lineas:
    partido = linea.split(",")
    print(partido)