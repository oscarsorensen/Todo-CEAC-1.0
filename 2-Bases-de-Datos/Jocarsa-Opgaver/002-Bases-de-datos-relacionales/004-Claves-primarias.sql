
En este ejercicio, imagino que dirijo un restaurante. Mi restaurante guarda los datos importantes de los clientes, como el nombre y la dirección. Como cada cliente es único, necesito una clave primaria para garantizar que cada registro sea identificable y no haya duplicados.
El objetivo del ejercicio es crear un sistema que me permita almacenar los datos personales de los clientes de forma estructurada y coherente.
Como también me gusta ir al gimnasio, pienso en cómo se habría hecho si se tratara de las cuotas del gimnasio en lugar de las del restaurante. Llego a la conclusión de que se podría hacer de forma muy similar, ya que las dos tareas son parecidas.

sudo mysql -u root -p -- Acceso a MySQL como usuario root

show databases; -- Mostrar las bases de datos existentes
-- Empresadam ya existe, no es necesario crearla de nuevo

use Empresadam; -- Seleccionar la base de datos Empresadam

show tables; -- Mostrar las tablas existentes en la base de datos Empresadam

select * from clientes; -- Mostrar todos los registros de la tabla clientes

ALTER TABLE clientes ADD COLUMN identificador INT AUTO_INCREMENT PRIMARY KEY FIRST; -- Agregar una nueva columna identificador como clave primaria auto incremental al inicio de la tabla clientes

DESCRIBE clientes; -- Mostrar la estructura de la tabla clientes

INSERT INTO clientes (nombre, direccion) VALUES ('Juan Pérez', 'Calle Falsa 123');

SELECT * FROM clientes; -- Mostrar todos los registros de la tabla clientes. Todo correcto.

Este tipo de estructura sería muy útil para registrar los clientes que hacen reservas o pedidos en mi restaurante.
De igual forma, podría aplicarse en un gimnasio para registrar a los socios y controlar sus cuotas o membresías, ya que ambos casos requieren identificar cada usuario de forma única mediante una clave primaria.


A través de este ejercicio, aprendo a crear y gestionar datos dentro de una base de datos mediante SQL.
El uso de comandos como ALTER TABLE, ADD, AUTO_INCREMENT y PRIMARY KEY demuestra la importancia de definir correctamente las claves primarias para garantizar la integridad y organización de los datos.
Este conocimiento se relaciona directamente con la unidad sobre modelo de datos, ya que permite diseñar estructuras sólidas para aplicaciones reales.
