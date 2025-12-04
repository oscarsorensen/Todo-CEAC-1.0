
'''
Applicacion de gestion de productos
(c)2024 Oscar Sorensen

'''

#En esta applicacion no aplica importar librerias

#Definimos clases y funciones

class Producto():
    def __init__(self):
        self.nombre = None
        self.precio = 0.0
# creamos las variables globales 

productos = []

#Primero lanzamos un mensaje de bienvenida
print("Gestor de productos v1.0, Oscar Sorensen")
#Le mostaramos al usuario las opciones que tiene
print("Seleccione una opcion")
print("1.- Crear un nuevo producto")
print("2.- Mostrar los productos")
print("3.- Actualizar un producto")
print("4.- Eliminar un producto")
opcion = int(input("Escoga una opcion (1-4): "))
#en funcion de la opcion que coja el usuario
if opcion == 1:
    #0 bien creamos un nuevo producto
    print("creamos un nuevo producto")
    producto = Producto() #creamos un nuevo producto
    producto.nombre = input("Nombre del producto: ")
    producto.precio =input("Precio del producto: ")
    productos.append(producto) #lo añadimos a la lista de productos
    
    
elif opcion == 2:
    #0 bien mostramos los productos
    print("mostramos los productos")
elif opcion == 3:
    #0 bien actuazamos los productos
    print("actualizamos los productos")
elif opcion == 4:
    #0 bien eliminamos los productos
    print("vamos a eliminar los productos")
# Y volvemos a repetir