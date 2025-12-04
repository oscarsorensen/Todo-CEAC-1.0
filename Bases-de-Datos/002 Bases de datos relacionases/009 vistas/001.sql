
CREATE VIEW personas_correos AS
SELECT
emails.direccion,
personas.nombre,
personas.apellidos
FROM emails
LEFT JOIN personas
ON emails.personas = personas.identificador;


select * from personas_correos; --se comporta como una tabla
