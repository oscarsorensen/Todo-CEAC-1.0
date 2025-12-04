#En este ejercicio trabajo con el manejo de errores y la depuración de código en Python.
#El objetivo de mi programa es crear una función llamada divide() que reciba dos parámetros, dividendo y divisor, y devuelva el resultado de dividirlos.
#A través de este ejercicio practico el uso de los bloques try y except, que permiten controlar errores sin que el programa se detenga.
#Este tipo de control es muy útil cuando los datos provienen del usuario, ya que evita fallos inesperados y mejora la fiabilidad del programa.

def divide(dividendo, divisor):
    try:
        dividendo = int(dividendo)
        divisor = int(divisor)

        if divisor != 0:
            return dividendo / divisor
        else:
            return False  # Indica error por división entre cero

    except ValueError:
        return "Error: No se puede dividir por texto"


for dividendo in range(-100, 100):
    for divisor in range(-100, 100):
        print(divide(dividendo, divisor))

print(divide(4, "a"))

#La función divide() que he desarrollado cumple con los requisitos del enunciado: convierte los valores a enteros, devuelve False si el divisor es cero y muestra un mensaje claro cuando el dato no es numérico.
#Gracias a esta práctica he entendido mejor cómo manejar excepciones y comprobar errores en Python, algo esencial para escribir código estable y fácil de depurar.
#El ejercicio me ha ayudado a ver la importancia de validar los datos antes de realizar operaciones como la división.