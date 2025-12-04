

--To Enter SQL

sudo mysql -u root -p


| Command                                     | Purpose                           | Example                                |
| ------------------------------------------- | --------------------------------- | -------------------------------------- |
| `CREATE DATABASE empresadam;`               | Creates a new database            | Defines a place to store tables        |
| `USE empresadam;`                           | Selects the active database       | Tells MySQL which database to work in  |
| `CREATE TABLE productos (...);`             | Creates a new table               | Defines the columns and their types    |
| `ALTER TABLE productos ADD CONSTRAINT ...;` | Adds new rules to a table         | You added checks like `precio >= 0`    |
| `INSERT INTO productos (...) VALUES (...);` | Inserts new data rows             | Adds real product records              |
| `SELECT * FROM productos;`                  | Reads and displays all rows       | Shows the data inside the table        |
| `DELETE FROM productos;`                    | Removes all rows                  | Clears the table                       |
| `DESCRIBE productos;`                       | Shows table structure             | Lets you confirm data types and keys   |
| `SHOW TABLES;`                              | Lists all tables in your database | Used to check what exists              |
| `SHOW CREATE TABLE productos;`              | Shows the full SQL definition     | Useful for verifying constraints       |
| `DROP CONSTRAINT ...`                       | Removes a constraint              | Used when renaming or replacing checks |
