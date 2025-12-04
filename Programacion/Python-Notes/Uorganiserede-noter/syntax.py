# ==========================================
# PYTHON EXAM SYNTAX DISCIPLINE CHECKLIST
# Oscar Sørensen – CEAC DAW
# ==========================================
# Purpose: eliminate careless syntax errors and structure mistakes.
# Focus on: indentation, naming, function layout, control flow, exceptions.
# ==========================================


# ---------- 1) INDENTATION ----------
# • Always 4 spaces per block (NEVER tabs).
# • Blocks must align vertically — every def, if, for, while, etc.
#   must have its body indented exactly one level.
# • VS Code: enable "Render Whitespace" and "Tab Size: 4".
# • Press Shift + Tab to move code LEFT; Tab to move it RIGHT.

def example_indentation():
    for i in range(3):
        print(i)
    print("Done")  # aligned back to function scope


# ---------- 2) CLEAN NAMING ----------
# • Use lowercase_with_underscores for variables/functions.
# • Use CapitalizedWords for classes.
# • Constants in ALL_CAPS.
# • Avoid Spanish/accents/spaces in names (safe ASCII only).
tax_rate = 0.21
def calc_total(base): return base * (1 + tax_rate)
class Customer: pass
MAX_USERS = 10


# ---------- 3) PRINTING & STRINGS ----------
# • Always wrap text in quotes; prefer f-strings.
# • Use commas in print() instead of concatenation when stressed.
name = "Oscar"
print("Hello,", name)
print(f"Hello, {name}!")     # preferred
print("Value:", 10 * 2)


# ---------- 4) IF / ELIF / ELSE ----------
# • Every if-block must end with a colon.
# • elif and else aligned with their if.
x = 10
if x > 10:
    print("Greater")
elif x == 10:
    print("Equal")
else:
    print("Smaller")


# ---------- 5) LOOPS ----------
# • for i in range(n): standard counting loop.
# • while condition: needs counter increment inside.
# • Avoid infinite loops unless specifically asked (use break).

for i in range(3):
    print("Loop", i)

counter = 0
while counter < 3:
    print("While", counter)
    counter += 1


# ---------- 6) FUNCTIONS ----------
# • Define with def name(params): (colon mandatory)
# • Return when you need the value later.
# • Keep all code inside one indentation level.

def add(a, b):
    return a + b

result = add(3, 4)
print("Result:", result)


# ---------- 7) TRY / EXCEPT ----------
# • try must have at least one except.
# • No nested ifs unless required.
# • Keep exception types specific (ZeroDivisionError, ValueError).

try:
    x = int(input("Enter number: "))  # only if exam asks for input
    y = 10 / x
except ZeroDivisionError:
    print("Cannot divide by zero")
except ValueError:
    print("Please enter a valid number")
else:
    print("Result:", y)
finally:
    print("Program finished")

# Example pattern for assignments like average calculator:
data = []
try:
    avg = sum(data) / len(data)
except ZeroDivisionError:
    avg = 0.0
print("Average:", avg)


# ---------- 8) ASSERTIONS ----------
# • Quick validation tool. Use to confirm preconditions.
def sqrt_positive(n):
    assert n >= 0, "n must be non-negative"
    return n ** 0.5


# ---------- 9) CLASS STRUCTURE ----------
# • Always define __init__ correctly.
# • Every method’s first argument must be self.
# • Keep consistent indentation across methods.

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_total(self, quantity):
        return self.price * quantity

item = Product("Pen", 1.5)
print(item.get_total(3))


# ---------- 10) FILE EXECUTION & ORDER ----------
# • Don’t leave stray code at the top.
# • Wrap test code under this guard to avoid auto-execution on import:
if __name__ == "__main__":
    print("Ready for exam testing.")


# ---------- 11) DEBUGGING QUICKLY ----------
# • SyntaxError → check for missing colon or indentation mismatch.
# • IndentationError → highlight, Shift+Tab or Tab correctly.
# • NameError → variable not defined or typo.
# • TypeError → wrong data type (use int(), float(), str() as needed).
# • Use print() for quick inspection, then remove it before submitting.

# Example:
value = "10"
print(type(value))
value = int(value)
print(type(value))


# ---------- 12) LAST-MINUTE SANITY CHECK ----------
# • Run the file once before submitting.
# • Make sure output matches exercise request exactly.
# • No untranslated comments unless asked.
# • No leftover debug prints.
# • Keep code simple: one function, one loop, clear logic.


# !!RELEVANT, BUT NOT FROM CLASS!!
# 13) WHEN STRESSED: THE 5-LINE STRUCTURE TEMPLATE
# ------------------------------------------------
# def main():
#     try:
#         # logic
#     except Exception as e:
#         print("Error:", e)
#     else:
#         print("Success")
#
# if __name__ == "__main__":
#     main()
