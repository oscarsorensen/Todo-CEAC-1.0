# ==========================================
# UNIT 005 — Reading & Writing Information (Deep Study Guide)
# Author: Oscar Sørensen — Study edition (explanations first, then clean, runnable code)
# Style: English learning-style explanations + short exam tip boxes + minimal, clean code blocks
# ==========================================

# ======================================================
# SECTION 0 — FILE BASICS: open(), modes, encodings, and iteration
# ======================================================
"""
BIG PICTURE
-----------
Your computer stores data as files on disk. Python can connect to those files, read data
from them, and write new data to them. The function you use is:
    open(path, mode, encoding)

- path:    file name or path (e.g., "example.txt" or "/Users/oscar/example.txt")
- mode:    what you want to do with the file
           "w"  -> write text (creates/overwrites the file)
           "a"  -> append text (adds at the end; preserves old content)
           "r"  -> read text (error if file does not exist)
           "wb" -> write binary (images, pickle objects, etc.)
           "rb" -> read binary
- encoding: how characters are translated to bytes for text files. Use "utf-8".

WHY 'with open(...) as f:' ?
----------------------------
Files are resources that must be closed after use. If you forget to close them, data might
not be fully saved (because of buffering), or the OS might lock the file. The 'with' block
creates a safe context: when the block ends, Python automatically calls f.close() for you,
even if an error happens inside the block.

WHAT IS f.write()?
------------------
- f is a file object. Think of it as a pen connected to the file.
- f.write(text) sends text from your program into the file on disk.
- It returns the number of characters written (we usually don't use that return value).

WHAT IS '\n'?
-------------
This is the newline character. It means “start a new line” (similar to pressing ENTER).
When you write "Hello\nWorld", the file content becomes:
    Hello
    World
If you forget the newline at the end of a line, the next write will continue on the same line.

HOW DOES READING WORK?
----------------------
When you do:
    for line in f:
Python reads the file line by line. Each 'line' still includes the newline at the end.
That's why we often call .strip() to remove newline and surrounding spaces before printing.

EXAM TIPS
---------
- Always use 'with open(..., mode, encoding="utf-8") as f:' in text tasks.
- Remember modes: 'w' overwrites, 'a' appends, 'r' reads (error if missing).
- Mention that '\\n' is a newline and why we use .strip() when printing lines.
"""

def file_basics_demo():
    # 1) Write (overwrites or creates)
    with open("example.txt", "w", encoding="utf-8") as f:
        f.write("First line\nSecond line")     # '\n' -> new line
    
    # 2) Append (preserves old content, adds to the end)
    with open("example.txt", "a", encoding="utf-8") as f:
        f.write("\nAppended line")
    
    # 3) Read (iterate lines, strip newline for clean output)
    with open("example.txt", "r", encoding="utf-8") as f:
        for line in f:
            print("Line:", line.strip())


# ======================================================
# SECTION 1 — TEXT FILE EXERCISE: a simple contact agenda (write & read)
# ======================================================
"""
GOAL
----
Create a minimal contact agenda that:
  1) Asks the user for a name and an email and saves it to 'agenda.txt'.
  2) Reads all contacts from 'agenda.txt' and prints them nicely.

WHY THIS MATTERS
----------------
- You learn persistence (data survives after the program ends).
- You practice modes 'a' (append) and 'r' (read).
- You practice splitting a line into parts using .split(',').

WHAT HAPPENS UNDER THE HOOD
---------------------------
WRITE:
- We ask for two strings using input().
- We open 'agenda.txt' in append mode ("a") so we never destroy existing contacts.
- We write "name,email\n" so each contact is on its own line.

READ:
- We open 'agenda.txt' in read mode ("r").
- We loop through each line. Each line looks like "Name,Email\n".
- We do line.strip() to remove '\n', then split(',') to separate fields into [name, email].
- We print them in a readable format.

COMMON MISTAKES
---------------
- Forgetting the '\n' -> new contact gets glued to the previous one.
- Using "w" accidentally instead of "a" -> you erase the file.
- Assuming the file exists when reading. Use try/except FileNotFoundError for a friendly message.

EXAM TIPS
---------
- Show that you know how to append without overwriting.
- Explain why you use .split(',') and .strip().
- Mention that you close files using 'with' (automatic).
"""

def agenda_write_contact():
    name = input("Enter contact name: ")
    email = input("Enter contact email: ")
    with open("agenda.txt", "a", encoding="utf-8") as f:
        f.write(name + "," + email + "\n")
    print("Contact saved.")

def agenda_read_all():
    print("\nContacts in the agenda:")
    try:
        with open("agenda.txt", "r", encoding="utf-8") as f:
            for line in f:
                name, email = line.strip().split(",")
                print("Name:", name, "| Email:", email)
    except FileNotFoundError:
        print("No 'agenda.txt' found — add a contact first.")


# ======================================================
# SECTION 2 — JSON to HTML: create a blog.html from blog.json
# ======================================================
"""
GOAL
----
Read a JSON file that contains blog posts and generate a simple HTML page that displays them.

WHAT IS JSON?
-------------
JSON is a text format for structured data: objects (dicts) and arrays (lists). In Python:
- json.load(file)  -> read JSON from a file and convert it to Python objects (dicts/lists).
- json.dump(obj)   -> write Python objects as JSON into a file.

WORKFLOW
--------
1) Read "blog.json" using json.load(). We expect a list of dicts like:
   [
     {"titulo":"...", "fecha":"...", "autor":"...", "contenido":"..."},
     ...
   ]
2) Open "blog.html" for writing.
3) Write an HTML header (doctype, <html>, <head>, styles, start of <main>).
4) For each article dict in the list, write an <article> block that includes its data.
5) Close the HTML structure.

WHY THIS MATTERS
----------------
- You learn to transform structured data (JSON) into a presentable format (HTML).
- You see how back-end code (Python) can produce front-end output (HTML page).

EXAM TIPS
---------
- Use the exact variable names if the statement requires them (archivo_json, archivo_html, contenido_blog).
- Explain that json.load() turns text JSON into Python data structures you can iterate over.
- Keep HTML writing clean and minimal. Close the tags.
"""
import json

def blog_json_to_html():
    archivo_json = "blog.json"
    archivo_html = "blog.html"
    contenido_blog = []

    # Read JSON into Python
    with open(archivo_json, "r", encoding="utf-8") as f:
        contenido_blog = json.load(f)

    # Build minimal HTML
    head = """<!doctype html>
<html lang="es">
  <head>
    <title>JOCARSAblog</title>
    <meta charset="utf-8">
    <style>
      body{background:steelblue;color:steelblue;font-family:sans-serif;}
      main{background:white;color:black;padding:20px;width:800px;margin:40px auto;border-radius:6px;}
      article{border-bottom:1px solid #ddd;padding:10px 0;margin:10px 0;}
      h2{margin:0 0 6px 0;}
      .meta{font-size:12px;color:#555;}
    </style>
  </head>
  <body>
    <header><h1 style="text-align:center;color:white;">JOCARSAblog</h1></header>
    <main>
"""
    tail = """    </main>
    <footer style="text-align:center;color:white;">(c)2025 Jose Vicente Carratalá</footer>
  </body>
</html>
"""

    # Write HTML file
    with open(archivo_html, "w", encoding="utf-8") as f:
        f.write(head)
        for art in contenido_blog:
            titulo = art.get("titulo", "(Sin título)")
            fecha  = art.get("fecha", "")
            autor  = art.get("autor", "")
            cont   = art.get("contenido", "")
            block = f"""      <article>
        <h2>{titulo}</h2>
        <div class="meta">{fecha} — {autor}</div>
        <p>{cont}</p>
      </article>
"""
            f.write(block)
        f.write(tail)
    print("Generated blog.html from blog.json")


# ======================================================
# SECTION 3 — “Antonio” case: write/append, read last line, and pickle an object
# ======================================================
"""
GOAL
----
- Write "Food cooked: Pizza" into 'foods.txt' (overwrite, then append "Hamburger").
- Read the last line from 'foods.txt'.
- Save and load an object using pickle (binary serialization).

WHAT IS PICKLE?
---------------
Pickle converts Python objects into a stream of bytes so you can save them to a file
and load them later. It preserves Python-specific structures (classes, lists, dicts, etc.).

- pickle.dump(obj, file) -> save object to an open file in 'wb' mode.
- pickle.load(file)      -> read object from an open file in 'rb' mode.

IMPORTANT
---------
Pickle is Python-specific. You cannot easily read a pickle file from other languages.
Use JSON for cross-language interchange, and pickle when you want to preserve exact Python objects.

EXAM TIPS
---------
- Remember: text files use "w"/"a"/"r" with encoding; pickle uses "wb"/"rb".
- Demonstrate that you can show the last line by reading all lines and taking the last element.
"""
import pickle

def foods_write_and_append():
    with open("foods.txt", "w", encoding="utf-8") as f:
        f.write("Food cooked: Pizza\n")
    with open("foods.txt", "a", encoding="utf-8") as f:
        f.write("Food cooked: Hamburger\n")
    print("Written and appended to 'foods.txt'.")

def foods_read_last_line():
    try:
        with open("foods.txt", "r", encoding="utf-8") as f:
            lines = f.readlines()                 # returns a list of lines
            if lines:
                print("Last line:", lines[-1].strip())
            else:
                print("File is empty.")
    except FileNotFoundError:
        print("No 'foods.txt' found — run foods_write_and_append() first.")

class Training:
    def __init__(self, date, exercise, sets, reps):
        self.date = date
        self.exercise = exercise
        self.sets = sets
        self.reps = reps

    def __repr__(self):
        return f"Training({self.date!r}, {self.exercise!r}, {self.sets!r}, {self.reps!r})"

def pickle_save_and_load_demo():
    obj = Training("2025-10-20", "Bench press", 4, 10)
    with open("training.bin", "wb") as f:
        pickle.dump(obj, f)          # serialize to bytes and write
    with open("training.bin", "rb") as f:
        loaded = pickle.load(f)      # read bytes and reconstruct object
    print("Loaded object:", loaded)


# ======================================================
# SECTION 4 — Filesystem operations: folder size and files larger than 1 GB
# ======================================================
"""
GOAL
----
- Ask for a folder path and calculate the total size of files in that folder (non-recursive).
- Walk the folder recursively and print files larger than 1 GB.

KEY FUNCTIONS
-------------
- os.listdir(path) -> list of names in a directory (files and subfolders, not recursive).
- os.path.join(a,b) -> safely join folder and name into a full path.
- os.path.getsize(path) -> file size in bytes.
- os.walk(top) -> recursively yields (dirpath, dirnames, filenames) for all subfolders.

WHY BYTES → MB/GB?
------------------
File size is in bytes. We convert to MB/GB by dividing:
- MB  = bytes / (1024 * 1024)
- GB  = bytes / (1024 * 1024 * 1024)

ERRORS
------
- If you try to get the size of a path that is not a file (like a folder), you may get errors.
- Wrap size calls in try/except OSError to skip unreadable files.

EXAM TIPS
---------
- Show both non-recursive (os.listdir) and recursive (os.walk) patterns.
- Use try/except around size calls to be robust.
"""
import os

def folder_size_megabytes():
    folder = input("Enter a folder path: ")
    try:
        names = os.listdir(folder)       # items in the folder (1 level)
    except FileNotFoundError:
        print("Folder not found.")
        return

    total = 0
    for name in names:
        path = os.path.join(folder, name)
        if os.path.isfile(path):
            try:
                total += os.path.getsize(path)
            except OSError:
                pass

    print("Total size:", total/(1024*1024), "MB")

def list_files_over_1gb():
    folder = input("Enter a folder path: ")
    one_gb = 1024 * 1024 * 1024
    for dirpath, dirnames, filenames in os.walk(folder):
        for filename in filenames:
            path = os.path.join(dirpath, filename)
            try:
                if os.path.getsize(path) > one_gb:
                    print(path, os.path.getsize(path)/(1024*1024), "MB")
            except OSError:
                pass


# ======================================================
# SECTION 5 — Create, delete, and ZIP files
# ======================================================
"""
GOAL
----
- Create a file and write some text.
- Delete a file using os.remove().
- Compress a file into a .zip using the zipfile module.

WHY ZIP?
--------
ZIP is a very common archive format. You collect files together and compress them, which is
useful for sharing or backups.

KEY FUNCTIONS
-------------
- open(..., "w") to create and write.
- os.remove(path) to delete.
- zipfile.ZipFile("dest.zip", "w") to create a new zip and .write("source").

EXAM TIPS
---------
- Explain the difference between creating/writing and removing.
- Show that you can pick a source file and add it to a zip archive.
"""
import zipfile

def create_and_delete_demo():
    with open("myfile.txt", "w", encoding="utf-8") as f:
        f.write("Sample text\nAnother line")
    print("Created: myfile.txt")

    os.remove("myfile.txt")
    print("Deleted: myfile.txt")

def zip_one_file(source, dest_zip):
    with zipfile.ZipFile(dest_zip, mode="w") as zf:
        zf.write(source, arcname=os.path.basename(source))
    print(f"Compressed '{source}' into '{dest_zip}'.")


# ======================================================
# SECTION 6 — Full console CRUD with pickle persistence (plus UPPER/lower options)
# ======================================================
"""
GOAL
----
Build a menu-driven console program to manage a list of clients using a simple class and
a Python list. Save the list to a file with pickle so it persists between runs.

REQUIREMENTS WE FOLLOW
----------------------
- Class only with properties (+ methods to change case).
- List of clients.
- Menu: insert, list, update, delete, change to UPPERCASE, change to lowercase, exit.
- Use .pop() to delete by index (restriction in your statement).
- Save (pickle) after every insert/update/delete or case-change.

HOW TO THINK ABOUT IT
---------------------
- 'clientes.bin' is your "database" file for this exercise.
- On start: try to load it; if it doesn't exist, start with an empty list.
- Each option is a function. The loop calls the correct function based on user input.

EXAM TIPS
---------
- Welcome message at the start.
- Use while True + if/elif for the menu.
- Use try/except for invalid IDs.
- Respect the "use pop()" rule for deletion.
"""
PICKLE_FILE = "clients.bin"

class Client:
    def __init__(self, name, surname, email):
        self.name = name
        self.surname = surname
        self.email = email

    def to_upper(self):
        self.name = self.name.upper()
        self.surname = self.surname.upper()

    def to_lower(self):
        self.name = self.name.lower()
        self.surname = self.surname.lower()

    def __repr__(self):
        return f"Client({self.name!r}, {self.surname!r}, {self.email!r})"

def load_clients():
    try:
        with open(PICKLE_FILE, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return []
    except Exception:
        return []

def save_clients(clients):
    with open(PICKLE_FILE, "wb") as f:
        pickle.dump(clients, f)

def insert_client(clients):
    name = input("Enter name: ")
    surname = input("Enter surname: ")
    email = input("Enter email: ")
    clients.append(Client(name, surname, email))
    save_clients(clients)
    print("Client inserted.")

def list_clients(clients):
    for idx, c in enumerate(clients):
        print(f"ID {idx} -> {c.name} {c.surname} {c.email}")

def update_client(clients):
    try:
        idx = int(input("ID to update: "))
        c = clients[idx]
        new_name = input(f"New name ({c.name}): ")
        new_surname = input(f"New surname ({c.surname}): ")
        new_email = input(f"New email ({c.email}): ")
        c.name = new_name or c.name
        c.surname = new_surname or c.surname
        c.email = new_email or c.email
        save_clients(clients)
        print("Client updated.")
    except (ValueError, IndexError):
        print("Invalid ID.")

def delete_client(clients):
    try:
        idx = int(input("ID to delete: "))
        confirm = input("Confirm deletion? (y/n): ")
        if confirm.lower() == "y":
            clients.pop(idx)   # <- required by your statement
            save_clients(clients)
            print("Client deleted.")
        else:
            print("Cancelled.")
    except (ValueError, IndexError):
        print("Invalid ID.")

def all_upper(clients):
    for c in clients:
        c.to_upper()
    save_clients(clients)
    print("All names set to UPPERCASE.")

def all_lower(clients):
    for c in clients:
        c.to_lower()
    save_clients(clients)
    print("All names set to lowercase.")

def clients_menu():
    print("###### Client manager v0.1 ######")
    print("####### Jose Vicente Carratala #######")
    clients = load_clients()

    while True:
        print("\nChoose an option:")
        print("1.-Insert client")
        print("2.-List clients")
        print("3.-Update client")
        print("4.-Delete client")
        print("5.-To UPPERCASE")
        print("6.-To lowercase")
        print("7.-Exit")
        op = input("> ")

        if op == "1":
            insert_client(clients)
        elif op == "2":
            list_clients(clients)
        elif op == "3":
            update_client(clients)
        elif op == "4":
            delete_client(clients)
        elif op == "5":
            all_upper(clients)
        elif op == "6":
            all_lower(clients)
        elif op == "7":
            print("Program finished.")
            break
        else:
            print("Invalid option.")


# ======================================================
# SECTION 7 — Tkinter mini-GUI: sum two numbers and show result
# ======================================================
"""
GOAL
----
Build a tiny window with two input fields, a button, and a label that shows the sum.

HOW TKINTER WORKS
-----------------
- tk.Tk() creates the main window (the application root).
- Widgets like Entry (text inputs), Button, and Label are created and placed in the window.
- The 'command=' of a Button points to a function that runs when clicked.
- .get() reads the current text in an Entry.
- You update the label with .config(text=...).
- .mainloop() starts the event loop so the window responds to clicks and typing.

EXAM TIPS
---------
- Keep it simple: two Entry, one Button, one Label.
- Convert input strings to float (or int) and handle ValueError.
"""
def tkinter_sum_demo():
    try:
        import tkinter as tk
    except ImportError:
        print("tkinter not available in this environment.")
        return

    def calculate():
        try:
            a = float(entry1.get() or "0")
            b = float(entry2.get() or "0")
            result.config(text=f"Total: {a + b}")
        except ValueError:
            result.config(text="Please enter valid numbers.")

    root = tk.Tk()
    root.title("Quick Sum")

    entry1 = tk.Entry(root)
    entry2 = tk.Entry(root)
    button = tk.Button(root, text="Calculate", command=calculate)
    result = tk.Label(root, text="Total: 0")

    entry1.pack(padx=10, pady=5)
    entry2.pack(padx=10, pady=5)
    button.pack(padx=10, pady=5)
    result.pack(padx=10, pady=5)

    root.mainloop()


# ======================================================
# SECTION 8 — Tkinter + MySQL (insert rows with a button) — template
# ======================================================
"""
GOAL
----
Create a GUI form that inserts a row into a MySQL table when you click a button.

WHAT YOU NEED BEFORE RUNNING
----------------------------
- MySQL server running locally or accessible.
- A database and a table created (e.g., amigos_gimnasio(name, surname, date)).
- The package 'mysql-connector-python' installed.

LOGIC
-----
- Collect text from Entry widgets.
- Open a DB connection with mysql.connector.connect(...).
- Execute an INSERT with placeholders (%s, %s, %s).
- Commit and close the connection.
- Show a "success" message in a Label.

EXAM TIPS
---------
- Keep credentials outside code in real projects (env vars). For the exam, placeholders are fine.
- Always commit after INSERT/UPDATE/DELETE.
- Show a short success/failure message.
"""
def tkinter_mysql_insert_template():
    try:
        import tkinter as tk
        import mysql.connector
    except ImportError:
        print("tkinter or mysql.connector not available here.")
        return

    def register():
        name = ent_name.get()
        surname = ent_surname.get()
        date = ent_date.get()
        try:
            con = mysql.connector.connect(
                host="localhost", user="useroscar", password="your_password", database="YourDB"
            )
            cur = con.cursor()
            cur.execute(
                "INSERT INTO amigos_gimnasio (nombre, apellidos, fecha) VALUES (%s,%s,%s)",
                (name, surname, date)
            )
            con.commit()
            cur.close(); con.close()
            msg.config(text="Inserted OK.")
        except mysql.connector.Error as e:
            msg.config(text=f"MySQL error: {e}")

    root = tk.Tk(); root.title("MySQL Insert")
    tk.Label(root, text="Name").grid(row=0, column=0, sticky="e")
    tk.Label(root, text="Surname").grid(row=1, column=0, sticky="e")
    tk.Label(root, text="Date (YYYY-MM-DD)").grid(row=2, column=0, sticky="e")

    ent_name = tk.Entry(root); ent_name.grid(row=0, column=1)
    ent_surname = tk.Entry(root); ent_surname.grid(row=1, column=1)
    ent_date = tk.Entry(root); ent_date.grid(row=2, column=1)

    tk.Button(root, text="Register", command=register).grid(row=3, column=0, columnspan=2, pady=8)
    msg = tk.Label(root, text=""); msg.grid(row=4, column=0, columnspan=2)
    root.mainloop()


# ======================================================
# SECTION 9 — Exam sketch: Console CRUD + Database (MySQL)
# ======================================================
"""
GOAL
----
Produce a small console menu that performs CRUD operations against a MySQL database for
a portfolio schema (Categoria and Pieza with a foreign key).

WHY A SKETCH?
-------------
In the exam, you will likely define your schema in SQL, then write a short Python program
to connect and run queries. Below is a clear skeleton: connection function, simple INSERT
and SELECT, and a minimal menu loop.

EXAM TIPS
---------
- Show a LEFT JOIN and a VIEW when asked in the DB part; in Python, focus on a clean menu.
- Check errors with try/except mysql.connector.Error and print friendly messages.
"""
EXAM_CRUD_SKETCH = r"""
import mysql.connector

def connect():
    return mysql.connector.connect(
        host="localhost",
        user="useroscar",
        password="your_password",
        database="PortafolioDB"
    )

def insert_category(title, desc):
    cn = connect(); cur = cn.cursor()
    cur.execute("INSERT INTO Categoria(titulo, descripcion) VALUES (%s,%s)", (title, desc))
    cn.commit(); cur.close(); cn.close()

def list_categories():
    cn = connect(); cur = cn.cursor()
    cur.execute("SELECT id, titulo, descripcion FROM Categoria")
    for row in cur.fetchall():
        print(row)
    cur.close(); cn.close()

def menu():
    while True:
        print("1) Insert category  2) List categories  3) Exit")
        op = input("> ")
        if op == "1":
            t = input("Title: "); d = input("Description: ")
            insert_category(t, d)
        elif op == "2":
            list_categories()
        elif op == "3":
            print("Bye"); break
        else:
            print("Invalid option")
"""


# ======================================================
# SECTION 10 — Error handling & practical exam reminders
# ======================================================
"""
WHY EXCEPTIONS?
---------------
Reading/writing files and connecting to databases can fail (missing files, permission
errors, network issues, etc.). Use try/except to handle errors gracefully and keep the
program alive or show a helpful message.

COMMON PATTERNS
---------------
- FileNotFoundError when opening non-existing files in 'r' mode.
- OSError when reading sizes from locked or special files.
- mysql.connector.Error for DB issues (wrong credentials, missing table).

EXAM TIPS
---------
- Wrap file reads in try/except FileNotFoundError (print a friendly message).
- For menus, validate user input and catch ValueError when converting to int.
- Mention persistence (pickle/text/JSON) and explain your choice quickly.
"""

def open_or_create_demo():
    try:
        with open("maybe.txt", "r", encoding="utf-8") as f:
            print(f.read())
    except FileNotFoundError:
        print("File not found -> creating a new one.")
        with open("maybe.txt", "w", encoding="utf-8") as f:
            f.write("Created automatically.")


# ======================================================
# __main__ — Uncomment what you want to test locally
# ======================================================
if __name__ == "__main__":
    pass
# --- Agenda ---
# agenda_escribir_contacto()
# agenda_leer_contactos()

# SECTION 0
# file_basics_demo()

# SECTION 1
# agenda_write_contact()
# agenda_read_all()

# SECTION 2
# blog_json_to_html()

# SECTION 3
# foods_write_and_append()
# foods_read_last_line()
# pickle_save_and_load_demo()

# SECTION 4
# folder_size_megabytes()
# list_files_over_1gb()

# SECTION 5
# create_and_delete_demo()
# zip_one_file("example.txt", "example.zip")  # ensure example.txt exists first

# SECTION 6
# clients_menu()

# SECTION 7
# tkinter_sum_demo()

# SECTION 8
# tkinter_mysql_insert_template()

# SECTION 9
# print(EXAM_CRUD_SKETCH)

# SECTION 10
# open_or_create_demo()
