CREATE DATABASE MyMusicStore
    CHARACTER SET utf8mb4
    COLLATE utf8mb4_unicode_ci;

USE MyMusicStore;

CREATE TABLE productos_musica (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    categoria VARCHAR(100),
    marca VARCHAR(100),
    anio INT,
    precio DECIMAL(15,2),
    web VARCHAR(150)
);

INSERT INTO productos_musica (nombre, categoria, marca, anio, precio, web) VALUES
('Guitarra Acústica Dreadnought', 'Guitarras', 'Yamaha', 2023, 349.99, 'https://www.yamaha.com'),
('Teclado Digital P-45', 'Teclados', 'Yamaha', 2022, 499.00, 'https://www.yamaha.com'),
('Batería Acústica Export', 'Baterías', 'Pearl', 2021, 899.50, 'https://pearldrum.com'),
('Micrófono SM58', 'Micrófonos', 'Shure', 2024, 119.00, 'https://www.shure.com');

CREATE USER 'usuariomusicstore'@'localhost' 
IDENTIFIED BY 'pwmusicstore$';

GRANT USAGE ON *.* TO 'usuariomusicstore'@'localhost';

ALTER USER 'usuariomusicstore'@'localhost'
WITH MAX_QUERIES_PER_HOUR 0 
MAX_CONNECTIONS_PER_HOUR 0 
MAX_UPDATES_PER_HOUR 0 
MAX_USER_CONNECTIONS 0;

GRANT ALL PRIVILEGES ON MyMusicStore.* 
TO 'usuariomusicstore'@'localhost';

FLUSH PRIVILEGES;

INSERT INTO productos_musica (id, nombre, categoria, marca, anio, precio, web) VALUES (
    NULL,
    'Guitarra Eléctrica Stratocaster',
    'Guitarras',
    'Fender',
    2024,
    1200.00,
    'https://www.fender.com'
);

UPDATE productos_musica
SET precio = 10
WHERE nombre = 'Micrófono SM58';

SELECT * FROM productos_musica;
