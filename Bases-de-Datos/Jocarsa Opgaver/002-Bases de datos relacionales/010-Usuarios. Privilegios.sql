--En esta tarea practico la creación y gestión de usuarios en MySQL, mostrando los usuarios existentes y asignando privilegios a uno nuevo.
--El objetivo es comprender cómo funcionan los permisos y accesos dentro de un sistema de bases de datos relacional, asegurando que cada usuario tenga los privilegios adecuados según sus necesidades.

--Para realizar la práctica, primero se accede al servidor MySQL con el usuario administrador root y se consultan las tablas internas de MySQL para visualizar los usuarios existentes y sus permisos.
--A continuación, se crea un nuevo usuario mediante la instrucción CREATE USER, estableciendo una contraseña segura y los límites de uso configurables con ALTER USER.
--Posteriormente, se asignan los privilegios necesarios con GRANT, limitando su acceso a la base de datos empresadam.
--Finalmente, se ejecuta FLUSH PRIVILEGES para actualizar los permisos en el sistema y aplicar los cambios.


sudo mysql -u root -p;

SELECT User, Host FROM mysql.user;
SELECT * FROM mysql.user;



-- Crea el nombre de usuario que queremos
CREATE USER 'nuevo_usuario'@'localhost' IDENTIFIED BY 'MuySegurocontraseña123!!!';

-- Permite acceso a ese usuario
GRANT USAGE ON *.* TO 'nuevo_usuario'@'localhost';

-- Quitale todos los limites que tenga
ALTER USER 'nuevo_usuario'@'localhost' REQUIRE NONE WITH MAX_QUERIES_PER_HOUR 0 MAX_CONNECTIONS_PER_HOUR 0 MAX_UPDATES_PER_HOUR 0 MAX_USER_CONNECTIONS 0;

-- Dale acceso a la base de datos empresadam
GRANT ALL PRIVILEGES ON empresadam.* TO 'nuevo_usuario'@'localhost';

-- Recarga la tabla de privilegios
FLUSH PRIVILEGES;
exit;

-- Este ejercicio demuestra cómo crear usuarios y asignar privilegios
-- de forma controlada, garantizando la seguridad y el acceso correcto a la base de datos.
