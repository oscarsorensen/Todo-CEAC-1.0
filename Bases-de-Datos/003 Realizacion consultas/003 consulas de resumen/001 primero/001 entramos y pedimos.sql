
-- sudo mysql -u root 

use clientes;

-- # Contar el numero de registros en la tabla clientes
select 
count(nombre)
from clientes;