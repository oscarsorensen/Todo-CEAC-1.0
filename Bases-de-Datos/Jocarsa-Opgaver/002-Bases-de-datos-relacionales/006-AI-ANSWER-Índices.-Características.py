

import sqlite3

# Connect to database (creates file if it doesn't exist)
connection = sqlite3.connect("clients.db")
cursor = connection.cursor()

# Create table if it doesn’t exist
cursor.execute("""
CREATE TABLE IF NOT EXISTS clients (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    surname TEXT,
    email TEXT
)
""")
connection.commit()

# ----------------------------
# CREATE
# ----------------------------
def create_client(name, surname, email):
    cursor.execute("INSERT INTO clients (name, surname, email) VALUES (?, ?, ?)", (name, surname, email))
    connection.commit()
    print("Client added successfully.")

# ----------------------------
# READ
# ----------------------------
def list_clients():
    cursor.execute("SELECT * FROM clients")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

# ----------------------------
# UPDATE
# ----------------------------
def update_client(id, new_name, new_surname, new_email):
    cursor.execute("UPDATE clients SET name=?, surname=?, email=? WHERE id=?", (new_name, new_surname, new_email, id))
    connection.commit()
    print("Client updated successfully.")

# ----------------------------
# DELETE
# ----------------------------
def delete_client(id):
    cursor.execute("DELETE FROM clients WHERE id=?", (id,))
    connection.commit()
    print("Client deleted successfully.")

# ----------------------------
# MENU
# ----------------------------
while True:
    print("\n--- CLIENT DATABASE MENU ---")
    print("1. Create client")
    print("2. List clients")
    print("3. Update client")
    print("4. Delete client")
    print("0. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        name = input("Name: ")
        surname = input("Surname: ")
        email = input("Email: ")
        create_client(name, surname, email)

    elif choice == "2":
        list_clients()

    elif choice == "3":
        id = input("Client ID to update: ")
        new_name = input("New name: ")
        new_surname = input("New surname: ")
        new_email = input("New email: ")
        update_client(id, new_name, new_surname, new_email)

    elif choice == "4":
        id = input("Client ID to delete: ")
        delete_client(id)

    elif choice == "0":
        break

    else:
        print("Invalid option. Try again.")

# Close connection
connection.close()
