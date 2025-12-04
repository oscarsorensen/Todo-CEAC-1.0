# ==========================================
# UNIT 3 — Control Structures
# Topics: if/elif/else, loops (for/while), break/continue/pass,
# exceptions (try/except/else/finally), assertions, small refactors.
# ==========================================

# ---------- 1) SELECTION (if / elif / else) ----------
x = 10
if x > 10:
    msg = "Greater than 10"
elif x == 10:
    msg = "Equal to 10"
else:
    msg = "Less than 10"
print("selection:", msg)

age = 20
has_license = True
if age >= 18 and has_license:
    print("Can drive")


# ---------- 2) LOOPS ----------
# for with range
for i in range(3):  # 0, 1, 2
    print("for i:", i)

# while
counter = 0
while counter < 3:
    print("while counter:", counter)
    counter += 1

# Accumulator pattern
numbers = [1, 2, 3, 4, 5]
total = 0
for n in numbers:
    total += n
print("sum:", total)

# Looping over lists directly
words = ["alpha", "beta", "gamma"]
for w in words:
    print("word:", w)


# ---------- 3) JUMP STATEMENTS ----------
for n in range(1, 8):
    if n == 3:
        continue   # skip this iteration
    if n == 6:
        break      # exit the loop
    if n == 2:
        pass       # placeholder (does nothing)
    print("n:", n)


# ---------- 4) EXCEPTIONS ----------
# try: attempt risky code
# except: handle specific failure gracefully
# else: runs only if no exception
# finally: runs always (cleanup)

def safe_divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError as e:
        print("Error: division by zero", e)
        return None
    except TypeError as e:
        print("Type error:", e)
        return None
    else:
        return result
    finally:
        # e.g., close resources if needed
        pass

print("safe_divide 10/2:", safe_divide(10, 2))
print("safe_divide 1/0:", safe_divide(1, 0))

# Pattern from your average exercise:
gym_days = []  # try [] and [1,3,4,0,2]
try:
    avg_days = sum(gym_days) / len(gym_days)
except ZeroDivisionError:
    avg_days = 0.0  # numeric fallback (keeps type numeric)
print("avg_days:", avg_days)

# Explanation (very important to remember):
# 1) Python tries the 'try' block.
# 2) If an error happens (e.g., division by zero), it jumps to the matching 'except'.
# 3) The 'except' block runs (assign 0.0) and the program continues normally.


# ---------- 5) ASSERTIONS ----------
# Assert states assumptions. If false, raises AssertionError.
def sqrt_non_negative(x):
    assert x >= 0, "x must be non-negative"
    return x ** 0.5

print("sqrt_non_negative(9):", sqrt_non_negative(9))
# sqrt_non_negative(-1)  # uncomment to see AssertionError


# ---------- 6) SMALL REFACTOR + DOCSTRINGS ----------
def documented_divide(dividend, divisor):
    """
    Return the quotient dividend/divisor as float.
    Converts inputs to int first; may raise ZeroDivisionError.
    """
    dividend = int(dividend)
    divisor = int(divisor)
    return dividend / divisor

try:
    print("documented_divide:", documented_divide("10", "2"))
except ZeroDivisionError:
    print("Division by zero")

# !!RELEVANT, BUT NOT FROM CLASS!!
# List comprehensions and any/all — high-signal shortcuts
evens = [n for n in range(10) if n % 2 == 0]
print("evens:", evens)
print("any > 5:", any(n > 5 for n in evens))
print("all even:", all(n % 2 == 0 for n in evens))
