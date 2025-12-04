sudo mysql -u root -p

create database clientes;
use clientes;
create table clientes(
    nombre varchar(255),
    apellido varchar(255),
    edad int

)