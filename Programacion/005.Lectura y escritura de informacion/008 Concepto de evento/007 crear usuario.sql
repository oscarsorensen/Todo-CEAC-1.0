
-- crea usuario nuevo con contraseña
CREATE USER 
'empresadam2'@'localhost' 
IDENTIFIED  BY 'Empresadam123$';
-- permite acceso a ese usuario
GRANT USAGE ON *.* TO 'empresadam2'@'localhost';
-- quitale todos los limites que tenga
ALTER USER 'empresadam2'@'localhost' 
REQUIRE NONE 
WITH MAX_QUERIES_PER_HOUR 0 
MAX_CONNECTIONS_PER_HOUR 0 
MAX_UPDATES_PER_HOUR 0 
MAX_USER_CONNECTIONS 0;
-- dale acceso a la base de datos empresadam
GRANT ALL PRIVILEGES ON `empresadam`.* 
TO 'empresadam2'@'localhost';
-- recarga la tabla de privilegios
FLUSH PRIVILEGES;