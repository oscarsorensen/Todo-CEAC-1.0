"""
En esta tarea desarrollo un programa en Python que calcula el total de una factura aplicando el IVA y un descuento fijo.
El objetivo es practicar los elementos fundamentales de un programa informático: variables, constantes, entrada de datos, operaciones aritméticas y salida de resultados.
De este modo, se aplica la lógica condicional para determinar si el descuento debe aplicarse según el valor del producto, reforzando la comprensión de estructuras básicas en Python.
El programa comienza definiendo las constantes IVA y DESCUENTO, utilizadas para calcular los importes de la factura.
A continuación, solicita al usuario el nombre del cliente y el precio bruto del producto mediante input(), convirtiendo el valor a tipo float para poder operar con él.

Después se calcula el IVA correspondiente (precio_bruto * IVA) y el subtotal con IVA.
Mediante un operador de comparación, se comprueba si el precio bruto es mayor o igual a 50 €, y se guarda el resultado en una variable booleana.
Si la condición se cumple, se aplica un descuento fijo de 10 €; en caso contrario, el descuento es 0.
Finalmente, se calcula el total a pagar y se muestran todos los datos en pantalla con formato de dos decimales.
"""


"""
Autor: Oscar Sørensen
Versión: 1.0
Descripción: Este programa calcula el total de una factura aplicando IVA (21 %)
y un descuento fijo de 10 €, solo si el precio bruto es mayor o igual a 50 €.
Archivo: factura_con_iva_descuento.py
"""

# 1. Variables y constantes
IVA = 0.21
DESCUENTO = 10.0

# 2. Entrada de datos
nombre_cliente = input("Ingrese el nombre del cliente: ")
precio_bruto = float(input("Ingrese el precio bruto del producto (€): "))

# 3. Cálculos
iva_aplicado = precio_bruto * IVA
subtotal_con_iva = precio_bruto + iva_aplicado

# Determinar si se aplica descuento
aplica_descuento = precio_bruto >= 50

if aplica_descuento:
    descuento_aplicado = DESCUENTO
else:
    descuento_aplicado = 0.0

total_a_pagar = subtotal_con_iva - descuento_aplicado

# 4. Salida de datos
print("\n--- FACTURA ---")
print("Cliente:", nombre_cliente)
print(f"Precio bruto: {precio_bruto:.2f} €")
print(f"IVA aplicado (21%): {iva_aplicado:.2f} €")
print(f"Descuento aplicado: {descuento_aplicado:.2f} €. Descuento solo aplicado si el precio sin IVA es mas que 50 €.")
print(f"Total a pagar: {total_a_pagar:.2f} €")

"""
El ejercicio permite consolidar el uso de variables, constantes y estructuras condicionales en Python.
A través de un caso práctico sencillo, demuestra cómo automatizar cálculos con IVA y descuentos, reforzando la comprensión de la estructura básica de un programa informático.
"""





