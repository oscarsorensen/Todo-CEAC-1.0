

use clientes;

-- Operador lógico AND (&&)
select
nombre, apellido, edad, edad < 30 as "es menor que 30?",
edad >= 30 && edad < 40 as "esta entre 30 y 40?",
edad > 40 as "es mayor de 40?"
from clientes;