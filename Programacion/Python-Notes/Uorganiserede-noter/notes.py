# ==========================================
#  PYTHON CHEAT SHEET – OSCAR SØRENSEN
#  Updated: 29 October 2025
# ==========================================

# ---------- 1. VARIABLES & TYPES ----------
x = 5           # int
y = 3.5         # float
name = "Oscar"  # str
active = True   # bool

# check data type
print(type(x))

# type conversion
a = int("10")
b = float("3.14")
c = str(123)
d = bool(1)

# ---------- 2. INPUT / OUTPUT ----------
# input() always returns a string
nombre = input("Tu nombre: ")
edad = int(input("Tu edad: "))
print("Hola,", nombre, "tienes", edad, "años.")

# ---------- 3. LISTS ----------
dias = [1, 3, 4, 0, 2]
print(dias[0])       # first element
print(len(dias))     # number of elements
print(sum(dias))     # sum of all elements
dias.append(5)       # add new element
dias.remove(0)       # remove element by value

# ---------- 4. LOOPS ----------
# for loop
for numero in range(1, 6):
    print("Número:", numero)

# while loop
contador = 0
while contador < 5:
    print("Contador:", contador)
    contador += 1

# ---------- 5. CONDITIONS ----------
x = 10
if x > 5:
    print("Mayor que 5")
elif x == 5:
    print("Igual a 5")
else:
    print("Menor que 5")

# ---------- 6. FUNCTIONS ----------
def saludar(nombre):
    print("Hola,", nombre)

saludar("Oscar")

# function with return value
def sumar(a, b):
    return a + b

resultado = sumar(3, 4)
print("Resultado:", resultado)

testtest
# ---------- 7. EXCEPTION HANDLING ----------
# try / except prevents the program from crashing
try:
    numero = int(input("Introduce un número: "))
    resultado = 10 / numero
    print("Resultado:", resultado)
except ZeroDivisionError:
    print("Error: No se puede dividir entre cero.")
except ValueError:
    print("Error: Debes introducir un número válido.")
finally:
    print("Fin del programa.")

# ---------- 8. STRINGS ----------
texto = "Hola Mundo"
print(texto.lower())   # hola mundo
print(texto.upper())   # HOLA MUNDO
print(texto[0:4])      # Hola
print(len(texto))      # 10

# ---------- 9. FILES (BÁSICO) ----------
# writing to a file
with open("archivo.txt", "w") as f:
    f.write("Hola desde Python.\n")

# reading a file
with open("archivo.txt", "r") as f:
    contenido = f.read()
    print(contenido)

# ---------- 10. COMMON BUILT-IN FUNCTIONS ----------
# sum(), len(), range(), type(), print(), input(), int(), float(), str()
# round(), min(), max(), abs(), sorted()

# ---------- 11. COMMENTS ----------
# one-line comment
"""
multi-line
comment
"""

# ---------- 12. SMALL REFERENCE EXAMPLES ----------

# average of list values
dias_al_gimnasio = [1, 3, 4, 0, 2]
try:
    promedio = sum(dias_al_gimnasio) / len(dias_al_gimnasio)
    print("Promedio:", promedio)
except ZeroDivisionError:
    print("No hay datos disponibles")

# dictionary example
persona = {"nombre": "Oscar", "edad": 25, "activo": True}
print(persona["nombre"])
print(persona.keys())
print(persona.values())

# end of cheat sheet
# ==========================================



# ==========================================
# PYTHON OPERATORS CHEAT SHEET
# ==========================================

# ---------- 1. COMPARISON OPERATORS ----------
# Used to compare two values. They always return True or False.

x = 5
y = 3

print(x == y)   # Equal to → False (5 is not equal to 3)
print(x != y)   # Not equal to → True (5 is different from 3)
print(x > y)    # Greater than → True
print(x < y)    # Less than → False
print(x >= y)   # Greater than or equal → True
print(x <= y)   # Less than or equal → False

# You can use these in if-statements:
if x != 0:
    print("x is not zero")

# ---------- 2. LOGICAL OPERATORS ----------
# Used to combine multiple conditions.

a = True
b = False

print(a and b)  # True if both are True → False
print(a or b)   # True if at least one is True → True
print(not a)    # Negates (inverts) a value → False

# Example:
edad = 25
tiene_licencia = True

if edad >= 18 and tiene_licencia:
    print("Puede conducir")

# ---------- 3. ASSIGNMENT OPERATORS ----------
# Used to store or modify variable values.

x = 10      # Assigns 10
x += 5      # Add and assign → x = x + 5 → 15
x -= 3      # Subtract and assign → x = x - 3 → 12
x *= 2      # Multiply and assign → x = x * 2 → 24
x /= 4      # Divide and assign → x = x / 4 → 6.0
x %= 4      # Modulus and assign → x = x % 4 → remainder after division
print(x)

# ---------- 4. MEMBERSHIP OPERATORS ----------
# Check if something is inside a list, string, or other sequence.

frutas = ["manzana", "pera", "plátano"]
print("manzana" in frutas)      # True
print("naranja" not in frutas)  # True

# ---------- 5. IDENTITY OPERATORS ----------
# Check if two variables refer to the same object in memory (rarely needed for CEAC-level work).

a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a is b)   # True (same object)
print(a is c)   # False (same values, different object)
print(a is not c) # True

# ---------- 6. COMMON COMBINATIONS ----------
edad = 20
if edad > 0 and edad < 120:
    print("Edad válida")

numero = 0
if numero != 0:
    print("No es cero")
else:
    print("Es cero")

# end of cheat sheet
# ==========================================
