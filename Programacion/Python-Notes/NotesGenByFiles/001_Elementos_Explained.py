# ==========================================
# UNIT 001 — Identificación de los elementos de un programa informático
# Keywords: (bloques, indentación, variables, tipos de datos, literales,
# constantes, operadores, entrada/salida, comentarios, funciones, módulos)
# ==========================================


# ---------- 1) BLOCKS & INDENTATION (bloques, indentación) ----------
# Python uses indentation (spaces at the start of a line) to define blocks of code.
# Standard is 4 spaces. Never mix tabs and spaces.
def show_blocks():                 # Define a function (función)
    for i in range(3):             # Start a loop that runs 3 times
        print("Loop index:", i)    # This line is inside the loop block
    # Back to this column = outside the loop block
show_blocks()                      # Call the function so it runs


# ---------- 2) VARIABLES (variables) ----------
# A variable is a named container for a value. Created by assignment (=).
greeting = "Hello, World"          # str (string / cadena)
age = 25                           # int (entero)
height = 1.82                      # float (decimal)
is_active = True                   # bool (booleano)

# Reassign values and use augmented assignment
age = age + 5                      # 30
age += 2                           # 32 (adds 2)
print("age:", age)

# Naming: snake_case is standard. Identifiers cannot start with digits.
user_name = "oscar_sorensen"       # (identificador en snake_case)


# ---------- 3) DATA TYPES (tipos de datos) ----------
n_int = 7                          # int (entero)
n_float = 2.5                      # float (decimal)
text = "text"                      # str (cadena)
flag = False                       # bool (booleano)
items = [1, 2, 3]                  # list (lista, mutable)
point = (10, 20)                   # tuple (tupla, inmutable)
        # Tuples (tuplas) are ordered collections like lists, but they are IMMUTABLE — 
        # meaning their contents cannot be changed once created. 
        # They use parentheses () instead of square brackets [].
        # Tuples are ideal for storing fixed groups of related data, such as coordinates, colors, or settings.
        # Example: point = (10, 20)
        # You can access elements by index (point[0] -> 10), but you cannot modify them (point[0] = 99 would cause an error).
        # Use tuples when you want data to remain constant throughout the program.

prefs = {"theme": "dark"}          # dict (diccionario, pares clave/valor)
        # Dictionaries (diccionarios) store data as key/value pairs (pares clave/valor). 
        # Each key must be unique and is used to access its corresponding value. 
        # Dictionaries are written with curly braces {} and use a colon (:) between each key and value.
        # Example: prefs = {"theme": "dark"}
        # You can retrieve values by key, e.g. prefs["theme"] -> "dark"
        # Dictionaries are MUTABLE — you can add, modify, or remove items after creation.
        # Example modifications:
        # prefs["language"] = "en"   # add new key/value
        # prefs["theme"] = "light"   # update existing value
        # del prefs["theme"]         # delete a key/value pair

unique = {1, 2, 3}                 # set (conjunto, sin duplicados)
        # Sets (conjuntos) are unordered collections of unique elements (sin duplicados).
        # They are written using curly braces {} like dictionaries, but without key/value pairs.
        # Example: unique = {1, 2, 3}
        # Sets automatically remove duplicates — {1, 2, 2, 3} becomes {1, 2, 3}.
        # They are useful for membership checks, removing duplicates from lists, 
        # and performing mathematical operations like union (|), intersection (&), and difference (-).
        # Example:
        # A = {1, 2, 3}; B = {3, 4, 5}
        # print(A | B)  # union -> {1, 2, 3, 4, 5}
        # print(A & B)  # intersection -> {3}
        # print(A - B)  # difference -> {1, 2}


print(type(items), type(prefs), type(unique))  # Show data types

# Conversions (conversiones de tipos)
n_from_str = int("10")             # "10" -> 10
f_from_str = float("2.5")          # "2.5" -> 2.5
        # The float() function converts a string or integer into a floating-point number (número decimal).
        # In this example, the string "2.5" becomes the numeric value 2.5.
        # This is essential when reading user input, because input() always returns text (str).
        # Example:
        # f_from_str = float("2.5")  # result: 2.5
        # Once converted, you can perform mathematical operations on it:
        # print(f_from_str * 2)  # -> 5.0
        # If the string cannot be converted (e.g., "abc"), Python will raise a ValueError.

s_from_num = str(123)              # 123 -> "123"
        # The bool() function converts a value into a Boolean (True or False).
        # In Python, the number 0 is considered False, and any nonzero number is True.
        # This is often used in conditions to test if a value is "empty" or "zero".
        # Example:
        # b_from_num = bool(0)      # -> False
        # b_from_num = bool(5)      # -> True
        # It also works with other data types:
        # bool("")  -> False (empty string)
        # bool([]) -> False (empty list)
        # bool("text") -> True (non-empty string)
        # This helps simplify conditions, for example:
        # if value: print("Has content")  # executes only if value is not empty or zero


# ---------- 4) LITERALS (literales) ----------
# A literal is a fixed value written directly in code.
answer = 42                        # int literal
pi = 3.14159                       # float literal
truth = True                       # boolean literal
hello = "Hello"                    # string literal
multiline = """This is
a multi-line string."""            # triple-quoted string (multi-línea)
print(hello, pi, truth)
print(multiline)


# ---------- 5) CONSTANTS BY CONVENTION (constantes) ----------
# Python has no enforced constants; we use UPPER_CASE names by convention.
TAX_RATE = 0.21                    # constant by convention
base_price = 100
total_price = base_price * (1 + TAX_RATE)
print("Total with tax:", total_price)


# ---------- 6) OPERATORS (operadores) ----------
a, b = 7, 3                        # multiple assignment

# Arithmetic (aritméticos)
print(a + b, a - b, a * b, a / b)  # + - * /  -> 10 4 21 2.333...
print(a // b)                      # // floor division -> 2 (entero)
print(a % b)                       # % modulus -> remainder 1
print(a ** b)                      # ** exponentiation -> 343

# Comparison (comparación) -> return bool
print(a == b, a != b, a > b, a >= b, a < b, a <= b)

# Logical (lógicos) with booleans
x, y = True, False
print(x and y, x or y, not x)      # and / or / not

# Membership (pertenencia) with sequences/collections
fruits = ["apple", "pear"]
print("apple" in fruits)           # True
print("orange" not in fruits)      # True

# Precedence (precedencia): ** > * / // % > + - > comparaciones > and > or.
# Use parentheses to make evaluation order explicit in exams.

# Comparison operators (operadores de comparación)
# These compare two values and return a Boolean result: True or False.
# They are used inside conditions (if statements, loops) to control program flow.

    # Operator | Meaning (English)              | Example (Result)
    # ------------------------------------------------------------
    # ==       | Equal to                       | 5 == 5   → True
    # !=       | Not equal to                   | 5 != 3   → True
    # >        | Greater than                   | 7 > 3    → True
    # >=       | Greater than or equal to       | 7 >= 7   → True
    # <        | Less than                      | 3 < 5    → True
    # <=       | Less than or equal to          | 4 <= 4   → True
    #
    # Example usage:
    # a, b = 7, 3
    # print(a == b)   # False
    # print(a > b)    # True
    # print(a != b)   # True
    #
    # These expressions are essential in conditional structures like:
    # if a > b:
    #     print("a is greater than b")



# ---------- 7) INPUT / OUTPUT (entrada/salida) ----------
# input() reads a line of user text (always returns str).
# print() shows output.
name = input("Enter your name: ")
age_str = input("Enter your age: ")
try:                               # try/except to catch conversion errors
    age_val = int(age_str)         # convert string to int
    print(f"Hello {name}. In 5 years you will be {age_val + 5}.")
except ValueError:                 # runs if int(...) fails
    print("Age must be a number.")

# The letter f before a string ("f-string") activates formatted string literals (cadenas formateadas).
# It allows you to insert variables or expressions directly inside curly braces {} within the string.
# Example:
# name = "Oscar"
# age_val = 25
# print(f"Hello {name}. In 5 years you will be {age_val + 5}.")
# → Output: Hello Oscar. In 5 years you will be 30.
#
# Without f-strings, you would need slower, more complex syntax:
# print("Hello " + name + ". In 5 years you will be " + str(age_val + 5))
#
# f-strings automatically convert values to text and can include calculations, functions, or formatting:
# print(f"Price: {9.99:.2f}")   # -> "Price: 9.99" (two decimals)
# print(f"Next year: {2025 + 1}")  # -> "Next year: 2026"
#
# In short: f-strings are cleaner, faster, and more readable for dynamic text output.



# ---------- 8) COMMENTS (comentarios) ----------
# Single-line comments start with '#'.
"""
This is a multi-line string often used for docstrings
or block comments to explain larger sections of code.
"""


# ---------- 9) FUNCTIONS & MODULES (funciones, módulos) ----------
# A function is a reusable block of code defined with 'def'.
# A module is a separate file/library you can import (e.g., math).

import math                        # (módulo estándar)

def circle_area(radius):           # Define a function with a parameter
    """Return area of a circle given its radius (radio)."""
    return math.pi * (radius ** 2) # Use math.pi and exponent operator

print("Area (r=2):", circle_area(2))

# Functions (funciones) let you group code into reusable blocks. 
# They are defined with the keyword 'def' followed by a name and parentheses.
# Any value passed between the parentheses is called a *parameter* (parámetro).
# You can then use that parameter inside the function’s code.
#
# The 'return' statement sends a result back to where the function was called.
# This makes functions ideal for calculations and repeated logic.
#
# Example:
# def circle_area(radius):
#     return math.pi * (radius ** 2)
# 
# When you call circle_area(2), Python:
# 1) Creates a variable radius = 2
# 2) Executes the function’s body
# 3) Returns the computed value (π * 2²)
#
# The import math line brings in the standard math module (módulo estándar),
# which contains mathematical constants and functions like math.pi, math.sqrt(), math.ceil(), etc.
#
# Example usage:
# print("Area (r=2):", circle_area(2))  -> Area (r=2): 12.566370614359172
#
# In summary:
# - Use 'def' to define reusable logic.
# - Use 'import' to bring in ready-made functions from other files or Python’s standard library.
# - Always include 'return' if you want the function to send back a value.



# ---------- 10) MINI PRACTICE ----------
# VAT calculator with formatting to 2 decimals
amount = 250
result = amount * (1 + TAX_RATE)
print(f"Amount {amount} -> Total {result:.2f}")

# Quick sanity check with assert (aseveración)
assert isinstance(result, float)   # should be float; raises if False

# The assert statement (aseveración) is used to test that something is True during program execution.
# If the condition inside assert is False, Python stops the program and raises an AssertionError.
# This is a quick way to catch logic errors or invalid results while developing.

# Example:
# assert isinstance(result, float)
# This checks that 'result' is a float (decimal number). 
# - If it IS a float, nothing happens and the program continues normally.
# - If it’s NOT a float, Python stops and prints an error like:
#   AssertionError: 

# You can also include a custom error message:
# assert result > 0, "Result must be positive"

# In short: use assert to confirm that important assumptions about your program are true.
# It’s mostly used for debugging or self-checks, not in final production code.

