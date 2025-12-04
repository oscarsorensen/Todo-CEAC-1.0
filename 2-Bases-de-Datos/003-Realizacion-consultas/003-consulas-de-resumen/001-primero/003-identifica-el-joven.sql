-- sudo mysql -u root 

use clientes;

-- # Contar el numero de registros en la tabla clientes
select 
    nombre,
    apellido,
    edad
from clientes
order by edad asc -- ordenamos de menor a mayor
limit 1;