
SELECT
    nombre AS "Nombre del cliente",
    apellido AS "Apellido del cliente",
    edad AS "Edad del cliente"
FROM
    clientes
ORDER BY
    edad DESC,
    apellido ASC;
