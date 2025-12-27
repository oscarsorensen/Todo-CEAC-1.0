
#En esta tarea, practico el trabajo con matrices multidimensionales para organizar la información de forma estructurada. Este tipo de matrices nos permiten almacenar datos en diferentes «niveles», como estantes, filas y columnas en un almacén. Sin embargo, en mi ejemplo a continuación solo utilizo la matriz para alimentos saludables. 
#Las matrices son útiles porque muchas situaciones reales necesitan este tipo de organización, como la gestión de inventarios, el almacenamiento de datos de juegos o el manejo de información compleja en aplicaciones. Muchas bases de datos complejas también funcionan de esta manera.

#En la tarea que creo, utilizo y pruebo, utilizo matrices multidimensionales en Python. En primer lugar, defino una matriz con varios niveles para representar datos organizados; utilizo alimentos saludables. A continuación, accedo a elementos específicos utilizando sus índices y modifico los valores que contienen para mostrar cómo funciona. Todo esto muestra cómo funcionan las matrices multidimensionales y cómo se pueden utilizar para gestionar la información de forma clara y eficiente.

comidas_saludables = [
    [   # Day 1
        ["Ensalada de quinoa", "Ensalada de espinacas y fresas", "Ensalada de garbanzos"],
        ["Salmón al horno con espárragos", "Pollo a la parrilla con verduras", "Tofu salteado con brócoli"],
        ["Yogur griego con frutas", "Batido de proteínas con plátano", "Nueces y semillas mixtas"]
    ],
    [   # Day 2
        ["Avena con frutas y nueces", "Tostadas integrales con aguacate", "Smoothie bowl de frutas"],
        ["Ensalada de pollo con aguacate", "Pasta integral con salsa de tomate y albahaca", "Sopa de lentejas"],
        ["Frutas frescas", "Barra de granola casera", "Hummus con palitos de verduras"]

    ]
]

print(comidas_saludables[0][1][1])  # Day 1 - Pollo a la parrilla con verduras
print(comidas_saludables[1][2][2])  # Day 2 - Hummus con palitos de verduras

# Modificando un elemento específico
print(comidas_saludables[0][0][0])  # Valor original, Ensalada de quinoa
comidas_saludables[0][0][0] = "Ensalada de kale y aguacate (cambiado)"
print(comidas_saludables[0][0][0])  # Nuevo valor, Ensalada de kale y aguacate (cambiado)

# Acceder a todos los elementos de la matriz
for x in range(len(comidas_saludables)):
    for y in range(len(comidas_saludables[x])):
        for z in range(len(comidas_saludables[x][y])):
            print(f"Día {x}, fila {y}, columna {z}: {comidas_saludables[x][y][z]}")



#Output:
"""
Pollo a la parrilla con verduras
Hummus con palitos de verduras
Ensalada de quinoa
Ensalada de kale y aguacate (cambiado)
Día 0, fila 0, columna 0: Ensalada de kale y aguacate (cambiado)
Día 0, fila 0, columna 1: Ensalada de espinacas y fresas
Día 0, fila 0, columna 2: Ensalada de garbanzos
Día 0, fila 1, columna 0: Salmón al horno con espárragos
Día 0, fila 1, columna 1: Pollo a la parrilla con verduras
Día 0, fila 1, columna 2: Tofu salteado con brócoli
Día 0, fila 2, columna 0: Yogur griego con frutas
Día 0, fila 2, columna 1: Batido de proteínas con plátano
Día 0, fila 2, columna 2: Nueces y semillas mixtas
Día 1, fila 0, columna 0: Avena con frutas y nueces
Día 1, fila 0, columna 1: Tostadas integrales con aguacate
Día 1, fila 0, columna 2: Smoothie bowl de frutas
Día 1, fila 1, columna 0: Ensalada de pollo con aguacate
Día 1, fila 1, columna 1: Pasta integral con salsa de tomate y albahaca
Día 1, fila 1, columna 2: Sopa de lentejas
Día 1, fila 2, columna 0: Frutas frescas
Día 1, fila 2, columna 1: Barra de granola casera
Día 1, fila 2, columna 2: Hummus con palitos de verduras
"""

#Esta tarea me ayudó a practicar mi comprensión de cómo se utilizan las matrices multidimensionales para almacenar y gestionar datos complejos. Las definí, accedí a la información y modifiqué los valores. Esto es importante para la programación porque muchos problemas reales necesitan este tipo de organización de datos. Este ejercicio está directamente relacionado con la unidad, ya que muestra cómo los datos estructurados son esenciales en el desarrollo de software y la resolución de problemas.