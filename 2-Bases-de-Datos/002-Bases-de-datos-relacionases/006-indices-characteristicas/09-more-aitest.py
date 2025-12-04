import sqlite3
import os
import time
import random

# 🎨 ANSI colors
RESET = "\033[0m"
BOLD = "\033[1m"
CYAN = "\033[36m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
MAGENTA = "\033[95m"
WHITE = "\033[97m"
BG_PURPLE = "\033[45m"
BG_BLUE = "\033[44m"

# 🗄️ Connect to funky database
DB_NAME = "empresa_funka.db"
conexion = sqlite3.connect(DB_NAME)
cursor = conexion.cursor()

# 🧱 Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS clientes(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    apellidos TEXT NOT NULL,
    email TEXT NOT NULL
);
""")

# 🧩 Preload data only if table is empty
cursor.execute("SELECT COUNT(*) FROM clientes;")
count = cursor.fetchone()[0]

if count == 0:
    demo_clients = [
        ("Alice", "Johnson", "alice.johnson@email.com"),
        ("Bob", "Snow", "bob.snow@email.eu"),
        ("Charlie", "Smith", "charlie.smith@email.com"),
        ("Diana", "Evans", "diana.evans@email.org"),
        ("Ethan", "Brooks", "ethan.brooks@email.net"),
        ("Fiona", "Anders", "fiona.anders@email.com"),
        ("George", "Hill", "george.hill@email.eu"),
        ("Hannah", "Peters", "hannah.peters@email.org"),
        ("Ian", "Reed", "ian.reed@email.com"),
        ("Julia", "Stone", "julia.stone@email.net"),
    ]
    cursor.executemany("INSERT INTO clientes (nombre, apellidos, email) VALUES (?, ?, ?)", demo_clients)
    conexion.commit()

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def banner(title):
    clear()
    print(f"{BG_PURPLE}{WHITE}{BOLD}💾 {title} 💾{RESET}\n")

def delay(msg, color=WHITE, seconds=0.6):
    for char in msg:
        print(color + char + RESET, end="", flush=True)
        time.sleep(seconds / len(msg))
    print()

# 🚀 Start
banner("AGENDA FUNKA v2.0 — OSCAR SORENSEN")
delay("✨ Bienvenido al gestor de clientes más cool de la galaxia... 🚀", CYAN)
time.sleep(0.4)

while True:
    print(f"""
{BOLD}{MAGENTA}╔══════════════════════════════════════════╗
║           🌈 MENÚ PRINCIPAL 🌈            ║
╚══════════════════════════════════════════╝{RESET}
{YELLOW}1.{RESET} ✨ Crear cliente nuevo
{YELLOW}2.{RESET} 📜 Listar todos los clientes
{YELLOW}3.{RESET} 🔄 Actualizar un cliente
{YELLOW}4.{RESET} ❌ Eliminar un cliente
{YELLOW}5.{RESET} 🚪 Salir del programa
""")

    opcion = input(f"{BOLD}👉 Elige una opción:{RESET} ")

    if opcion == "1":
        banner("CREAR CLIENTE ✨")
        nombre = input("👤 Nombre: ")
        apellidos = input("🧾 Apellidos: ")
        email = input("📧 Email: ")

        cursor.execute("INSERT INTO clientes (nombre, apellidos, email) VALUES (?, ?, ?)",
                       (nombre, apellidos, email))
        conexion.commit()

        emojis = ["🎉", "💫", "🪩", "🚀", "🎈", "🌟"]
        print(f"\n{GREEN}✅ Cliente '{nombre} {apellidos}' añadido con éxito! {random.choice(emojis)}{RESET}")
        time.sleep(1)

    elif opcion == "2":
        banner("LISTA DE CLIENTES 📜")
        cursor.execute("SELECT * FROM clientes")
        filas = cursor.fetchall()
        if filas:
            print(f"{BOLD}{CYAN}{'🆔 ID':<7}{'Nombre':<15}{'Apellidos':<20}{'Email'}{RESET}")
            print(f"{MAGENTA}{'─'*60}{RESET}")
            for fila in filas:
                color = random.choice([YELLOW, GREEN, CYAN, WHITE])
                print(f"{color}{fila[0]:<7}{fila[1]:<15}{fila[2]:<20}{fila[3]}{RESET}")
            print()
        else:
            print(f"{RED}⚠️ No hay clientes registrados aún. Añade uno con opción 1.{RESET}")
        input(f"\nPresiona Enter para volver al menú...")

    elif opcion == "3":
        banner("ACTUALIZAR CLIENTE 🔄")
        identificador = input("🔢 ID del cliente a actualizar: ")
        cursor.execute("SELECT * FROM clientes WHERE id=?", (identificador,))
        cliente = cursor.fetchone()
        if cliente:
            print(f"{BOLD}Cliente actual: {GREEN}{cliente[1]} {cliente[2]} - {CYAN}{cliente[3]}{RESET}\n")
            nombre = input(f"Nuevo nombre ({cliente[1]}): ") or cliente[1]
            apellidos = input(f"Nuevos apellidos ({cliente[2]}): ") or cliente[2]
            email = input(f"Nuevo email ({cliente[3]}): ") or cliente[3]

            cursor.execute("UPDATE clientes SET nombre=?, apellidos=?, email=? WHERE id=?",
                           (nombre, apellidos, email, identificador))
            conexion.commit()
            print(f"{GREEN}\n✅ Cliente actualizado correctamente! 💪{RESET}")
        else:
            print(f"{RED}⚠️ No existe ningún cliente con ID {identificador}.{RESET}")
        time.sleep(1.5)

    elif opcion == "4":
        banner("ELIMINAR CLIENTE ❌")
        identificador = input("🔢 ID del cliente a eliminar: ")
        cursor.execute("SELECT * FROM clientes WHERE id=?", (identificador,))
        cliente = cursor.fetchone()
        if cliente:
            confirm = input(f"¿Seguro que quieres eliminar a {cliente[1]} {cliente[2]}? (s/n): ").lower()
            if confirm == "s":
                cursor.execute("DELETE FROM clientes WHERE id=?", (identificador,))
                conexion.commit()
                print(f"{RED}🗑️ Cliente eliminado con éxito.{RESET}")
            else:
                print(f"{YELLOW}🚫 Operación cancelada.{RESET}")
        else:
            print(f"{RED}⚠️ Cliente no encontrado.{RESET}")
        time.sleep(1.5)

    elif opcion == "5":
        banner("👋 DESPEDIDA")
        delay("Gracias por usar AGENDA FUNKA 💾 — Hasta pronto, Oscar! 🌈", GREEN)
        conexion.close()
        break

    else:
        print(f"{RED}⚠️ Opción no válida. Inténtalo de nuevo!{RESET}")
        time.sleep(1.2)
        clear()
