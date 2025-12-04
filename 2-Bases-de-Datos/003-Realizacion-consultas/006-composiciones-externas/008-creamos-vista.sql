

create view matriculas_join as
SELECT 
asignaturas.nombre as "Nombre de la asignatura",
alumnos.nombre as "Nombre del alumno",
alumnos.apellidos as "Apellidos del alumno"
FROM matriculas
LEFT JOIN asignaturas
ON matriculas.id_asignatura = asignaturas.Identificador
LEFT JOIN alumnos
ON matriculas.id_alumno = alumnos.Identificador;