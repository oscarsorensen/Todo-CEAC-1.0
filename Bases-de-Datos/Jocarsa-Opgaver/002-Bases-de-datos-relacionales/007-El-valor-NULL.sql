--En las bases de datos relacionales, el valor NULL se utiliza para representar la ausencia de información o un dato desconocido.
--A diferencia de un valor vacío o cero, NULL indica que un campo no tiene ningún valor asignado todavía.
--Esto es útil en situaciones donde la información aún no está disponible, como un pedido que se ha creado pero todavía no tiene un producto definido.
--En este ejercicio, trabajo con la base de datos empresadam y la tabla pedidos para observar cómo se comporta el valor NULL, cómo se muestra en una consulta y cómo puede ser actualizado más adelante cuando el dato esté disponible.

sudo mysql -u root -p
SHOW DATABASES; 
--Database empresadam ya existe
-- Verifico que la base de datos esté seleccionada correctamente
USE empresadam;
SHOW TABLES;
--Tabla pedidos ya existe

INSERT INTO pedidos (numerodepedido, cliente, producto) VALUES ('1001', 'Juan Pérez', 'Laptop HP');
INSERT INTO pedidos (numerodepedido, cliente, producto) VALUES ('1002', 'María López', NULL);

SELECT * FROM pedidos;

-- el cliente con el pedido número 1002 no tiene un valor asignado para el producto.

--voy a corregir el valor NULL del producto para el pedido número 1002
UPDATE pedidos
SET producto = "Iphone 14"
WHERE numerodepedido = '1002';

select * from pedidos;
-- ahora el pedido número 1002 tiene asignado el producto "Iphone 14" en lugar de NULL.
 
--A través de este ejercicio comprobé que el valor NULL cumple una función esencial dentro de una base de datos:
--permite mantener la integridad de los registros incluso cuando faltan datos temporales.
--Aprendí que NULL no significa “cero” ni “vacío”, sino sin valor definido, y que puede reemplazarse fácilmente con un valor real mediante el comando UPDATE.
--Este concepto resulta especialmente útil en tablas de pedidos o clientes, donde ciertos campos pueden completarse en momentos distintos del proceso de trabajo.