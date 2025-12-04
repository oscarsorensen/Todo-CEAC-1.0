-- ===========================================================
-- UNIT: VIEWS AND USERS IN RELATIONAL DATABASES
-- ===========================================================

-- ===========================================================
-- 1. CONCEPT OF A VIEW
-- ===========================================================
-- A VIEW is a saved SQL query that behaves like a virtual table.
-- It does not store data physically; it displays results from a SELECT.
-- Views are useful to simplify complex queries and limit access to sensitive data.

-- CREATE a view:
CREATE VIEW people_emails AS
SELECT 
    persons.id,              -- person's unique identifier
    persons.name,
    persons.surname,
    emails.address           -- email address linked to that person
FROM emails
LEFT JOIN persons
ON emails.person = persons.id;

-- VERIFY that the view works:
SELECT * FROM people_emails;  -- The view behaves like a table

-- DELETE a view:
DROP VIEW people_emails;

-- NOTES:
-- - A view can combine multiple tables using JOIN.
-- - It saves only the query definition, not the data itself.
-- - It can protect data by showing only selected fields to users.

-- ===========================================================
-- 2. SHOWING USERS IN A MYSQL SYSTEM
-- ===========================================================
-- MySQL stores users in the internal table mysql.user.
-- To list all users in the system:

SELECT User, Host FROM mysql.user;   -- shows username and host
SELECT * FROM mysql.user;            -- shows full details (advanced)

-- ===========================================================
-- 3. CREATING A NEW USER
-- ===========================================================
-- Creates a new user called 'new_user' that can connect locally.
-- IMPORTANT: replace 'password123' with a secure password.

CREATE USER 'new_user'@'localhost' IDENTIFIED BY 'password123';

-- ===========================================================
-- 4. ASSIGNING PRIVILEGES TO A USER
-- ===========================================================
-- GRANT is used to give a user permission to access databases or tables.

-- Example: give full access to the database empresadam:
GRANT ALL PRIVILEGES ON empresadam.* TO 'new_user'@'localhost';

-- APPLY the changes so they take effect:
FLUSH PRIVILEGES;

-- ===========================================================
-- 5. KEY CONCEPTS TO REMEMBER FOR THE EXAM
-- ===========================================================
-- * VIEW: A stored SELECT query that acts like a virtual table.
-- * CREATE VIEW view_name AS SELECT ... ;
-- * SELECT FROM a view the same way as a table.
-- * DROP VIEW view_name; removes it.
-- * CREATE USER 'name'@'host' IDENTIFIED BY 'password';
-- * GRANT ALL PRIVILEGES ON database.* TO 'name'@'host';
-- * FLUSH PRIVILEGES; applies the permission changes.
-- * Views simplify complex queries.
-- * Users and privileges control security and data access in MySQL.
