import sqlite3

def create_table():
    conn = sqlite3.connect('customers.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS clientes
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  nombre TEXT NOT NULL,
                  email TEXT NOT NULL,
                  telefono TEXT NOT NULL)''')
    conn.commit()
    conn.close()

def add_customer(nombre, email, telefono):
    conn = sqlite3.connect('customers.db')
    c = conn.cursor()
    c.execute("INSERT INTO clientes (nombre, email, telefono) VALUES (?, ?, ?)", (nombre, email, telefono))
    conn.commit()
    conn.close()

def list_customers():
    conn = sqlite3.connect('customers.db')
    c = conn.cursor()
    c.execute("SELECT * FROM clientes")
    rows = c.fetchall()
    for row in rows:
        print(row)
    conn.close()

def update_customer(id, nombre, email, telefono):
    conn = sqlite3.connect('customers.db')
    c = conn.cursor()
    c.execute("UPDATE clientes SET nombre = ?, email = ?, telefono = ? WHERE id = ?", (nombre, email, telefono, id))
    conn.commit()
    conn.close()

def delete_customer(id):
    conn = sqlite3.connect('customers.db')
    c = conn.cursor()
    c.execute("DELETE FROM clientes WHERE id = ?", (id,))
    conn.commit()
    conn.close()

def main():
    create_table()
    while True:
        try:
            action = input("Elija una acción (crear, listar, actualizar, borrar, salir): ").strip().lower()
            if action == 'crear':
                nombre = input("Nombre: ").strip()
                email = input("Email: ").strip()
                telefono = input("Teléfono: ").strip()
                add_customer(nombre, email, telefono)
            elif action == 'listar':
                list_customers()
            elif action == 'actualizar':
                id = input("ID del cliente a actualizar: ").strip()
                nombre = input("Nuevo nombre: ").strip()
                email = input("Nuevo email: ").strip()
                telefono = input("Nuevo teléfono: ").strip()
                update_customer(id, nombre, email, telefono)
            elif action == 'borrar':
                id = input("ID del cliente a borrar: ").strip()
                delete_customer(id)
            elif action == 'salir':
                break
            else:
                print("Acción no válida")
        except EOFError:
            break

if __name__ == "__main__":
    main()