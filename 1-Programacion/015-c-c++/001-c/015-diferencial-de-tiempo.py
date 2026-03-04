import time

inicio = time.time()

numero = 1.0000000432

for contador in range(235324544):
    numero = numero * 1.00000000645

fin = time.time()

print(f"El resultado es: {numero}")
print(f"Tiempo de ejecucion: {fin - inicio:.6f} segundos")
