# ==========================================
# UNITS 004–005 — File System, Persistence, and Interfaces
# Keywords: (filesystem, os, open, read, write, pickle, json, compression, tkinter, events, mysql)
# ==========================================

# ---------- 1) FILE SYSTEM OPERATIONS ----------
# Python can explore and manipulate the filesystem using the os module.

import os
print(os.listdir('.'))          # List files in current folder
print(os.getcwd())              # Show current working directory
print(os.path.getsize('file'))  # Get file size (bytes)
print(os.path.abspath('file'))  # Get absolute path

# Recursive directory walk
for root, dirs, files in os.walk('.'):
    for name in files:
        print(os.path.join(root, name))

# ---------- 2) FILE ATTRIBUTES ----------
# You can check existence, type, and permissions.

print(os.path.exists('file.txt'))
print(os.path.isfile('file.txt'))
print(os.path.isdir('folder'))

# ---------- 3) TEXT FILES ----------
# open(filename, mode, encoding)
# Modes: 'r' (read), 'w' (write, overwrite), 'a' (append)

with open('example.txt', 'w', encoding='utf-8') as f:
    f.write('First line\nSecond line')

with open('example.txt', 'a', encoding='utf-8') as f:
    f.write('\nAppended line')

with open('example.txt', 'r', encoding='utf-8') as f:
    for line in f:
        print('Line:', line.strip())

# ---------- 4) JSON FILES ----------
import json
data = {'name': 'Oscar', 'year': 2025}
with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

with open('data.json', 'r', encoding='utf-8') as f:
    result = json.load(f)
print('JSON loaded:', result)

# ---------- 5) PICKLE (BINARY PERSISTENCE) ----------
import pickle

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def __repr__(self):
        return f'Product({self.name!r}, {self.price!r})'

products = [Product('Shaker', 9.99), Product('Bottle', 5.5)]

# Save binary
with open('products.bin', 'wb') as f:
    pickle.dump(products, f)

# Load binary
with open('products.bin', 'rb') as f:
    loaded = pickle.load(f)
print('Loaded from binary:', loaded)

# ---------- 6) FILE CREATION / DELETION / COMPRESSION ----------
# Create folder and files
os.mkdir('myfolder')
with open('myfolder/test.txt', 'w') as f:
    f.write('test')

# Delete file or folder
os.remove('myfolder/test.txt')
os.rmdir('myfolder')

# Compress files
import zipfile
with zipfile.ZipFile('archive.zip', 'w') as z:
    z.write('example.txt')

# ---------- 7) ERROR HANDLING ----------
try:
    with open('maybe.txt', 'r', encoding='utf-8') as f:
        print(f.read())
except FileNotFoundError:
    print('File not found -> creating new one.')
    with open('maybe.txt', 'w', encoding='utf-8') as f:
        f.write('Created automatically.')

# ---------- 8) STATIC METHODS ----------
class Entrenamiento:
    @staticmethod
    def calcular_puntuacion(series, repeticiones):
        return series * repeticiones

print('Training score:', Entrenamiento.calcular_puntuacion(4, 10))

# ---------- 9) SIMPLE CRUD MENU ----------
def insert_client():
    print('Insert client placeholder')

def list_clients():
    print('List clients placeholder')

while True:
    print('\n1) Insert client  2) List clients  3) Exit')
    option = input('> ')
    if option == '1':
        insert_client()
    elif option == '2':
        list_clients()
    elif option == '3':
        break
    else:
        print('Invalid option.')

# ---------- 10) TKINTER (GRAPHICAL INTERFACES) ----------
from tkinter import *

root = Tk()
root.title('My App')
Label(root, text='Name:').pack()
Entry(root).pack()
Button(root, text='Save').pack()
root.mainloop()

# ---------- 11) EVENTS ----------
# Events are actions triggered by the user (clicks, keys).
# Example of binding an event to a button click.

def on_click():
    print('Button clicked!')

root = Tk()
btn = Button(root, text='Click Me')
btn.pack()
btn.bind('<Button-1>', lambda e: on_click())
root.mainloop()

# ---------- 12) MYSQL CONNECTION (optional) ----------
# Simple connection example (requires mysql-connector-python).

import mysql.connector
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='password',
    database='examdb'
)
cursor = conn.cursor()
cursor.execute('SHOW TABLES;')
for row in cursor:
    print(row)
conn.close()

# ---------- 13) KEY CONCEPTS SUMMARY ----------
# open() modes: r, w, a, rb, wb
# pickle: save/load Python objects in binary
# json: structured text format (compatible with other languages)
# os: list, remove, create, navigate files/folders
# tkinter: build graphical interfaces
# events: user interactions like clicks or keys
# mysql.connector: connect to MySQL databases
# try/except: handle errors gracefully
