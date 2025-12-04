

CREATE USER 'new_user'@'localhost' IDENTIFIED BY 'password123';

grant usage on *.* to 'new_user'@'localhost' identified by 'password123';

alter user 'new_user'@'localhost' identified by 'new_password456';
require none
with max_queries_per_hour 0
max_connections_per_hour 0
max_updates_per_hour 0
max_user_connections 0;

grant all privileges on clientes.*
to 'new_user'@'localhost';