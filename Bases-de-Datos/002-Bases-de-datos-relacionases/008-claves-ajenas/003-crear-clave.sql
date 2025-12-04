
alter table emails
modify column personas int;

alter table emails
add constraint fk_emails_personas
foreign key (personas) references personas(identificador)
on delete cascade
on update cascade;

alter table emails -- altera tabla emails
add constraint fk_emails_personas -- añade la restricción fk_emails_personas
foreign key (persona)  -- la columna persona de emails
references personas(identificador) -- clave foránea que referencia a personas(identificador)
on delete cascade -- si se borra una persona, se borran sus emails
on update cascade; -- si se actualiza el id de una persona, se actualizan sus emails

show tables; 
