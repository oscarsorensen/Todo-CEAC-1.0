# ==========================================
# UNIT 4 — Building Classes (OOP Basics)
# Topics: defining classes, instance attributes & methods,
# visibility conventions, properties (@property), getters/setters,
# constructors (__init__), simple CRUD patterns, inheritance (basics).
# ==========================================

# ---------- 1) DEFINING A CLASS ----------
class Cat:
    def __init__(self, name):
        self.name = name  # instance attribute

    def meow(self):
        return f"{self.name} says meow"

mishi = Cat("Mishi")
print(mishi.meow())


# ---------- 2) VISIBILITY CONVENTIONS ----------
# Python doesn't enforce private; use naming conventions:
# _name  -> "protected" by convention (don’t touch from outside)
# __name -> name-mangled (avoids accidental collisions)

class BankAccount:
    def __init__(self, holder, balance=0.0):
        self.holder = holder
        self._balance = float(balance)

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount

    def balance(self):
        return self._balance

acct = BankAccount("Oscar", 100)
acct.deposit(50)
acct.withdraw(25)
print("Balance:", acct.balance())


# ---------- 3) PROPERTIES (@property) ----------
# Idiomatic Python accessors (instead of manual get_/set_ methods)

class Customer:
    def __init__(self, name, phones=None):
        self._name = name
        self._phones = list(phones or [])

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if isinstance(new_name, str) and new_name:
            self._name = new_name

    @property
    def phones(self):
        return self._phones

    def add_phone(self, p):
        if isinstance(p, str) and p:
            self._phones.append(p)

cli = Customer("Oscar")
cli.add_phone("600123123")
print(cli.name, cli.phones)


# ---------- 4) METHODS (getters/setters style) ----------
class Product:
    def __init__(self, name, price):
        self._name = name
        self._price = float(price)

    def get_name(self):
        return self._name

    def set_name(self, name):
        if name:
            self._name = name

    def get_price(self):
        return self._price

    def set_price(self, price):
        if price >= 0:
            self._price = float(price)

p = Product("Coffee", 2.5)
p.set_price(2.8)
print(p.get_name(), p.get_price())


# ---------- 5) CONSTRUCTORS (__init__) ----------
class Order:
    def __init__(self, order_id, customer, items=None):
        self.order_id = order_id
        self.customer = customer
        self.items = list(items or [])

    def add_item(self, name, price):
        self.items.append((name, float(price)))

    def total(self):
        return sum(price for _, price in self.items)

order = Order(1, "Oscar")
order.add_item("Apple", 1.2)
order.add_item("Bread", 0.8)
print("Order total:", order.total())


# ---------- 6) SIMPLE IN-MEMORY CRUD ----------
class CustomerManager:
    def __init__(self):
        self._customers = []

    def insert(self, customer: Customer):
        self._customers.append(customer)

    def list_all(self):
        for c in self._customers:
            print("-", c.name, c.phones)

mgr = CustomerManager()
mgr.insert(Customer("Ana", ["600111222"]))
mgr.insert(Customer("Luis"))
mgr.list_all()


# ---------- 7) INHERITANCE (BASICS) ----------
class Animal:
    def __init__(self, name):
        self.name = name
    def sound(self):
        return "..."

class Dog(Animal):
    def sound(self):
        return "woof"

dog = Dog("Toby")
print(dog.name, dog.sound())


# !!RELEVANT, BUT NOT FROM CLASS!!
# ---------- 8) dataclasses (less boilerplate for data containers) ----------
from dataclasses import dataclass, field

@dataclass
class Article:
    name: str
    price: float
    tags: list[str] = field(default_factory=list)

a = Article("Notebook", 3.5)
a.tags.append("stationery")
print(a)
