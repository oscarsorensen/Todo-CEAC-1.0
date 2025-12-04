"""En este ejercicio aplico el concepto de los métodos set y get dentro de una clase en Python para realizar operaciones básicas de modificación y consulta de datos.
He creado una clase llamada Cliente que representa a una persona con propiedades como nombre, apellidos, dirección y correo electrónico.
Este ejemplo permite relacionar la programación con situaciones del mundo real, donde los datos personales pueden cambiar y deben actualizarse de forma controlada.

La clase Cliente incluye un constructor `` __init__()`` con cuatro propiedades, junto con dos métodos: set_email() y get_email(), tal como indica el enunciado.
Posteriormente, he creado tres instancias de la clase —cliente1, cliente2 y cliente3—, cada una con sus propios valores.
Para demostrar el funcionamiento de los métodos, utilicé set_email() para modificar el correo electrónico de cada cliente y después get_email() para mostrar el nuevo valor y comprobar que el cambio se aplicó correctamente.
Estos métodos permiten acceder y modificar los datos de manera segura, respetando el principio de encapsulación dentro de la programación orientada a objetos.

````
"""
class Client:
    def __init__(self, nombre, apellido, direccion, email):   # (constructor)
        self.nombre = nombre               # property (propiedad)
        self.email = email             # property (propiedad)
        self.apellido = apellido
        self.direccion = direccion
        
    def get_email(self):               # method (método)
        return self.email
    
    def set_email(self, new_email):
        self.email = new_email

#Creamos tres instancias de la clase Client
cliente1 = Client("Oscar", "Sorensen", "calle Maximilia", "oscar@gmail.com")
cliente2 = Client("Sofia", "Sorensen", "Calle Madrid", "sofia@gmail.com")
cliente3 = Client("Jose", "Vicente", "noclue 123", "jose@gmail.com")

#Demostramos que los métodos set y get funcionan para cada una de las instancias
cliente1.set_email("oscarnewemail@gmail.com")
print("Cliente 1 new email:", cliente1.get_email())
cliente2.set_email("sofianewemail")
print("Cliente 2 new nombre:", cliente2.get_email())
cliente3.set_email("josevicentenewemail")
print("Cliente 3 new calle:", cliente3.get_email())
""""
````
Con esta actividad he practicado el uso de los métodos set y get dentro de una clase y su aplicación sobre propiedades específicas.
Estos métodos facilitan la modificación y lectura de los datos de los objetos de forma estructurada, aplicando los principios básicos de la programación orientada a objetos, como la organización, la reutilización del código y la claridad en el diseño.
"""