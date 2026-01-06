En este ejercicio trabajé con tres partes diferentes de la creación de un sitio web: bases de datos (SQL), Flask y plantillas con HTML y Jinja. Todo este ejercicio simula cómo funciona una aplicación web real con una base de datos que almacena la información y con Flask actuando como servidor, y las plantillas HTML mostrando la información correcta al usuario. Se trata básicamente de un mini proyecto de desarrollo full stack y muestra cómo las diferentes capas de una aplicación se comunican entre sí.

 Primero, creé las tablas SQL con sus claves primarias y claves externas y luego inserté algunos datos de ejemplo. Después, construí/modifiqué la aplicación Flask dada con varias páginas, como «inicio», «batoinfo» y «contactobatos», cada una con su propia plantilla HTML dentro de la carpeta de plantillas. Utilicé Jinja2 para renderizar las plantillas como hicimos en clase y conecté Flask con la base de datos para que las páginas pudieran mostrar datos reales en lugar de texto estático. Por último, probé las rutas en el navegador para comprobar que todo funcionaba correctamente. Y así fue.

# ---------- Crea las Tablas SQL ----------
-- =========================================
--  BASE DE DATOS
-- =========================================
CREATE DATABASE IF NOT EXISTS tienda_patitos
  CHARACTER SET utf8mb4
  COLLATE utf8mb4_unicode_ci;

USE tienda_patitos;

-- =========================================
-- TABLAS
-- =========================================

CREATE TABLE categorias (
    id_categoria INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL
);

CREATE TABLE productos (
    id_producto INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(150) NOT NULL,
    descripcion TEXT,
    precio DECIMAL(10,2) NOT NULL,
    id_categoria INT NOT NULL,
    CONSTRAINT fk_producto_categoria
        FOREIGN KEY (id_categoria)
        REFERENCES categorias(id_categoria)
        ON DELETE RESTRICT
        ON UPDATE CASCADE
);

CREATE TABLE clientes (
    id_cliente INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(150) NOT NULL,
    email VARCHAR(200) NOT NULL UNIQUE,
    telefono VARCHAR(50),
    direccion VARCHAR(255)
);

CREATE TABLE pedidos (
    id_pedido INT AUTO_INCREMENT PRIMARY KEY,
    fecha DATETIME NOT NULL,
    id_cliente INT NOT NULL,
    total DECIMAL(10,2),
    CONSTRAINT fk_pedido_cliente
        FOREIGN KEY (id_cliente)
        REFERENCES clientes(id_cliente)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);

CREATE TABLE lineas_pedido (
    id_linea INT AUTO_INCREMENT PRIMARY KEY,
    id_pedido INT NOT NULL,
    id_producto INT NOT NULL,
    cantidad INT NOT NULL,
    precio_unitario DECIMAL(10,2) NOT NULL,

    CONSTRAINT fk_linea_pedido
        FOREIGN KEY (id_pedido)
        REFERENCES pedidos(id_pedido)
        ON DELETE CASCADE,

    CONSTRAINT fk_linea_producto
        FOREIGN KEY (id_producto)
        REFERENCES productos(id_producto)
        ON DELETE RESTRICT
);

CREATE TABLE stock (
    id_stock INT AUTO_INCREMENT PRIMARY KEY,
    id_producto INT NOT NULL,
    cantidad INT NOT NULL,
    ubicacion VARCHAR(100),

    CONSTRAINT fk_stock_producto
        FOREIGN KEY (id_producto)
        REFERENCES productos(id_producto)
        ON DELETE CASCADE
);

-- =========================================
--  VISTAS
-- =========================================

CREATE VIEW vista_productos_categoria AS
SELECT p.id_producto, p.nombre, p.precio, c.nombre AS categoria
FROM productos p
INNER JOIN categorias c ON p.id_categoria = c.id_categoria;

CREATE VIEW vista_pedidos_clientes AS
SELECT pe.id_pedido, pe.fecha, pe.total, c.nombre AS cliente, c.email
FROM pedidos pe
INNER JOIN clientes c ON pe.id_cliente = c.id_cliente;

CREATE VIEW vista_lineas_pedido_detalle AS
SELECT lp.id_linea, pe.id_pedido, c.nombre AS cliente,
       pr.nombre AS producto, lp.cantidad, lp.precio_unitario
FROM lineas_pedido lp
INNER JOIN pedidos pe ON lp.id_pedido = pe.id_pedido
INNER JOIN clientes c ON pe.id_cliente = c.id_cliente
INNER JOIN productos pr ON lp.id_producto = pr.id_producto;



# ---------- Inserta Datos Ejemplo  ----------

-- =========================================
--  INSERTS (ORDEN CORRECTO)
-- =========================================

INSERT INTO categorias (nombre) VALUES
('Patos Clásicos'),
('Patos Animales'),
('Patos Temáticos'),
('Patos Edición Limitada');

INSERT INTO clientes (nombre, email, telefono, direccion) VALUES
('Juan Pérez', 'juan@example.com', '600000001', 'Madrid'),
('Laura Gomez', 'laura@example.com', '600000002', 'Valencia'),
('Carlos Ruiz', 'carlos@example.com', '600000003', 'Barcelona');

INSERT INTO productos (nombre, descripcion, precio, id_categoria) VALUES
('Pato Clásico Amarillo', 'El pato de goma de toda la vida', 4.99, 1),
('Pato León', 'Pato de goma disfrazado de león', 7.50, 2),
('Pato Superhéroe', 'Pato edición especial de superhéroe', 9.99, 3),
('Pato Dorado Deluxe', 'Edición limitada colección premium', 19.99, 4);

INSERT INTO stock (id_producto, cantidad, ubicacion) VALUES
(1, 120, 'Almacén A'),
(2, 60, 'Almacén B'),
(3, 45, 'Almacén A'),
(4, 10, 'Caja Seguridad');

INSERT INTO pedidos (fecha, id_cliente, total) VALUES
(NOW(), 1, 0),
(NOW(), 2, 0);

INSERT INTO lineas_pedido (id_pedido, id_producto, cantidad, precio_unitario) VALUES
(1, 1, 3, 4.99),
(1, 3, 1, 9.99),
(2, 2, 2, 7.50);

UPDATE pedidos
SET total = (
  SELECT SUM(cantidad * precio_unitario)
  FROM lineas_pedido
  WHERE lineas_pedido.id_pedido = pedidos.id_pedido
);
# ---------- Desarrolla la Aplicación Web ----------
import mysql.connector
from flask import Flask, render_template 

app = Flask(__name__)
conexion = mysql.connector.connect(
    host="localhost",
    user="root",         
    password="",          
    database="tienda_patitos"
)


@app.route("/")
def inicio():
  return render_template("inicio.html")
  
@app.route("/sobremi")
def sobremi():
    cursor = conexion.cursor(dictionary=True)
    cursor.execute("SELECT nombre, precio FROM productos")
    productos = cursor.fetchall()
    return render_template("batoinfo.html", productos=productos)
  
@app.route("/contacto")
def contacto():
  return render_template("contactobatos.html")

if __name__ == "__main__":
  app.run(debug=True)

# ---------- Integra el Modelo con la Vista ----------
Los 3 plantillas

"inicio.html"
<!doctype html>
<html lang="es">
  <head>
    <title>La página de Los Batos</title>
    <meta charset="utf-8">
  </head>
  <body>
    <h1>La página de Los Batos</h1>
    <nav>
      <a href="/">Inicio</a>
      <a href="/sobremi">batoinfo</a>
      <a href="/contacto">contactobatos</a>
    </nav>
    <p>Esta es la página de inicio</p>
  </body>
</html>

"batoinfo.html"

<!doctype html>
<html lang="es">
  <head>
    <title>La página de Los Batos</title>
    <meta charset="utf-8">
  </head>
  <body>
    <h1>La página de Los Batos</h1>
    <nav>
      <a href="/">Inicio</a>
      <a href="/sobremi">batoinfo</a>
      <a href="/contacto">contactobatos</a>
    </nav>
    
    <p>Lista de productos:</p>

        <ul>
        {% for p in productos %}
            <li>{{ p.nombre }} - {{ p.precio }} €</li>
        {% endfor %}
        </ul>


  </body>
</html>

"contactobatos.html"

<!doctype html>
<html lang="es">
  <head>
    <title>La página de Los Batos</title>
    <meta charset="utf-8">
  </head>
  <body>
    <h1>La página de Los Batos</h1>
    <nav>
      <a href="/">Inicio</a>
      <a href="/sobremi">batoinfo</a>
      <a href="/contacto">contactobatos</a>
    </nav>
    <p>Esta es la página de contactobatos</p>
  </body>
</html>

# ---------- Prueba tu Aplicación ----------
from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)

def conexion():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="tienda_patitos"
    )

@app.route("/")
def inicio():
    db = conexion()
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT nombre, precio FROM productos")
    productos = cursor.fetchall()
    db.close()

    return render_template("inicio.html", productos=productos)

if __name__ == "__main__":
    app.run(debug=True)

<!-- todo funciona correctamente -->

# ---------- Documenta Tu Proceso ----------

Primero olvidé añadir las claves externas, pero lo solucioné. Por lo demás, funcionó según lo previsto, ya que lo hemos hecho en clase.

Este ejercicio me ayudó a practicar cómo funcionan juntas diferentes tecnologías y lenguajes de programación en un proyecto real. Ahora puedo ver más claramente cómo SQL, Flask y HTML + Jinja2 forman un sistema funcional completo. Esto es muy práctico en un escenario real, donde me veo a mí mismo realizando este tipo de tareas. Fue bastante más largo que otras tareas que he realizado, pero lo disfruté.