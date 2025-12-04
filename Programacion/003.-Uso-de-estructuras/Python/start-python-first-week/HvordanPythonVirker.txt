'''
Programa calculadora de IVA
(c) 2025 Oscar
Esto es un ejercicio de clase
'''

# Define IVA
IVA = 0.21

# Toma entradas
nombre = input("Introduce el nombre: ")
precio_base = input("Introduce el precio de venta: ")
almacenamiento_gb = input("Introduce la capacidad del dispositivo (GB): ")
peso_g = input("Introduce el peso en gramos: ")
pantalla_pulgadas = input("Introduce el tamaño de la pantalla en pulgadas: ")

# Convierte tipos
precio_base = int(precio_base)
almacenamiento_gb = int(almacenamiento_gb)
peso_g = int(peso_g)
pantalla_pulgadas = int(pantalla_pulgadas)

# Calcula
total_iva = precio_base * IVA
precio_total = precio_base + total_iva
almacenamiento_mb = almacenamiento_gb * 1024
peso_kg = peso_g / 1000

# Compara sin if
presupuesto_max = 800.0
excede_presupuesto = precio_total > presupuesto_max

# Salida
print("Nombre:", nombre)
print("Precio base:", precio_base)
print("Precio total con IVA:", precio_total)
print("Almacenamiento:", almacenamiento_mb, "MB")
print("Peso:", peso_kg, "kg")
print("Excede presupuesto:", excede_presupuesto)

print("el total de IVA es:", total_iva)
print("El precio total es:", precio_total)
print("la cantiad de almacenamiento:", pantalla_pulgadas)
print("el peso en kg es:", peso_kg)
print("el maximo presupuesto es:", presupuesto_max)
print("Excede el presupuesto:", excede_presupuesto)
