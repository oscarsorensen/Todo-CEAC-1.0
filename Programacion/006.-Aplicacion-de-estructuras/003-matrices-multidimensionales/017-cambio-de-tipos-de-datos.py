
tupla = ("manzanas", "naranjas", "platanos")
# necesito meter una fruta mas
print(tupla)
lista = list(tupla)  # convierto la tupla en lista
print(lista)
lista.append("kiwi")  # agrego el nuevo elemento

# ahoora supongamos que tengo que volver a tupla
nueva_tupla = tuple(lista)  # convierto la lista en tupla
print(nueva_tupla)