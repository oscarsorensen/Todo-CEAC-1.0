numeros = [
    1,
    2,
    "3",
    4,
    "cinco",
    "patata"
]

print(numeros)
numeros_etiquetas = ["cero", "uno", "dos", "tres", "cuatro", "cinco"]

def calculaDoble():
    for numero in numeros:
        try:                             # primero intentamos convertir 
            numero = int(numero)
            print(numero * 2)
        except:                          # si no se puede convertir buscamos la etiqueta
            centinela = False
            for i in range(0, len(numeros_etiquetas)):
                if numero == numeros_etiquetas[i]:
                    print(i * 2)
                    centinela = True
            if centinela == False:
                print("Mira tio, lo he intentado pero no he podido")

calculaDoble()
