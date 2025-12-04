import pickle
import os

# Colores ANSI
class Colores:
    RESET = "\033[0m"
    BOLD = "\033[1m"
    CYAN = "\033[96m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    RED = "\033[91m"
    MAGENTA = "\033[95m"
    BLUE = "\033[94m"

# Clase Cliente
class Cliente:
    def __init__(self, nombre, apellidos, email):
        self.nombre = nombre
        self.apellidos = apellidos
        self.email = email

# Banner
def banner():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(Colores.MAGENTA + "═══════════════════════════════════════════════════════")
    print("💼 " + Colores.BOLD + "GESTIÓN DE CLIENTES v2.0".center(47))
    print(Colores.MAGENTA + "═══════════════════════════════════════════════════════")
    print(Colores.CYAN + "👤 Desarrollado por: " + Colores.GREEN + "Oscar Sørensen")
    print(Colores.MAGENTA + "═══════════════════════════════════════════════════════" + Colores.RESET)
    print()

# Cargar datos
clientes = []
try:
    with open("clientes.bin2", "rb") as archivo:
        clientes = pickle.load(archivo)
except:
    print(Colores.YELLOW + "⚠️  No existe archivo de datos. Se creará uno nuevo." + Colores.RESET)

# Funciones
def crear_cliente():
    print(Colores.CYAN + "\n🆕 Crear nuevo cliente\n" + Colores.RESET)
    nombre = input("👉 Nombre: ")
    apellidos = input("👉 Apellidos: ")
    email = input("📧 Email: ")
    clientes.append(Cliente(nombre, apellidos, email))
    print(Colores.GREEN + "✅ Cliente añadido correctamente.\n" + Colores.RESET)

def listar_clientes():
    print(Colores.CYAN + "\n📋 Lista de clientes\n" + Colores.RESET)
    if not clientes:
        print(Colores.YELLOW + "⚠️  No hay clientes registrados.\n" + Colores.RESET)
        return
    for i, cliente in enumerate(clientes):
        print(Colores.BOLD + f"🆔 ID: {i}" + Colores.RESET)
        print(f"👤 {cliente.nombre} {cliente.apellidos}")
        print(f"📧 {cliente.email}")
        print(Colores.MAGENTA + "───────────────────────────────" + Colores.RESET)
    print()

def actualizar_cliente():
    listar_clientes()
    try:
        i = int(input("✏️  Introduce el ID del cliente a actualizar: "))
        clientes[i].nombre = input("👉 Nuevo nombre: ")
        clientes[i].apellidos = input("👉 Nuevos apellidos: ")
        clientes[i].email = input("📧 Nuevo email: ")
        print(Colores.GREEN + "✅ Cliente actualizado correctamente.\n" + Colores.RESET)
    except:
        print(Colores.RED + "❌ Error: ID no válido.\n" + Colores.RESET)

def eliminar_cliente():
    listar_clientes()
    try:
        i = int(input("🗑️  Introduce el ID del cliente a eliminar: "))
        confirm = input("⚠️  ¿Seguro que deseas eliminarlo? (s/n): ").lower()
        if confirm == 's':
            clientes.pop(i)
            print(Colores.RED + "🗑️  Cliente eliminado.\n" + Colores.RESET)
        else:
            print(Colores.YELLOW + "❎ Eliminación cancelada.\n" + Colores.RESET)
    except:
        print(Colores.RED + "❌ Error: ID no válido.\n" + Colores.RESET)

# Guardar datos
def guardar_datos():
    with open("clientes.bin2", "wb") as archivo:
        pickle.dump(clientes, archivo)

# Programa principal
while True:
    banner()
    print(Colores.BOLD + Colores.BLUE + "📌 Menú principal" + Colores.RESET)
    print(Colores.CYAN + """
1️⃣  Crear cliente
2️⃣  Listar clientes
3️⃣  Actualizar cliente
4️⃣  Eliminar cliente
5️⃣  Salir
""" + Colores.RESET)

    try:
        opcion = int(input(Colores.YELLOW + "👉 Escoge una opción: " + Colores.RESET))
    except ValueError:
        print(Colores.RED + "❌ Opción inválida.\n" + Colores.RESET)
        continue

    if opcion == 1:
        crear_cliente()
    elif opcion == 2:
        listar_clientes()
    elif opcion == 3:
        actualizar_cliente()
    elif opcion == 4:
        eliminar_cliente()
    elif opcion == 5:
        guardar_datos()
        print(Colores.GREEN + "💾 Datos guardados. ¡Hasta pronto!\n" + Colores.RESET)
        break
    else:
        print(Colores.RED + "❌ Opción no reconocida.\n" + Colores.RESET)

    input(Colores.MAGENTA + "Presiona ENTER para continuar..." + Colores.RESET)
