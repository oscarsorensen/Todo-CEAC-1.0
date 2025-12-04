"""En esta actividad aplico el concepto de métodos dentro de una clase en Python para realizar operaciones matemáticas básicas.
He creado una clase llamada Matematicas que representa una herramienta sencilla para redondear números, lo cual resulta útil en muchas situaciones cotidianas, como calcular precios, medidas o resultados con decimales.
Este ejercicio me permite relacionar la programación con operaciones matemáticas reales y comprender cómo organizar funciones dentro de una misma clase.
"""

"""La clase Matematicas incluye un constructor __init__() que inicializa el atributo PI, demostrando cómo definir valores internos en una clase.
Dentro de la clase se implementan tres métodos principales:

redondeo(numero): calcula la parte entera y la parte decimal del número. Si el decimal es menor que 0.5, el método devuelve el número redondeado hacia abajo; si es mayor o igual, lo redondea hacia arriba.

techo(numero): devuelve el número redondeado hacia arriba (al siguiente entero) siempre que tenga una parte decimal.

suelo(numero): realiza un redondeo real hacia abajo, incluso con números negativos. Para lograrlo, comprueba si el número es menor que cero y tiene parte decimal, restando uno al valor entero para obtener el resultado correcto.

Cada método utiliza estructuras condicionales if/else para decidir la operación a realizar, sin emplear librerías externas.
Finalmente, se crea un objeto mate = Matematicas() y se prueban los tres métodos con varios valores positivos y negativos, mostrando los resultados en pantalla."""

"""
Programa: RedondeosAlzaBaja
Versión: 0.1
Autor: Oscar Sorensen
Descripción: Implementación de una clase Matematicas para realizar redondeos hacia alza y baja sin usar la librería estándar de Python.
"""

class Matematicas: # Clase para operaciones matemáticas básicas
    def __init__(self):          # Constructor
        self.PI = 3.14159265359

    def redondeo(self, numero): #metodo de redondeo al entero más cercano
        entero = int(numero)
        decimal = numero - entero
        if decimal < 0.5:
            return entero            # baja
        else:
            return entero + 1        # alza

    def techo(self, numero): # método de redondeo hacia arriba
        entero = int(numero)
        decimal = numero - entero
        if decimal == 0:
            return entero            # ya es entero
        else:
            return entero + 1        # redondeo hacia arriba

    def suelo(self, numero):
        entero = int(numero)
        if numero < 0 and numero != entero:
            return entero - 1   # adjust for negatives
        else:
            return entero



# Pruebas
mate = Matematicas()
print("redondeo(4.7) : ", mate.redondeo(4.7))   
print("redondeo(4.2) : ", mate.redondeo(4.2))   
print("techo(4.2) : ", mate.techo(4.2))      
print("suelo(4.7) : ", mate.suelo(4.7))      


"""Con este ejercicio comprendí cómo definir varios métodos dentro de una misma clase y cómo aplicar condiciones lógicas para controlar su comportamiento.
En especial, el método suelo() me permitió entender la diferencia entre truncar y redondear hacia abajo, algo esencial al trabajar con números negativos.
El uso de clases como Matematicas facilita mantener las funciones organizadas y reutilizables, aplicando los principios básicos de la programación orientada a objetos de forma práctica y estructurada."""