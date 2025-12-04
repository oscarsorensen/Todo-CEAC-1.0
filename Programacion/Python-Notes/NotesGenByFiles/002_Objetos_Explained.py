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
