sudo mysql -u root -p

create database ejemploclaves;

use ejemploclaves;

--crear tabla personas
CREATE TABLE personas (
  nombre VARCHAR(50),
  apellidos VARCHAR(255)
);


-- añado identificador

alter table
add column identificador int auto_increment primary key first;


 ---crear tabla emails
 create table emails(
    direccion varchar(50)
    persona varchar(255)
 );

show tables;



