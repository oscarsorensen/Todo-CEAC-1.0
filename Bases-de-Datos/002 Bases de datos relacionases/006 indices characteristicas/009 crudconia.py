import sqlite3
import os

# === ANSI colors ===
RESET = "\033[0m"
BOLD = "\033[1m"
CYAN = "\033[36m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
RED = "\033[31m"
MAGENTA = "\033[35m"

conexion = sqlite3.connect("empresa.db")
cursor = conexion.cursor()

# Ensure table exists (safe even if already created)
cursor.execute("""
CREATE TABLE IF NOT EXISTS clientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    apellidos TEXT NOT NULL,
    email TEXT NOT NULL
);
""")
conexion.commit()

def limpiar_pantalla():
    os.system("cls" if os.name == "nt" else "clear")

def cabecera(titulo):
    limpiar_pantalla()
    print(f"{BOLD}{CYAN}=== {titulo} ==={RESET}\n")

print(f"{BOLD}{MAGENTA}Programa Agenda SQLite v0.2 — Oscar Sorensen{RESET}")

while True:
    print(f"""
{BOLD}{CYAN}Menú principal{RESET}
{YELLOW}1.{RESET} Crear cliente
{YELLOW}2.{RESET} Listar clientes
{YELLOW}3.{RESET} Actualizar cliente
{YELLOW}4.{RESET} Eliminar cliente
{YELLOW}5.{RESET} Salir
""")

    try:
        opcion = int(input(f"{BOLD}Selecciona una opción:{RESET} "))
    except ValueError:
        print(f"{RED}Por favor, introduce un número válido.{RESET}\n")
        continue

    if opcion == 1:
        cabecera("Crear cliente")
        nombre = input("Nombre: ")
        apellidos = input("Apellidos: ")
        email = input("Email: ")

        # ✅ Safe and correct insertion
        cursor.execute("INSERT INTO clientes (nombre, apellidos, email) VALUES (?, ?, ?)", 
                       (nombre, apellidos, email))
        conexion.commit()

        print(f"{GREEN}\nCliente añadido correctamente.{RESET}\n")

    elif opcion == 2:
        cabecera("Listado de clientes")
        cursor.execute("SELECT * FROM clientes")
        filas = cursor.fetchall()
        if filas:
            print(f"{BOLD}{'ID':<5}{'Nombre':<15}{'Apellidos':<20}{'Email'}{RESET}")
            print("-" * 60)
            for fila in filas:
                print(f"{fila[0]:<5}{fila[1]:<15}{fila[2]:<20}{fila[3]}")
        else:
            print(f"{RED}No hay clientes registrados.{RESET}")
        print()

    elif opcion == 3:
        cabecera("Actualizar cliente")
        identificador = input("Introduce el ID a actualizar: ")
        cursor.execute("SELECT * FROM clientes WHERE id=?", (identificador,))
        cliente = cursor.fetchone()
        if cliente:
            nombre = input(f"Nuevo nombre ({cliente[1]}): ") or cliente[1]
            apellidos = input(f"Nuevos apellidos ({cliente[2]}): ") or cliente[2]
            email = input(f"Nuevo email ({cliente[3]}): ") or cliente[3]
            cursor.execute("UPDATE clientes SET nombre=?, apellidos=?, email=? WHERE id=?", 
                           (nombre, apellidos, email, identificador))
            conexion.commit()
            print(f"{GREEN}\nCliente actualizado correctamente.{RESET}\n")
        else:
            print(f"{RED}Cliente no encontrado.{RESET}\n")

    elif opcion == 4:
        cabecera("Eliminar cliente")
        identificador = input("Introduce el ID a eliminar: ")
        cursor.execute("SELECT * FROM clientes WHERE id=?", (identificador,))
        cliente = cursor.fetchone()
        if cliente:
            confirm = input(f"¿Seguro que deseas eliminar a {cliente[1]} {cliente[2]}? (s/n): ").lower()
            if confirm == "s":
                cursor.execute("DELETE FROM clientes WHERE id=?", (identificador,))
                conexion.commit()
                print(f"{GREEN}\nCliente eliminado correctamente.{RESET}\n")
            else:
                print(f"{YELLOW}\nOperación cancelada.{RESET}\n")
        else:
            print(f"{RED}Cliente no encontrado.{RESET}\n")

    elif opcion == 5:
        print(f"{BOLD}{MAGENTA}\nHasta pronto, Oscar!{RESET}")
        conexion.close()
        break

    else:
        print(f"{RED}Opción no válida.{RESET}\n")

    input(f"{BOLD}Pulsa Enter para continuar...{RESET}")
    limpiar_pantalla()
