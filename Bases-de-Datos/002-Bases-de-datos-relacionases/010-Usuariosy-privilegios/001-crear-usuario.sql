-- Crea usuario nuevo con contraseña
CREATE USER 'useroscar'@'localhost'
IDENTIFIED BY 'oscar1234';

-- Permite acceso a ese usuario (sin restricciones iniciales)
GRANT USAGE ON *.* TO 'useroscar'@'localhost';

-- Quita todos los límites
ALTER USER 'useroscar'@'localhost'
REQUIRE NONE
WITH MAX_QUERIES_PER_HOUR 0
MAX_CONNECTIONS_PER_HOUR 0
MAX_UPDATES_PER_HOUR 0
MAX_USER_CONNECTIONS 0;

-- Dale acceso completo a la base de datos empresadam
GRANT ALL PRIVILEGES ON empresadam.* TO 'useroscar'@'localhost';

-- Recarga los privilegios
FLUSH PRIVILEGES;
