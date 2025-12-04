

class Cliente():
    #Este es ek metodo constructor
    def __init__(self):
        self.nombrecompleto = ""
        self.email = ""
        
    #Entos son setter y getters
    def setNombreCompleto(self, nuevonombre):
        self.nombrecompleto = nuevonombre
    def setEmail(self, nuevoemail):
        self.email = nuevoemail
    def getNombreCompleto(self):
        return self.nombrecompleto
    def getEmail(self):
        return self.email
    
#CRUD - Create, Read, Update, Delete
#CRUD SQL - INSERT, SELECT, UPDATE, DELETE

clientes = []            ##########Lista vacia de clientes

print("GEstor de clientes v0.1 Oscar Sorensen")
while True:
    print("Selecciona una opcion")
    print("1. Crear cliente")
    print("2. Obtener listado de clientes")
    opcion = int(input("Indica tu opcion (1 o 2): "))

    if opcion == 1:      #Los SETTERS se usan en las operaciones de creacion de nuevos elementes
        print("Voy a insertar un cliente")
        nuevocliente = Cliente()
        nombrecliente = input("Indica el nombre del cliente: ") #Tomo el dato
        nuevocliente.setNombreCompleto(nombrecliente) #Uso el metodo set para meter el dato en el objeto
        emailcliente = input("Indica el email del cliente: ") #Tomo el dato
        nuevocliente.setEmail(emailcliente) #Uso el metodo set para meter el dato en el objeto
        clientes.append(nuevocliente)  #y por ultimo inserto el objeto en la lista
    elif opcion == 2:       #Los GETTERS se usan en las operaciones de listado
        print("Saco el listado de clientes")
        for cliente in clientes:
            print("nombre", cliente.getNombreCompleto())
            print("email", cliente.getEmail())
            print("--------------")    
        
        