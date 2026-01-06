
En este ejercicio trabajo con diagramas ER. Lo hago para comprender mejor cómo se puede representar un objeto completo junto con sus partes en un modelo de base de datos. Primero, observo el ejemplo dado de un coche y sus componentes, y luego creo mis propios ejemplos utilizando una casa y una bicicleta.



He creado una estructura ER en la que una entidad principal representa el objeto completo y las demás entidades representan sus componentes. Primero, he creado una casa, donde Casa es el todo (principal) y está relacionada con partes como Fundación, Columnas, Paredes, Ventanas, Entradas/Salidas y Techo, cada una con sus propiedades y una clave externa a Casa. Después, lo hago de nuevo con una bicicleta, donde Bicicleta es la entidad principal y está conectada con partes como Cuadro, Ruedas, Manillar, Frenos y Sillín. Esto se muestra en SQL.

# ---------- Paso 1: Revisa los ejemplos proporcionados ----------
Analizado. Rueda, Llanta, Neumático, Chasis, Motor y Chapa son partes del Coche.

# ---------- Paso 2 & 3: Dibuja tu propio diagrama ER y Añade propiedades ----------
-- CASA (main)
CREATE TABLE casa (
  id INT PRIMARY KEY,
  direccion VARCHAR(255),
  metros INT,
  color VARCHAR(100)
);

-- FUNDACION
CREATE TABLE fundacion (
  id INT PRIMARY KEY,
  tipo VARCHAR(100),
  profundidad INT,
  material VARCHAR(100),
  casa_id INT,
  FOREIGN KEY (casa_id) REFERENCES casa(id)
);

-- COLUMNAS
CREATE TABLE columnas (
  id INT PRIMARY KEY,
  material VARCHAR(100),
  cantidad INT,
  altura INT,
  casa_id INT,
  FOREIGN KEY (casa_id) REFERENCES casa(id)
);

-- PAREDES
CREATE TABLE paredes (
  id INT PRIMARY KEY,
  material VARCHAR(100),
  grosor INT,
  color VARCHAR(100),
  casa_id INT,
  FOREIGN KEY (casa_id) REFERENCES casa(id)
);

-- ENTRADAS Y SALIDAS (puertas, accesos)
CREATE TABLE entradas_salidas (
  id INT PRIMARY KEY,
  tipo VARCHAR(100),
  cantidad INT,
  material VARCHAR(100),
  casa_id INT,
  FOREIGN KEY (casa_id) REFERENCES casa(id)
);

-- VENTANAS
CREATE TABLE ventanas (
  id INT PRIMARY KEY,
  cantidad INT,
  tipo VARCHAR(100),
  material VARCHAR(100),
  casa_id INT,
  FOREIGN KEY (casa_id) REFERENCES casa(id)
);

-- TECHO
CREATE TABLE techo (
  id INT PRIMARY KEY,
  tipo VARCHAR(100),
  material VARCHAR(100),
  inclinacion VARCHAR(100),
  casa_id INT,
  FOREIGN KEY (casa_id) REFERENCES casa(id)
);

# ---------- Paso 4: Practica con diferentes objetos ----------
-- BICICLETA (main)
CREATE TABLE bicicleta (
  id INT PRIMARY KEY,
  marca VARCHAR(100),
  modelo VARCHAR(100),
  color VARCHAR(50)
);

-- CUADRO
CREATE TABLE cuadro (
  id INT PRIMARY KEY,
  material VARCHAR(100),
  tamaño VARCHAR(50),
  bicicleta_id INT,
  FOREIGN KEY (bicicleta_id) REFERENCES bicicleta(id)
);

-- RUEDAS
CREATE TABLE ruedas (
  id INT PRIMARY KEY,
  tamaño VARCHAR(50),
  tipo VARCHAR(50),
  bicicleta_id INT,
  FOREIGN KEY (bicicleta_id) REFERENCES bicicleta(id)
);

-- MANILLAR
CREATE TABLE manillar (
  id INT PRIMARY KEY,
  tipo VARCHAR(50),
  material VARCHAR(100),
  bicicleta_id INT,
  FOREIGN KEY (bicicleta_id) REFERENCES bicicleta(id)
);

-- FRENOS
CREATE TABLE frenos (
  id INT PRIMARY KEY,
  tipo VARCHAR(50),
  bicicleta_id INT,
  FOREIGN KEY (bicicleta_id) REFERENCES bicicleta(id)
);

-- SILLIN
CREATE TABLE sillin (
  id INT PRIMARY KEY,
  material VARCHAR(100),
  altura INT,
  bicicleta_id INT,
  FOREIGN KEY (bicicleta_id) REFERENCES bicicleta(id)
);


# ---------- Paso 5: Comparte tus diagramas ----------
Mi compañero de clase dice que es muy bueno. Por supuesto, comenta que todo podría ampliarse aún más, pero es perfecto como ejemplo. 


Este ejercicio me ayudó a comprender mejor cómo funciona la agregación en los diagramas ER. Aprendí a separar un objeto complejo en componentes y a relacionarlos correctamente mediante claves externas. Esto es muy útil para modelar sistemas reales, ya que muchas aplicaciones necesitan representar relaciones «todo-parte».