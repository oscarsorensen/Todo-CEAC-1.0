
--create
insert into clientes values(
    null,
    'Oscar Sorensen',
    'Sjorman',
    'oscar@gmail.com'
);
-- read
select * from clientes;
--update
update clientes
set email = 'info@oscarsorensen.com'
where Identificador = 1;
--delete
delete from clientes
where Identificador = 1;