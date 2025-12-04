En esta actividad, trabajo con una base de datos relacional que ya tengo, llamada empresadam, que contiene información de clientes de una empresa ficticia.
El objetivo es practicar la creación y modificación de tablas, aplicando diferentes restricciones de validación para garantizar que los datos sean correctos y se almacenen adecuadamente.

Estas operaciones son fundamentales en la administración de bases de datos, ya que permiten controlar el tipo de información que se puede insertar y evitar errores o duplicados.
A lo largo del ejercicio, utilizo comandos SQL para añadir, eliminar y renombrar columnas, así como para definir reglas de comprobación (CHECK) que validan el formato de campos importantes como el DNI/NIE y el correo electrónico.


-- Aplicación práctica: creación y modificación de la tabla clientes con restricciones de validación

sudo mysql -u root -p -- Acceso a MySQL como usuario root

USE empresadam; -- Seleccionar la base de datos empresadam

DESCRIBE clientes; -- Describir la estructura de la tabla clientes

ALTER TABLE clientes ADD COLUMN direccion VARCHAR(255); -- Agregar columna direccion

ALTER TABLE clientes DROP COLUMN direccion; -- Eliminar columna direccion. Estaba de prueba

ALTER TABLE clientes RENAME COLUMN dni TO dninie; -- Renombrar columna dni a dninie

-- Agregar restricción para validar DNI/NIE
ALTER TABLE clientes ADD CONSTRAINT comprobar_dni_nie_letra  
CHECK (
  (dninie REGEXP '^[0-9]{8}[A-Za-z]$' AND UPPER(SUBSTRING(dninie, 9, 1)) = SUBSTRING('TRWAGMYFPDXBNJZSQVHLCKE', (CAST(SUBSTRING(dninie, 1, 8) AS UNSIGNED) MOD 23) + 1, 1))
  OR
  (dninie REGEXP '^[XYZxyz][0-9]{7}[A-Za-z]$' AND UPPER(SUBSTRING(dninie, 9, 1)) = SUBSTRING('TRWAGMYFPDXBNJZSQVHLCKE', (CAST(CONCAT(CASE UPPER(SUBSTRING(dninie, 1, 1)) WHEN 'X' THEN '0' WHEN 'Y' THEN '1' WHEN 'Z' THEN '2' END, SUBSTRING(dninie, 2, 7)) AS UNSIGNED) MOD 23) + 1, 1))
);

-- Agregar restricción para validar formato de email
ALTER TABLE clientes ADD CONSTRAINT comprobar_email 
CHECK (email REGEXP '^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\.[A-Za-z]{2,}$');

-- Probar inserción con DNI/NIE inválido
INSERT INTO clientes VALUES(NULL, '12345678A', 'nombre del cliente', 'Carratala Sanchis', 'info@jocarsa.com'); -- DNI inválido

-- Debería insertarse correctamente 
INSERT INTO clientes VALUES(NULL, '12345678Z', 'Oscar', 'Sorensen', 'oscar@empresadam.com');

-- Consultar todos los registros de la tabla clientes. Muestras los datos insertados
SELECT * FROM clientes;

quit; -- Salir de MySQL

-- Realizar copia de seguridad de la base de datos empresadam
sudo mysqldump -u root -p empresadam > copiadeseguridad.sql 
-- Fin de la aplicación práctica: la base de datos se ha modificado y respaldado correctamente


Esta tarea práctica me ha ayudado a consolidar mis conocimientos sobre la modificación y validación de tablas en una base de datos MySQL.
He practicado cómo modificar estructuras existentes, añadir restricciones con expresiones regulares y realizar pruebas para garantizar la integridad de los datos.
Además, he comprendido la importancia de las copias de seguridad como parte del mantenimiento de los sistemas de información.
El uso de comandos SQL precisos me ayuda a desarrollar una base sólida para gestionar bases de datos de forma segura y profesional. 
También puedo ver cómo esto puede ser útil en un escenario real, ya que almacenar datos con criterios específicos es algo que hacen todas las empresas. Como se puede ver en la tarea, también he incorporado algunos datos personales, para mostrar cómo lo utilizaría personalmente.



