# ==========================================
# COMBINED UNITS 001–005 (Explained)
# ==========================================



# ==========================================
# UNIT 002 — Utilización de objetos (Using Objects)
# Keywords: (objetos, métodos, propiedades, mutabilidad, cadenas, listas, tuplas, diccionarios, conjuntos)
# ==========================================

# Everything in Python is an object. Objects contain data (attributes) and functions (methods)
# that operate on that data.

# ---------- 1) STRINGS (cadenas) ----------
# Strings are sequences of characters. They are immutable (cannot be changed directly).

text = "  CEAC Programación 2025  "   # A string with spaces
print(text.strip())                    # Removes spaces at start/end
print(text.lower())                    # Converts to lowercase
print(text.upper())                    # Converts to uppercase
print(text.replace("2025", "2026"))    # Replace parts of the string
print("CEAC" in text)                  # Check membership (returns True if found)

# Splitting and joining strings
words = text.split()                   # Split into list of words
joined = "-".join(words)               # Join list back into string
print(words)
print(joined)


# ---------- 2) LISTS (listas) ----------
# Lists are ordered, mutable collections (can be changed).

numbers = [3, 1, 2]                   # Create a list
numbers.append(4)                     # Add element at the end
numbers.sort()                        # Sort list in place
print("Sorted list:", numbers)

numbers.insert(0, 99)                 # Insert 99 at index 0
print("After insert:", numbers)
print(numbers[0], numbers[-1])        # Access first and last element
print(numbers[1:3])                   # Slice (elements from 1 to 2)

removed = numbers.pop()               # Remove last element and return it
print("Removed:", removed, "Now:", numbers)


# ---------- 3) TUPLES (tuplas) ----------
# Tuples are like lists but immutable (cannot be changed).

point = (10, 20)
print(point[0], len(point))
# point[0] = 99  # Would cause error because tuples are immutable


# ---------- 4) DICTIONARIES (diccionarios) ----------
# Dictionaries store key/value pairs. You can add or modify entries dynamically.

student = {"name": "Oscar", "age": 25}
print(student["name"])                 # Access value by key
student["grade"] = 9.5                 # Add new key/value
print(student)

print(list(student.keys()))            # List of keys
print(list(student.values()))          # List of values
print(student.get("city", "Unknown"))  # Safe access (returns default if missing)


# ---------- 5) SETS (conjuntos) ----------
# Sets store unique, unordered elements. Useful for removing duplicates.

A = {1, 2, 3}
B = {3, 4, 5}
print("Union:", A | B)                # Union of both sets
print("Intersection:", A & B)         # Common elements
print("Difference:", A - B)           # In A but not B
print("Symmetric diff:", A ^ B)       # In one but not both


# ---------- 6) MUTABILITY (mutabilidad) ----------
# Mutable means the content can change without changing identity.

L = [1, 2, 3]
L[0] = 100                            # Modify first element
T = (1, 2, 3)
# T[0] = 100                          # Error (immutable)
D = {"x": 1}
D["x"] = 2                            # Modify dict value
print(L, D)


# ---------- 7) OBJECT METHODS (métodos de objeto) ----------
# Methods are functions attached to objects.

name = "oscar"
print(name.capitalize())               # Capitalize first letter
print(name.startswith("o"))            # Returns True if starts with "o"
print(",".join(["a", "b", "c"]))       # Join elements of list into a string


# ---------- 8) PRACTICE EXAMPLE ----------
# Normalize a list of emails (strip + lower) and remove duplicates.

emails = ["  A@X.com ", "b@y.com", "a@x.com"]
normalized = [e.strip().lower() for e in emails]   # Clean up each email
unique_emails = sorted(set(normalized))            # Convert to set (remove duplicates)
print(unique_emails)


# ---------- 9) EXAM TIPS ----------
# - Be able to manipulate strings, lists, dicts, and sets.
# - Remember which objects are mutable (list, dict, set) vs immutable (str, tuple).
# - Use methods correctly: list.append(), dict.get(), str.replace(), set.union().


# ==========================================
# UNIT 003 — Uso de estructuras de control (Use of Control Structures)
# Keywords: (condicionales, bucles, if, while, for, operadores lógicos, break, continue, pass)
# ==========================================

# Control structures determine which parts of the program execute and when.


# ---------- 1) CONDITIONALS (condicionales if/elif/else) ----------
# Used to execute different code depending on conditions.

score = 78
if score >= 90:
    grade = "A"                       # Block 1 executes if condition is True
elif score >= 70:
    grade = "B"                       # Block 2 executes if previous failed but this True
else:
    grade = "C"                       # If all fail, execute this block
print("Grade:", grade)


# ---------- 2) FOR LOOP (bucle for) ----------
# A for-loop repeats a block of code for each value in a sequence.
# range(start, stop) produces numbers from start to stop-1.

for i in range(1, 6):                 # i takes values 1,2,3,4,5
    print("Iteration:", i)            # Executed once per loop
# When range runs out, the loop ends automatically.


# ---------- 3) WHILE LOOP (bucle while) ----------
# A while-loop repeats as long as a condition remains True.

count = 0
while count < 3:
    print("Count:", count)
    count += 1                        # Must update variable to avoid infinite loop


# ---------- 4) BREAK, CONTINUE, PASS ----------
# These modify loop behavior.
for n in range(6):
    if n == 2:
        continue                      # Skip this iteration and continue with next
    if n == 4:
        break                         # Exit the loop entirely
    if n == 5:
        pass                          # Placeholder (does nothing)
    print("n =", n)
print("Loop finished")


# ---------- 5) LOGICAL OPERATORS (operadores lógicos) ----------
x, y, z = 5, 10, 20
if x < y and y < z:                   # Both conditions must be True
    print("Values increasing")
if x < y or y > z:                    # At least one True
    print("At least one condition True")
if not (x > y):                       # not reverses result
    print("x is not greater than y")


# ---------- 6) INPUT VALIDATION WITH LOOP ----------
# Program repeats until user gives valid number.
while True:
    entry = input("Enter a number 1–5: ")
    try:
        num = int(entry)
        if 1 <= num <= 5:
            print("Valid number:", num)
            break                      # Exit loop if valid
        else:
            print("Out of range.")
    except ValueError:
        print("Not a number. Try again.")


# ---------- 7) MINI PROJECT: HORSE STABLE PLANNER (planificador de cuadras) ----------
# Example combining input, conditions, math, and date modules.

import math
import datetime

horses = input("Enter number of horses: ")
if horses == "0":
    print("No horses, no stables needed.")
else:
    capacity = input("Stable capacity (horses per stable): ")
    stables_needed = math.ceil(int(horses) / int(capacity))
    today = datetime.date.today()
    is_weekend = today.isoweekday() in (6, 7)   # 6=Saturday,7=Sunday
    print("Date:", today, "Weekend?", is_weekend)
    print("Stables needed:", stables_needed)


# ---------- 8) EXAM TIPS ----------
# - Use indentation correctly for if/elif/else and loops.
# - Show input validation with try/except.
# - Demonstrate break/continue inside a loop.
# - Combine range(), input(), and conditions in one example.


# ==========================================
# UNIT 004 — Desarrollo de clases (Class Development)
# Keywords: (clase, objeto, propiedades, métodos, constructor, CRUD, getters, setters)
# ==========================================

# Classes combine data (attributes) and behavior (methods).
# You create multiple objects (instances) from one class.

# ---------- 1) DEFINE CLASS AND CONSTRUCTOR ----------
class Client:
    def __init__(self, name, email):   # (constructor)
        # 'self' refers to the specific object being created
        self.name = name               # property (propiedad)
        self.email = email             # property (propiedad)

    def show_info(self):               # method (método)
        print(f"Client: {self.name}, Email: {self.email}")

# Create and use an object
c = Client("Oscar", "o@example.com")
c.show_info()


# ---------- 2) LIST OF OBJECTS + CRUD MENU ----------
clients = []                           # lista para guardar objetos

class Client:
    def __init__(self, name, email):
        self.name = name
        self.email = email

def insert_client():
    name = input("Name: ")
    email = input("Email: ")
    clients.append(Client(name, email))
    print("Inserted.")

def list_clients():
    if len(clients) == 0:
        print("No clients yet.")
        return
    i = 1
    for c in clients:
        print(i, c.name, c.email)
        i = i + 1

# Simple CRUD (Create, Read, Update, Delete) simulation
while True:
    print("\n1) Insert  2) List  3) Exit")
    op = input("> ")
    if op == "1":
        insert_client()
    elif op == "2":
        list_clients()
    elif op == "3":
        break
    else:
        print("Invalid option")



# ---------- 3) PRIVATE ATTRIBUTES + GETTERS/SETTERS ----------
class BankAccount:
    def __init__(self):
        self._balance = 0.0            # underscore indicates internal use (privado)

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount

    def get_balance(self):
        return self._balance

acc = BankAccount()
acc.deposit(100)
acc.withdraw(40)
print("Balance:", acc.get_balance())


# ---------- 4) EXAM TIPS ----------
# - Include at least one __init__ constructor.
# - Show property assignment and access.
# - Demonstrate methods that modify data.
# - Use self consistently inside class methods.


# ==========================================
# UNIT 005 — Lectura y escritura de información (Reading and Writing Information)
# Keywords: (archivos, ficheros, lectura, escritura, pickle, binarios, json, persistencia)
# ==========================================

# ---------- 1) TEXT FILES ----------
# Files can be opened in text mode using open(filename, mode, encoding).

# 'w' -> write (overwrites existing file)
with open("example.txt", "w", encoding="utf-8") as f:
    f.write("First line\nSecond line")

# 'a' -> append (adds to end of file)
with open("example.txt", "a", encoding="utf-8") as f:
    f.write("\nAppended line")

# 'r' -> read
with open("example.txt", "r", encoding="utf-8") as f:
    for line in f:
        print("Line:", line.strip())


# ---------- 2) JSON (structured text) ----------
import json
data = {"name": "Oscar", "year": 2025}
with open("data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

with open("data.json", "r", encoding="utf-8") as f:
    result = json.load(f)
print("JSON loaded:", result)


# ---------- 3) PICKLE (binary files) ----------
import pickle
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def __repr__(self):
        return f"Product({self.name!r}, {self.price!r})"

products = [Product("Shaker", 9.99), Product("Bottle", 5.5)]

# Save binary
with open("products.bin", "wb") as f:
    pickle.dump(products, f)

# Load binary
with open("products.bin", "rb") as f:
    loaded = pickle.load(f)
print("Loaded from binary:", loaded)


# ---------- 4) FILESYSTEM OPERATIONS ----------
import os
print("Files in current folder:", os.listdir("."))

# Calculate total size of all files
total = 0
for root, dirs, files in os.walk("."):
    for fname in files:
        try:
            total += os.path.getsize(os.path.join(root, fname))
        except OSError:
            pass
print("Total bytes:", total)


# ---------- 5) ERROR HANDLING ----------
try:
    with open("maybe.txt", "r", encoding="utf-8") as f:
        print(f.read())
except FileNotFoundError:
    print("File not found -> creating new one.")
    with open("maybe.txt", "w", encoding="utf-8") as f:
        f.write("Created automatically.")


# ---------- 6) EXAM TIPS ----------
# - Know open() modes: r, w, a, rb, wb.
# - Understand difference between text and binary files.
# - Use pickle for saving/loading Python objects.
# - Handle missing files using try/except.
