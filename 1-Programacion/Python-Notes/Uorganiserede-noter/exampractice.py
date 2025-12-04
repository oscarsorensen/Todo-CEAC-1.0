# ==========================================
# Object Practice File
# Author: Oscar Sørensen
# Description:
#   Contains simple object-oriented examples
#   for studying Units 2–3 (CEAC DAW).
# ==========================================


# ---------- Example 1: Fruit ----------
class Fruit:
    def __init__(self, kind):
        self.kind = kind

    def kind_is(self):
        print("the kind is", self.kind)


f1 = Fruit("Banana")
f1.kind_is()

f2 = Fruit("Apple")
f2.kind_is()



# ---------- Example 2: Basic Book ----------
class Book:
    def __init__(self, title):
        self.title = title

    def title_is(self):
        print("the title is", self.title)


t1 = Book("Book one")
t1.title_is()

t2 = Book("Book two")
t2.title_is()



# ---------- Example 3: Book with change_title ----------
class Book:
    def __init__(self, title):
        self.title = title

    def title_is(self):
        print("the title is", self.title)

    def change_title(self, new_title):
        self.title = new_title


b1 = Book("Old title")
b1.title_is()

b1.change_title("New title")
b1.title_is()

# ==========================================
# Example 4: Static Methods (Converter)
# Author: Oscar Sørensen
# Description:
#   Demonstrates how to use @staticmethod in a class.
#   Static methods belong to the class, not to individual objects.
#   They do not use "self" and are often used for general calculations.
# ==========================================

class Converter:
    # ---------- Static Methods ----------
    # Static methods do not need "self"
    # They can be called using the class name directly.

    @staticmethod
    def km_to_miles(km):
        # Converts kilometers to miles
        # 1 kilometer = 0.621371 miles
        return km * 0.621371

    @staticmethod
    def celsius_to_fahrenheit(celsius):
        # Converts Celsius to Fahrenheit
        # Formula: (C × 9/5) + 32
        return (celsius * 9/5) + 32


# ---------- Example Usage ----------
# Static methods are called directly from the class name.
# No object creation is required.

print("10 kilometers is", Converter.km_to_miles(10), "miles")
print("25°C is", Converter.celsius_to_fahrenheit(25), "°F")

# Output:
# 10 kilometers is 6.21371 miles
# 25°C is 77.0 °F

# ==========================================
# Example 5: Working with Built-in Objects
# Author: Oscar Sørensen
# Description:
#   Demonstrates that strings, lists, and dictionaries
#   are objects with their own methods.
# ==========================================


# ---------- STRING OBJECT ----------
text = "hello world"

# Methods that belong to the string object
print("Uppercase:", text.upper())       # 'HELLO WORLD'
print("Lowercase:", text.lower())       # 'hello world'
print("Replace:", text.replace("world", "Oscar"))  # 'hello Oscar'
print("Split:", text.split())           # ['hello', 'world']

# len() is a global function, not a method
print("Length:", len(text))             # 11


# ---------- LIST OBJECT ----------
numbers = [3, 1, 4]
print("Original list:", numbers)

# List methods
numbers.append(2)                       # add at the end
print("After append:", numbers)

numbers.sort()                          # sort in place
print("After sort:", numbers)

numbers.remove(1)                       # remove a value
print("After remove:", numbers)

# len() works on lists too
print("List length:", len(numbers))


# ---------- DICTIONARY OBJECT ----------
person = {"name": "Oscar", "age": 25, "country": "Spain"}

# Dictionary methods
print("Keys:", person.keys())
print("Values:", person.values())
print("Items:", person.items())

# Access and modify values
print("Name:", person["name"])
person["age"] = 26
print("Updated age:", person["age"])

# Add a new key/value pair
person["language"] = "Python"
print("New dictionary:", person)


# ---------- SUMMARY ----------
# Strings, lists, and dictionaries are all objects.
# Each one has its own set of methods you can call with a dot (.)
# Example: text.upper(), numbers.append(), person.keys()

# !!RELEVANT, BUT NOT FROM CLASS!!
# Some other useful built-in objects:
#   set()  -> unique elements, supports .add() and .remove()
#   tuple  -> immutable ordered collection
