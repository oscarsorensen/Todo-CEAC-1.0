
-- En esta tarea, voy a crear una base de datos en SQL para organizar los datos de los clientes de manera eficiente y estructurada. Utilizaré entidades y variables para resolver esta tarea. Esto podría ser útil para alguien a quien le guste ir al gimnasio y cocinar. Una gestión eficiente de los datos supone menos tiempo dedicado, lo que ayuda a conciliar el trabajo y la vida personal. Es importante almacenar los datos en bases de datos relacionales, ya que esto permite obtener fácilmente una visión general y un mayor control sobre los entornos. Las bases de datos son necesarias en nuestro mundo moderno, tanto en los grandes bancos como en las pequeñas empresas familiares. Son una forma excelente de obtener una visión general de lo que es importante y de almacenar datos importantes.


sudo mysql -u root -p; -- Acceso a MySQL como usuario root

create database Clientes; -- Crear la base de datos Clientes
use Clientes; -- Seleccionar la base de datos Clientes

CREATE TABLE clientes ( -- Crear la tabla clientes
    dni VARCHAR(10) PRIMARY KEY, -- define dni como clave primaria
    nombre VARCHAR(50) NOT NULL, -- define nombre como un campo obligatorio
    apellidos VARCHAR(100) NOT NULL, -- define apellidos como un campo obligatorio
    email VARCHAR(100) UNIQUE NOT NULL -- define email como un campo único y obligatorio
);

-- Insertar clientes de ejemplo en la tabla clientes

INSERT INTO clientes (dni, nombre, apellidos, email)
VALUES 
    ('12345678A', 'Oscar', 'Sorensen', 'algo@correo.com'),
    ('12345678B', 'Jose Vicente', 'Carratala', 'josecarsa@correo.com'),
    ('12345678C', 'Bob', 'Jensen', 'bobs@correo.com');

show tables; -- Mostrar las tablas en la base de datos actual
DESCRIBE clientes; -- Describir la estructura de la tabla clientes


-- El código anterior muestra cómo crear y utilizar entidades y variables para crear una base de datos en SQL, que puede almacenar datos de manera eficiente. Las bases de datos son importantes en nuestro mundo globalizado, desde las empresas más grandes hasta las más pequeñas. Ponen orden en nuestras vidas, que de otro modo estarían desorganizadas. Las bases de datos son la columna vertebral de toda la infraestructura moderna y, por lo tanto, son de vital importancia en situaciones de la vida real. 