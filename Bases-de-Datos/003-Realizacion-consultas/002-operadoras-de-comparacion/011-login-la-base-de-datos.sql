
sudo mysql -u root -p

use clientes;

select nombre 
from clientes;

select nombre, apellido,
edad+500
from clientes;

select nombre, apellido,
edad-500
from clientes;

select nombre, apellido,
edad*500
from clientes;

select nombre, apellido,
edad/500
from clientes;

select nombre, apellido,
edad < 30 as "es menor que 30?"
from clientes;