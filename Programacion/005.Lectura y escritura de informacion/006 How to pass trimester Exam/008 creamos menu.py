



    
    class Cliente():
        def __init__(self,nombre,apellido,email):
            self.nombre = nombre
            self.apellido = apellido
            self.email = email
            
            
print("**************** Gestion de clientes v0.1******************")
print("****************** Oscar Sorensen **************************")

[clientes] = []

while True:
    print("Escoge una opcion: ")
    print("1. Crear cliente")
    print("2. Listar clientes")
    print("3. Actualizar cliente")
    print("4. Eliminar cliente")
    opcion = int(input("Escoge una opcion: "))