create database tienda_virtual;

use tienda_virtual;

create table clientes (
    id_cliente int primary key auto_increment,
    nombre varchar(100) not null,
    apellidos varchar(255) not null,
    email varchar(50) not null unique
);

create table pedido (
    id_pedido int primary key auto_increment,
    fecha_pedido datetime not null,
    id_cliente int
)

create table productos (
    id_producto int primary key auto_increment,
    nombre_producto varchar(255) not null
);

create table lineapedido (

    
)