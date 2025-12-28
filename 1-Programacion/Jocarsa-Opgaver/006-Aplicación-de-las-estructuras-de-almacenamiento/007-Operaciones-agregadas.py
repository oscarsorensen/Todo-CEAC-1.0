
#En este ejercicio, trabajo en la creación de una matriz 3x3 relacionada con los sudokus. Una sección válida de sudoku debe contener los números del 1 al 9 una sola vez, por lo que el objetivo del programa es generar una matriz y verificarlo. Para ello, utilizo conjuntos de Python, que ayudan a comprobar fácilmente la unicidad, ya que no permiten duplicados. Esto conecta el concepto de validación del sudoku con la programación práctica.
#El programa primero genera nueve números aleatorios entre 1 y 9 y los almacena en una lista. Luego, convierto esta lista en un conjunto y la comparo con un conjunto de referencia. Si ambos conjuntos coinciden, la matriz es válida. A continuación, la lista se transforma en una matriz 3x3. Después de validarla, el programa selecciona una posición aleatoria y elimina un número. Todo este proceso se repite hasta generar cinco matrices válidas, utilizando bucles, conjuntos y estructuras condicionales.

# ------------ 1 & 2 Generar una matriz bidimensional y Comprobar la validez de la matriz ------------

import random

core = {1,2,3,4,5,6,7,8,9}

contador = 0 # contador de matrices válidas generadas
while contador < 5:
    lista = []
    for i in range(9):
        lista.append(random.randint(1,9))  
    conjunto = set(lista)

    if conjunto == core:
        contador += 1
        print("core:", core)
        print("Lista:", lista)
        print("La matriz es válida")

        # convierto lista a matriz 
        matrix = [
            lista[0:3],
            lista[3:6],
            lista[6:9]
        ]

        print("Lista en formato matrix:", matrix)

# ------------ 3 Eliminar un número aleatorio: ------------
        fila = random.randint(0,2)
        columna = random.randint(0,2)
        matrix[fila][columna] = "_"

        print("Matriz despues elimino un numero")
        print(matrix)
        print("--------------- Matrix", contador, "---------------")

# ------------ 4 Repetir el proceso: ------------

#output:
"""
core: {1, 2, 3, 4, 5, 6, 7, 8, 9}
Lista: [3, 1, 4, 7, 8, 9, 2, 5, 6]
La matriz es válida
Lista en formato matrix: [[3, 1, 4], [7, 8, 9], [2, 5, 6]]
Matriz despues elimino un numero
[[3, 1, 4], ['_', 8, 9], [2, 5, 6]]
--------------- Matrix 1 ---------------
core: {1, 2, 3, 4, 5, 6, 7, 8, 9}
Lista: [3, 8, 1, 7, 4, 2, 5, 9, 6]
La matriz es válida
Lista en formato matrix: [[3, 8, 1], [7, 4, 2], [5, 9, 6]]
Matriz despues elimino un numero
[[3, 8, 1], [7, 4, '_'], [5, 9, 6]]
--------------- Matrix 2 ---------------
core: {1, 2, 3, 4, 5, 6, 7, 8, 9}
Lista: [8, 1, 4, 7, 5, 3, 9, 6, 2]
La matriz es válida
Lista en formato matrix: [[8, 1, 4], [7, 5, 3], [9, 6, 2]]
Matriz despues elimino un numero
[[8, 1, '_'], [7, 5, 3], [9, 6, 2]]
--------------- Matrix 3 ---------------
core: {1, 2, 3, 4, 5, 6, 7, 8, 9}
Lista: [7, 2, 3, 5, 6, 1, 4, 9, 8]
La matriz es válida
Lista en formato matrix: [[7, 2, 3], [5, 6, 1], [4, 9, 8]]
Matriz despues elimino un numero
[[7, 2, 3], ['_', 6, 1], [4, 9, 8]]
--------------- Matrix 4 ---------------
core: {1, 2, 3, 4, 5, 6, 7, 8, 9}
Lista: [6, 9, 3, 5, 1, 2, 4, 8, 7]
La matriz es válida
Lista en formato matrix: [[6, 9, 3], [5, 1, 2], [4, 8, 7]]
Matriz despues elimino un numero
[[6, 9, 3], [5, 1, 2], [4, 8, '_']]
--------------- Matrix 5 ---------------
"""

#Este ejercicio muestra cómo se utilizan los conjuntos para verificar que los valores no se repitan. También muestra cómo se puede utilizar esta lógica en problemas más complejos, como un programa completo de Sudoku. Al repetir el proceso automáticamente, el programa demuestra cómo la programación ayuda a gestionar la validación repetitiva de forma eficiente. Puedo ver fácilmente cómo utilizaría esto para crear un programa completo de Sudoku en la vida real.