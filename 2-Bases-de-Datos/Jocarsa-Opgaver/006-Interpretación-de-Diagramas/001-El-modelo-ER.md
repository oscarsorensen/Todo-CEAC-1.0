En este ejercicio creo una base de datos relacional para una tienda online. Primero creo un diagrama ER para comprender las entidades y las relaciones y luego lo convierto a SQL para crear las tablas reales con claves primarias y externas. Para ello utilizo la página web de josevicentes. A continuación, utilizo Python para que el programa pueda interactuar con la base de datos.

Creo el diagrama ER con las entidades Cliente, Pedido, LineaPedido y Producto, definiendo sus atributos y cómo se relacionan entre sí. A continuación, genero este diseño en SQL creando las tablas y estableciendo las claves primarias y externas correctas para garantizar la integridad de los datos. Después, creo las clases Python que representan estas entidades y las conecto con la base de datos para que puedan realizar operaciones CRUD.

# ---------- Paso 1: Diseño de Diagrama ER ----------
Diagramas ER:

--
Cliente
id
nombre
apellidos
email
--
Pedido
id
fecha
cliente_id
--
Producto
id
nombre
precio
--
Linea_Pedido
id
Pedido_id
Producto_id

# ---------- Paso 2: Implementación en SQL ----------

CREATE TABLE cliente(
  id INT PRIMARY KEY,
  nombre VARCHAR(255),
  apellidos VARCHAR(255),
  email VARCHAR(255)
);

CREATE TABLE pedido(
  id INT PRIMARY KEY,
  fecha VARCHAR(255),
  cliente_id INT,
  FOREIGN KEY (cliente_id) REFERENCES cliente(id)
);

CREATE TABLE producto(
  id INT PRIMARY KEY,
  nombre VARCHAR(255),
  precio VARCHAR(255)
);

CREATE TABLE linea_pedido(
  id INT PRIMARY KEY,
  pedido_id INT,
  producto_id INT,
  FOREIGN KEY (pedido_id) REFERENCES pedido(id),
  FOREIGN KEY (producto_id) REFERENCES producto(id)
);



# ---------- Paso 3: Implementación en Python ----------

from typing import Optional

class Cliente:
    def __init__(self, id: Optional[int] = None, nombre: Optional[str] = None, apellidos: Optional[str] = None, email: Optional[str] = None):
        self.id = id
        self.nombre = nombre
        self.apellidos = apellidos
        self.email = email

    def __repr__(self):
        return f"Cliente(id={self.id!r}, nombre={self.nombre!r}, apellidos={self.apellidos!r}, email={self.email!r})"

    # FK1: id -> pedido.id

class Pedido:
    def __init__(self, id: Optional[int] = None, fecha: Optional[str] = None, cliente_id: Optional[int] = None):
        self.id = id
        self.fecha = fecha
        self.cliente_id = cliente_id

    def __repr__(self):
        return f"Pedido(id={self.id!r}, fecha={self.fecha!r}, cliente_id={self.cliente_id!r})"

    # FK1: id -> linea_pedido.id

class Producto:
    def __init__(self, id: Optional[int] = None, nombre: Optional[str] = None, precio: Optional[str] = None):
        self.id = id
        self.nombre = nombre
        self.precio = precio

    def __repr__(self):
        return f"Producto(id={self.id!r}, nombre={self.nombre!r}, precio={self.precio!r})"

    # FK1: id -> linea_pedido.id

class LineaPedido:
    def __init__(self, id: Optional[int] = None, pedido_id: Optional[int] = None, producto_id: Optional[int] = None):
        self.id = id
        self.pedido_id = pedido_id
        self.producto_id = producto_id

    def __repr__(self):
        return f"LineaPedido(id={self.id!r}, pedido_id={self.pedido_id!r}, producto_id={self.producto_id!r})"


# ---------- Paso 4: Ejecución y Prueba ----------

import sqlite3

conexion = sqlite3.connect("tienda.db")
cursor = conexion.cursor()

print("CREAR TABLA")
cursor.execute("""
CREATE TABLE IF NOT EXISTS pedido(
 id INTEGER PRIMARY KEY,
 fecha TEXT,
 cliente_id INTEGER
)
""")

print("INSERT (CREATE)")
cursor.execute("INSERT INTO pedido (id, fecha, cliente_id) VALUES (1, '2026-01-06', 10)")
conexion.commit()

print("SELECT (READ)")
cursor.execute("SELECT * FROM pedido")
print(cursor.fetchall())

print("UPDATE")
cursor.execute("UPDATE pedido SET fecha='2026-12-31' WHERE id=1")
conexion.commit()

cursor.execute("SELECT * FROM pedido")
print(cursor.fetchall())

print("DELETE")
cursor.execute("DELETE FROM pedido WHERE id=1")
conexion.commit()

cursor.execute("SELECT * FROM pedido")
print(cursor.fetchall())

conexion.close()

Gracias a este ejercicio, he podido practicar y ahora entiendo mejor cómo pasar del diseño teórico de una base de datos a su implementación real en SQL y cómo utilizarla desde Python. Esto es muy útil, porque muestra cómo el diseño, las bases de datos y la programación funcionan conjuntamente en los sistemas profesionales.