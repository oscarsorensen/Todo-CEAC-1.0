 En esta actividad trabajo como asistente de gimnasio que necesita organizar la información de los clientes que entrenan en mi centro. Por ello, creo una base de datos para almacenar los datos indicados: el nombre del cliente, su edad, peso inicial, objetivo de entrenamiento y las fechas de sus sesiones. Este tipo de tarea podría darse perfectamente en la vida real si fuera contratado por un gimnasio para gestionar la información de sus clientes.



 Comienzo accediendo a MySQL con el siguiente comando:
 sudo mysql -u root -p
Después creo una base de datos llamada gimnasio con el comando:
 CREATE DATABASE gimnasio;
A continuación, accedo a la base de datos que acabo de crear:
 USE gimnasio;
Luego creo una tabla llamada clientes:
 CREATE TABLE clientes
 y otra llamada sesiones:
 CREATE TABLE sesiones
Después utilizo el comando INSERT para insertar los datos proporcionados (nombre, edad, peso inicial, objetivo, cliente_id, fecha y duración) en las tablas clientes y sesiones que acabo de crear:
 INSERT INTO clientes
De esta forma, ya tengo una base de datos llamada gimnasio, con dos tablas (clientes y sesiones) que contienen datos.
Finalmente, realizo una consulta para comprobar que la base de datos funciona correctamente y visualizar la información.
 El comando SELECT c.id selecciona la tabla clientes y el identificador del cliente. De la misma manera, selecciono el nombre, la edad, el peso y los demás datos.
 Luego uno las dos tablas mediante el siguiente comando:
SELECT c.id, c.nombre, c.edad, c.peso_inicial, c.objetivo, s.fecha, s.duracion
FROM clientes c
JOIN sesiones s ON c.id = s.cliente_id;




sudo mysql -u root -p -- Acceso a MySQL como usuario root

CREATE DATABASE gimnasio; -- Crear la base de datos gimnasio

USE gimnasio; -- Seleccionar la base de datos gimnasio

CREATE TABLE clientes ( -- Crear la tabla clientes
  id INT AUTO_INCREMENT PRIMARY KEY,
  nombre VARCHAR(100) NOT NULL,
  edad INT,
  peso_inicial DECIMAL(5,2),
  objetivo VARCHAR(255)
);


CREATE TABLE sesiones ( -- Crear la tabla sesiones
  id INT AUTO_INCREMENT PRIMARY KEY,
  cliente_id INT,
  fecha DATE NOT NULL,
  duracion TIME NOT NULL,
  FOREIGN KEY (cliente_id) REFERENCES clientes(id)
);

INSERT INTO clientes (nombre, edad, peso_inicial, objetivo) VALUES ('Juan Pérez', 30, 75.5, 'Perder 10 kg'); -- Insertar un cliente de ejemplo en la tabla clientes
INSERT INTO clientes (nombre, edad, peso_inicial, objetivo) VALUES ('María González', 28, 60.0, 'Aumentar fuerza'); -- Insertar otro cliente de ejemplo en la tabla clientes

INSERT INTO sesiones (cliente_id, fecha, duracion) VALUES (1, '2023-10-05', '60:00'); -- Insertar una sesión de ejemplo en la tabla sesiones
INSERT INTO sesiones (cliente_id, fecha, duracion) VALUES (2, '2023-10-06', '45:00'); -- Insertar otra sesión de ejemplo en la tabla sesiones

SELECT c.id, c.nombre, c.edad, c.peso_inicial, c.objetivo, s.fecha, s.duracion
FROM clientes c
JOIN sesiones s ON c.id = s.cliente_id; -- Consultar datos combinados de clientes y sesiones



Esta actividad me ha permitido comprender cómo se crean y gestionan bases de datos relacionales en MySQL. He aprendido a definir tablas relacionadas mediante claves primarias y foráneas, así como a insertar y consultar datos de forma estructurada. Este tipo de base de datos puede aplicarse fácilmente en un entorno real, como un gimnasio, donde es necesario registrar la información de los clientes y hacer un seguimiento de sus sesiones de entrenamiento. Además, este ejercicio refuerza los conocimientos adquiridos en la unidad sobre la organización y gestión eficiente de la información.