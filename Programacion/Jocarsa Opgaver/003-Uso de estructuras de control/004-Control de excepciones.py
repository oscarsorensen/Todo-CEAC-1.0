

"""
En esta tarea desarrollo un programa para un entrenador fitness que necesita calcular
el promedio de los días que sus clientes han asistido al gimnasio durante el mes.
Es importante manejar excepciones, ya que puede ocurrir un error si no hay registros,
y el programa no debe interrumpirse.
"""

# Definición de variables
dias_al_gimnasio = [1, 3, 4, 0, 2]  # Ejemplo con datos

try:
    # Calcular el promedio de los días registrados
    promedio_dias = sum(dias_al_gimnasio) / len(dias_al_gimnasio)
except ZeroDivisionError:
    # Si la lista está vacía, no se puede dividir entre cero
    promedio_dias = "No hay datos disponibles"

# Salida del resultado
print("Promedio de días al gimnasio:", promedio_dias)

"""
Este ejercicio demuestra la importancia de manejar excepciones como ZeroDivisionError
para evitar que un programa se detenga ante errores comunes. En este caso,
se aplican los conceptos de control de excepciones aprendidos en la unidad,
asegurando que el programa sea más estable y confiable.
"""
