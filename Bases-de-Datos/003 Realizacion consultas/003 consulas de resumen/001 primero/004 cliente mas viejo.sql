-- sudo mysql -u root 

use clientes;

-- # Contar el numero de registros en la tabla clientes
select 
    nombre,
    apellido,
    edad
from clientes
order by edad desc -- ordenamos de mayor a menor
limit 1;