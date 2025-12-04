CREATE TABLE persona (
  id INT PRIMARY KEY,
  nombre VARCHAR(255),
  apellidos VARCHAR(255)
);

CREATE TABLE alumno (
  id INT PRIMARY KEY,
  nia VARCHAR(255),
  CONSTRAINT fk_alumno_1 FOREIGN KEY (id) REFERENCES persona(id)
);

CREATE TABLE entidad (
  id INT PRIMARY KEY,
  atributo VARCHAR(255),
  CONSTRAINT fk_entidad_1 FOREIGN KEY (id) REFERENCES persona(id)
);