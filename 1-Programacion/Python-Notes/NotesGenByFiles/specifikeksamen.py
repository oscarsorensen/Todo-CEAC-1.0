# ==============================================================
# HOW TO USE THIS TEMPLATE (EXAM INSTRUCTIONS)
# ==============================================================
# 1) This is a universal CRUD program ready for exam use.
#    It connects to MySQL and performs Create, Read, Update, Delete.
#
# 2) Change only names to match the exam theme:
#      examdb     →  your database (e.g. blog, journal, ads)
#      category   →  main table (e.g. autores, usuarios)
#      item       →  secondary table (e.g. entradas, anuncios)
#
# 3) What’s already included:
#    - MySQL connection setup
#    - Full CRUD functions (Create, Read, Update, Delete)
#    - Infinite menu loop with if/elif structure
#    - Clean console output
#
# 4) How to test:
#    - Run the SQL template first to create the DB and user
#    - Then execute this Python file in VS Code terminal
#    - Check results with "Read" (option 2)
#
# 5) To adapt fast in exam:
#    a) Ctrl+H to rename table and field names
#    b) Add/remove fields if needed
#    c) Verify connection (no errors on startup)
#
# 6) Compatible with MySQL 8 and Python 3 (CEAC exam setup)
# ==============================================================

import mysql.connector

# ---------- 1) DATABASE CONNECTION ----------
config = {
    "host": "localhost",
    "user": "exam_user",     # same as in SQL script
    "password": "1234",
    "database": "examdb"     # change to your database name
}

db = mysql.connector.connect(**config)
cursor = db.cursor()

# ---------- 2) CRUD FUNCTIONS ----------

def create_item():
    title = input("Title: ")
    category_id = input("Category ID: ")
    content = input("Content: ")
    sql = "INSERT INTO item (title, category_id, date, image, content) VALUES (%s, %s, CURDATE(), '', %s)"
    cursor.execute(sql, (title, category_id, content))
    db.commit()
    print("Record created successfully.")

def read_items():
    cursor.execute("SELECT item.id, item.title, category.name FROM item LEFT JOIN category ON item.category_id = category.id")
    results = cursor.fetchall()
    for row in results:
        print(row)

def update_item():
    item_id = input("ID to update: ")
    new_title = input("New title: ")
    sql = "UPDATE item SET title=%s WHERE id=%s"
    cursor.execute(sql, (new_title, item_id))
    db.commit()
    print("Record updated successfully.")

def delete_item():
    item_id = input("ID to delete: ")
    sql = "DELETE FROM item WHERE id=%s"
    cursor.execute(sql, (item_id,))
    db.commit()
    print("Record deleted successfully.")

# ---------- 3) MENU LOOP ----------

def menu():
    while True:
        print("\n=== CONTROL PANEL ===")
        print("1. Create")
        print("2. Read")
        print("3. Update")
        print("4. Delete")
        print("5. Exit")

        option = input("Select an option: ")

        if option == "1":
            create_item()
        elif option == "2":
            read_items()
        elif option == "3":
            update_item()
        elif option == "4":
            delete_item()
        elif option == "5":
            print("Exiting program.")
            break
        else:
            print("Invalid option.")

# ---------- 4) START PROGRAM ----------

if __name__ == "__main__":
    print("Welcome to the CRUD control panel.")
    menu()
    cursor.close()
    db.close()
