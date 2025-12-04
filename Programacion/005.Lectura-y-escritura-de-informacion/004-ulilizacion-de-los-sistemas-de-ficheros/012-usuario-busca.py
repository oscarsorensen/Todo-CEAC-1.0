


archivo = open("mapa.txt",'r') #READ
busca = input("Introduce el temino a buscar: ")


lineas = archivo.readlines()

for linea in lineas:
    if busca in linea:
        print("#######################")
        print("Encontrado!: ",linea)
        