# ==========================================
# UNIT 1 — Program Basics (Python)
# Topics: blocks & indentation, variables, data types, literals,
# constants (by convention), operators, printing, comments.
# ==========================================

# ---------- 1) BLOCKS & INDENTATION ----------
# Python uses indentation (spaces) to mark code blocks.
# Use 4 spaces per indentation level. Never mix tabs and spaces.

def show_blocks():
    for i in range(3):
        print("Loop index:", i)  # inside the loop block
    # out here -> outside the loop
show_blocks()


# ---------- 2) VARIABLES ----------
# Python creates a variable the moment you assign a value.
# No explicit type declaration required.

greeting = "Hello, World"
age = 25            # int
height = 1.82       # float
is_active = True    # bool

# Reassigning
age = age + 5       # 30
age += 2            # 32
print("age:", age)

# Naming convention: snake_case (lowercase_with_underscores)
user_name = "oscar_sorensen"


# ---------- 3) DATA TYPES ----------
n_int = 7                     # int - int is short for integer (whole number)
n_float = 2.5                 # float
text = "text"                 # str
flag = False                  # bool
items = [1, 2, 3]             # list (mutable sequence)
point = (10, 20)              # tuple (immutable sequence)
prefs = {"theme": "dark"}     # dict (key/value map)
print(type(items), type(prefs))

# Conversions
n_from_str = int("10")        # 10
f_from_str = float("2.5")     # 2.5
s_from_num = str(123)         # "123"
b_from_num = bool(0)          # False (0 -> False; nonzero -> True)


# ---------- 4) LITERALS ----------
answer = 42            # int literal
pi = 3.14159           # float literal
truth = True           # boolean literal
hello = "Hello"        # string literal
multiline = """This is
a multi-line string."""
print(hello, pi, truth)
print(multiline)


# ---------- 5) CONSTANTS (BY CONVENTION) ----------
# Python doesn’t enforce constants; use UPPER_CASE names by convention.
TAX_RATE = 0.21
base_price = 100
total_price = base_price * (1 + TAX_RATE)
print("Total with tax:", total_price)


# ---------- 6) OPERATORS ----------
a, b = 7, 3
# Arithmetic
print(a + b, a - b, a * b, a / b)  # 10 4 21 2.333...
print(a // b)   # floor division -> 2
print(a % b)    # modulus -> 1
print(a ** b)   # exponentiation -> 343

# Comparison -> Boolean
print(a == b, a != b, a > b, a >= b, a < b, a <= b)

# Logical
x, y = True, False
print(x and y, x or y, not x)  # False True False

# Membership
fruits = ["apple", "pear"]
print("apple" in fruits)       # True
print("orange" not in fruits)  # True

# Operator precedence basics: ** > * / // % > + - > comparisons > and > or.
# Use parentheses to make intent explicit in exams.


# ---------- 7) PRINT & COMMENTS ----------
print("Simple output with print()")
# One-line comment
"""
Multi-line comment/docstring-style block.
"""


# ---------- 8) MINI PRACTICE ----------
# Small VAT calculator with formatting
amount = 250
result = amount * (1 + TAX_RATE)
print(f"Amount {amount} -> Total {result:.2f}")

# String formatting examples
name = "Oscar"
print(f"Hello, {name}. Int: {n_int}, Float: {n_float:.2f}")

# !!RELEVANT, BUT NOT FROM CLASS!!
# Quick assert-of-assumptions (unit tests will cover this later)
assert isinstance(result, float)
