#En este ejercicio, creo un sencillo programa en Python para gestionar la lista de la compra de Juan, sus alimentos y el gimnasio. Podría tratarse de una tarea real para organizar productos y sus cantidades. Este ejercicio se ha diseñado para adaptarse a la rutina diaria de Juan y le ayuda a organizar sus compras y el gimnasio.
#El programa utiliza una lista para almacenar la lista de la compra. Cada producto se guarda como un diccionario con el nombre del producto y su cantidad. Se pueden añadir productos, ver la lista, modificar cantidades y eliminar productos mediante un menú. Todas las acciones se realizan utilizando listas y diccionarios, siguiendo las reglas del ejercicio. Todos los datos se pueden ver en el archivo json. También podría haber sido una lista de cosas relacionadas con el gimnasio.

print("Lista de la compra v0.1")
import json

lista_de_la_compra = []   # keep variable name the same

##########   Adding this part myself, so the list doesnt dissapear every time i close the program.         #############
try:
    archivo = open("lista.json", "r")
    lista_de_la_compra = json.load(archivo)
    archivo.close()
except:
    lista_de_la_compra = []
#############################

while True:
    print("Seleccione una opcion:")
    print("1. Añadir producto")
    print("2. Ver lista de la compra")
    print("3. Modificar un producto")
    print("4. Eliminar un producto")

    opcion = int(input("Ingrese el número de la opción deseada: "))
    
    if opcion == 1: ## Añadir producto
        print("Añadir producto")
        nombre = input("Ingrese el nombre del producto: ")
        cantidad = input("Ingrese la cantidad: ")  
        lista_de_la_compra.append({"producto": nombre, "cantidad": cantidad})

        archivo = open("lista.json", "w")
        json.dump(lista_de_la_compra, archivo)
        archivo.close()
        print(" ---------------- Producto añadido. ----------------")
        
    elif opcion == 2: ## Ver lista de la compra
        print("Lista de la compra:")
        for producto in lista_de_la_compra:
            print("-----------------------------")
            print("Producto:", producto["producto"])
            print("Cantidad:", producto["cantidad"])
            print("-----------------------------")

    elif opcion == 3: ## Modificar un producto
        nombre = input("Ingrese el nombre del producto a modificar: ")
        for producto in lista_de_la_compra:
            if producto["producto"] == nombre:
                nueva_cantidad = input("Ingrese la nueva cantidad: ")
                producto["cantidad"] = nueva_cantidad
                print("---------------- Producto modificado. ----------------")

        archivo = open("lista.json", "w") ## Guardar los cambios en el archivo
        json.dump(lista_de_la_compra, archivo)
        archivo.close() 

    elif opcion == 4: ## Eliminar un producto
        nombre = input("Ingrese el nombre del producto a eliminar: ")
        for producto in lista_de_la_compra:
            if producto["producto"] == nombre: ## Encontrar el producto y eliminarlo
                lista_de_la_compra.remove(producto)
                print("---------------- Producto eliminado. ----------------")

        archivo = open("lista.json", "w")
        json.dump(lista_de_la_compra, archivo)
        archivo.close()

#En este ejercicio, practiqué cómo usar listas y diccionarios en una situación cercana a la vida real. Practiqué cómo añadir, leer, modificar y eliminar datos, que son habilidades básicas e importantes en programación que se pueden usar en aplicaciones cotidianas. Puedo imaginar fácilmente cómo puedo usar esto en el futuro.