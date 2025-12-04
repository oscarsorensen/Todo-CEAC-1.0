Este ejercicio consistió en el diseño e implementación de un modelo de datos para la entidad Cliente, donde se creó una estructura de base de datos flexible y práctica para gestionar información de clientes. El enfoque principal fue desarrollar un esquema que se adaptara a escenarios reales donde los usuarios pueden no proporcionar toda su información personal durante el registro.

1. Crearemos una tabla llamada Cliente:

`
CREATE TABLE Cliente (
    dni VARCHAR(20) PRIMARY KEY,
    nombre VARCHAR(50),
    apellidos VARCHAR(100),
    email VARCHAR(100)
);
`

2. Características del Modelo:

Clave primaria: dni
Todos los campos son opcionales excepto dni (por ser PK)
No hay restricciones de unicidad en email
Estructura flexible que permite registros parciales
Tipos VARCHAR para adaptarse a diferentes longitudes de texto

3. Insertar un ejemplo de Cliente:

`
INSERT INTO Cliente (dni, nombre, apellidos, email)
VALUES ('48763219M', 'Ayman', 'Mouzakki', 'ayman.mouzakki@ejemplo.com');
`

4. Consultar el cliente insertado:

`
SELECT * FROM Cliente WHERE dni = '48763219M';
`

Vamos a juntar las ideas que tenemos arriba para crear un programa completo:

`
CREATE TABLE Cliente (
    dni VARCHAR(20) PRIMARY KEY,
    nombre VARCHAR(50),
    apellidos VARCHAR(100),
    email VARCHAR(100)
);

INSERT INTO Cliente (dni, nombre, apellidos, email)
VALUES ('48763219M', 'Ayman', 'Mouzakki', 'ayman.mouzakki@ejemplo.com');

-- Consultar el cliente insertado
SELECT * FROM Cliente WHERE dni = '48763219M';
`

Este ejercicio sienta las bases para un sistema de gestión de clientes robusto pero flexible, preparado para extenderse con relaciones con otras entidades como pedidos, facturas o reservas en futuras iteraciones.