# ==========================================
# UNIT 2 — Working with Objects
# Topics: everything is an object, attributes & methods, instances,
# calling methods with parameters, properties (attributes),
# static methods, simple constructors, basic resource handling.
# ==========================================

# ---------- 1) EVERYTHING IS AN OBJECT ----------
text = "Python DAW"
print(text.upper())   # method (belongs to the string object)
print(len(text))      # built-in function operating on the object

nums = [3, 1, 2]
nums.append(4)        # list method
print(sorted(nums))   # built-in that returns a new sorted list
print(nums)           # original list has [3,1,2,4]

# ---------- 1.2)FUNCTION OR METHOD ----------

# Functions
print(len("Hi"))             # 2
print(sorted([3, 1, 2]))     # [1, 2, 3]
print(sum([1, 2, 3]))        # 6

# Methods
print("hi".upper())          # "HI"
numbers = [3, 1, 2]
numbers.append(4)
print(numbers)               # [3, 1, 2, 4]


# ---------- 2) INSTANCES & NAMESPACES ----------
class Cat:
    pass

my_cat = Cat()        # instance
other_cat = Cat()

# Each instance can carry its own attributes (dynamic in Python)
my_cat.name = "Mishi"
other_cat.name = "Luna"
print(my_cat.name, other_cat.name)   # different namespaces


# ---------- 3) METHODS & PARAMETERS ----------
class Calculator:
    def add(self, a, b):
        return a + b

calc = Calculator()
print("add:", calc.add(3, 4))


# ---------- 4) PROPERTIES (ATTRIBUTES) ----------
class Customer:
    def __init__(self, name, age):
        self.name = name   # public attribute
        self.age = age

c = Customer("Oscar", 25)
print(f"Customer: {c.name}, age {c.age}")


# ---------- 5) STATIC METHODS ----------
# Static methods don’t use 'self' or object state.

class MathTools:
    @staticmethod
    def double(n):
        return n * 2

print(MathTools.double(5))
mt = MathTools()
print(mt.double(7))  # technically allowed, but prefer calling via class


# ---------- 6) CONSTRUCTORS (BASICS) ----------
from datetime import datetime, date

today = date.today()
now = datetime.now()
print("Today:", today.isoformat(), "Now:", now.strftime("%Y-%m-%d %H:%M:%S"))

class Order:
    def __init__(self, customer, total, created_at=None):
        self.customer = customer
        self.total = float(total)
        self.created_at = created_at or datetime.now()

order = Order("Oscar", 99.9)
print("Order:", order.customer, order.total, order.created_at)


# ---------- 7) RESOURCE MANAGEMENT ----------
# Use 'with' to ensure resources are released automatically.
with open("unit2_output.txt", "w") as f:
    f.write("Resource released automatically when leaving 'with' block.\n")


# !!RELEVANT, BUT NOT FROM CLASS!!
# ---------- 8) classmethod vs staticmethod ----------
class Example:
    factor = 10

    @classmethod
    def from_factor(cls, n):
        # Uses the class (cls). Often used for alternate constructors.
        return n * cls.factor

    @staticmethod
    def triple(n):
        return 3 * n

print("from_factor:", Example.from_factor(2))  # 20
print("triple:", Example.triple(3))            # 9
