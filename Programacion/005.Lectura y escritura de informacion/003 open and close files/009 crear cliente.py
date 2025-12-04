

class Cliente():
    def __iniit__(self, nuevonombre, nuevoemail):
        self.nombre = nuevonombre
        self.email = nuevoemail
        
clientes = []

clientes.append(Cliente("Oscar Sorensen","info@oscar.com"))
clientes.append(Cliente("Juan Bob","info@juan.com"))

print(clientes)


class Cliente:
    def __init__(self, nuevonombre, nuevoemail):
        self.nombre = nuevonombre
        self.email = nuevoemail

    def __str__(self):
        return f"Nombre: {self.nombre}, Email: {self.email}"

clientes = []

clientes.append(Cliente("Oscar Sorensen", "info@oscar.com"))
clientes.append(Cliente("Juan Bob", "info@juan.com"))

for cliente in clientes:
    print(cliente)
