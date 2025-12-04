"""
En este ejercicio trabajo con una aplicación web creada para gestionar los clientes y sus reservas en mi gimnasio local.
El sistema almacena información personal y de contacto de cada cliente, por lo que es fundamental evitar cualquier pérdida de datos.
Para garantizar la seguridad y la integridad de la información, realizo copias de seguridad periódicas de la base de datos y ejecuto operaciones básicas como la actualización o eliminación de registros.
De este modo, mantengo la base de datos del gimnasio siempre actualizada, organizada y protegida ante posibles errores o fallos técnicos.
"""

"""
-- empiezo creando una carpeta en mi escritorio llamada "micopiadeseguridad" para almacenar las copias de seguridad de la base de datos del gimnasio.

cd ~/Escritorio/
mkdir micopiadeseguridad
cd micopiadeseguridad

-- A continuación, utilizo el siguiente comando para crear una copia de seguridad completa de la base de datos "empresarial" y guardarla en la carpeta "micopiadeseguridad".
mysqldump -u usuarioempresarial -p empresarial > copia_de_seguridad_empresarial.sql

"""
-- Después de realizar la copia de seguridad, aplico las siguientes operaciones SQL para actualizar y eliminar clientes"
-- Insertar un nuevo cliente en la tabla "clientes"
-- Actualizar el nombre de un cliente según su número de teléfono
UPDATE clientes
SET nombre = "Jose Vicente"
WHERE telefono = 620891718;

-- Eliminar el cliente una vez realizado el cambio, si ya no pertenece al gimnasio
DELETE FROM clientes
WHERE telefono = '620891718';

-- Para restaurar la base de datos desde la copia de seguridad, utilizo el siguiente comando:
mysql -u usuarioempresarial -p empresarial < gestion_clientes.sql


"""
Las copias de seguridad y las operaciones de mantenimiento en bases de datos son esenciales para garantizar la seguridad de la información en cualquier aplicación profesional.
En el caso del gimnasio, estas acciones permiten conservar los datos de los clientes, prevenir pérdidas y asegurar un funcionamiento estable del sistema web.
Este ejercicio demuestra cómo las herramientas básicas de MySQL, usadas de forma planificada, contribuyen directamente a la fiabilidad y éxito del proyecto.
"""