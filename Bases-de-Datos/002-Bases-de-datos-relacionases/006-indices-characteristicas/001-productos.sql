

create table "clientes" (
    "Identificador" integer,
    "nombre" text,
    "apellidos",
    "email",
    primary key("Identificador" AUTOINCREMENT)
);

create table "productos" (
    "Identificador" integer,
    "nombre" text,
    "description" text,
    "precio" text,
    primary key("Identificador" AUTOINCREMENT)
);