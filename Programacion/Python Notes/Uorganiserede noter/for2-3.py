# ==========================================
# EXAM NOTES — UNIDAD 2 & 3 (CEAC DAW)
# Author: Oscar Sørensen
# ==========================================
# These notes summarize everything needed for
# Units 2 (Objects) and 3 (Control Structures)
# for the CEAC "Programación" exam.
# ==========================================


# ==========================================
# --------- UNIT 2 — WORKING WITH OBJECTS ----------
# ==========================================

# ----- CLASSES AND OBJECTS -----
# A class is a blueprint. An object is a specific example.

class Book:
    def __init__(self, title):
        self.title = title          # Attribute belongs to the object

    def show_title(self):
        print("The title is", self.title)


b1 = Book("Example Book")
b1.show_title()


# ----- CONSTRUCTOR -----
# Runs automatically when an object is created.
# Always named __init__.

class Example:
    def __init__(self, value):
        self.value = value


# ----- ATTRIBUTES -----
# Variables that belong to the object.
# Access with self.attribute inside the class,
# or object.attribute outside the class.
x = Example(5)
print("Value:", x.value)


# ----- METHODS -----
# Functions defined inside a class.
# They always have "self" as the first parameter.

class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print("Hello, my name is", self.name)


p = Person("Oscar")
p.greet()


# ----- STATIC METHODS -----
# Do not depend on object data.
# Use @staticmethod decorator.
# Called directly from the class.

class Converter:
    @staticmethod
    def km_to_miles(km):
        return km * 0.621371

    @staticmethod
    def celsius_to_fahrenheit(c):
        return (c * 9/5) + 32


print("10 km =", Converter.km_to_miles(10), "miles")
print("25°C =", Converter.celsius_to_fahrenheit(25), "°F")


# ----- BUILT-IN OBJECTS -----
# Strings, lists, and dictionaries are objects with their own methods.

text = "hello world"
print("Uppercase:", text.upper())
print("Replace:", text.replace("world", "Oscar"))

nums = [3, 1, 2]
nums.append(4) # add element- here 4
nums.sort()
print("List:", nums)

person = {"name": "Oscar", "age": 25}
person["age"] = 26
print("Dictionary:", person)

# !!RELEVANT, BUT NOT FROM CLASS!!
# tuple = immutable ordered collection
# set()  = unordered unique elements


# ==========================================
# --------- UNIT 3 — CONTROL STRUCTURES ----------
# ==========================================

# ----- CONDITIONALS -----
x = 10
if x > 10:
    print("Greater than 10")
elif x == 10:
    print("Equal to 10")
else:
    print("Less than 10")

# Operators:
# ==  !=  >  <  >=  <=
# and / or / not


# ----- LOOPS -----
# FOR LOOP
for i in range(3):
    print("for i:", i)

# WHILE LOOP
count = 0
while count < 3:
    print("while:", count)
    count += 1


# ----- JUMP STATEMENTS -----
for n in range(1, 6):
    if n == 3:
        continue    # skip this number
    if n == 5:
        break       # stop completely
    print("n =", n)


# ----- TRY / EXCEPT -----
# Used to handle errors without stopping the program.
# Must have at least one except.

try:
    result = 10 / 0
except ZeroDivisionError:
    result = 0
print("Result:", result)


# ----- MULTIPLE EXCEPTIONS -----
try:
    x = int("abc")
    y = 10 / x
except ZeroDivisionError:
    print("Division by zero")
except ValueError:
    print("Conversion error")


# ----- ASSERTIONS -----
# Used to check assumptions during runtime.
def positive_square_root(n):
    assert n >= 0, "n must be non-negative"
    return n ** 0.5


print("sqrt(9) =", positive_square_root(9))
# positive_square_root(-1)  # would raise AssertionError


# ----- SMALL PRACTICAL EXAMPLE -----
def safe_divide(a, b):
    try:
        a = int(a)
        b = int(b)
        return a / b
    except ZeroDivisionError:
        return 0.0
    except ValueError:
        return "Error: not a number"


print("safe_divide(6, 3) =", safe_divide(6, 3))
print("safe_divide(4, 0) =", safe_divide(4, 0))
print("safe_divide(4, 'a') =", safe_divide(4, "a"))


# ----- FINAL REMINDERS -----
# - Always indent with 4 spaces
# - Use clear variable names
# - Each "if", "for", "while", "def" ends with a colon :
# - Use print() to show results, not return (unless asked)
# - No nested if unless required
# - Use try/except instead of big conditional chains when checking errors
# - Focus on clarity and correctness, not shortcuts
