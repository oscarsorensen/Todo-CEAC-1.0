import pickle

class Cliente:
    def __init__(self, nuevonombre, nuevoemail):
        self.nombre = nuevonombre
        self.email = nuevoemail


clientes = []

clientes.append(Cliente("Oscar Sorensen", "info@oscar.com"))
clientes.append(Cliente("Juan Bob", "info@juan.com"))

archivo = open("clientes.bin","wb")
pickle.dump(clientes,archivo)
archivo.close()