
-- Redondeo de valores en consultas de resumen
select 
    round(avg(edad))
from clientes;
-- Redondeo con decimales
select 
    floor(avg(edad))
from clientes;
-- Redondeo hacia arriba
select 
    ceil(avg(edad))
from clientes;