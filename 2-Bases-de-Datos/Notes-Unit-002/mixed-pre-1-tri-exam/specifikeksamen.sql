-- ============================
-- UNIVERSAL SQL EXAM TEMPLATE
-- Adapt by renaming keywords only
-- ============================
-- ==============================================================
-- HOW TO USE THIS TEMPLATE (EXAM INSTRUCTIONS)
-- ============================================================== 
-- 1) This file is a universal exam skeleton. 
--    You only need to rename the database and table names 
--    to fit the assignment (blog, journal, ads, etc.).
--
-- 2) Example replacements:
--      examdb    →  blog
--      category  →  autores / usuarios
--      item      →  entradas / publicaciones
--
-- 3) Steps this template already covers:
--    - Create database
--    - Create two related tables (1:N relationship)
--    - Define primary and foreign keys
--    - Example LEFT JOIN
--    - Create a view
--    - Create a user with permissions
--
-- 4) Optional: Run the INSERT examples to test your tables.
--    They can be deleted before submission.
--
-- 5) To adapt fast in exam:
--    a) Change names (Ctrl+H)
--    b) Execute the script section by section
--    c) Verify each part with:
--         SHOW TABLES;
--         DESCRIBE table_name;
--         SELECT * FROM view_name;
--
-- Ready for use with MySQL 8 (CEAC exam environment)
-- ==============================================================

-- 1) CREATE DATABASE
CREATE DATABASE IF NOT EXISTS examdb;
USE examdb;

-- 2) CREATE TABLES
CREATE TABLE IF NOT EXISTS category (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100)
);

CREATE TABLE IF NOT EXISTS item (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(150),
    category_id INT,
    date DATE,
    image VARCHAR(255),
    content TEXT,
    FOREIGN KEY (category_id) REFERENCES category(id)
);

-- 3) LEFT JOIN EXAMPLE
SELECT 
    item.id AS item_id,
    item.title,
    category.name AS category_name
FROM item
LEFT JOIN category
ON item.category_id = category.id;

-- 4) CREATE VIEW
CREATE OR REPLACE VIEW items_with_category AS
SELECT 
    item.title,
    item.date,
    category.name AS category_name
FROM item
LEFT JOIN category
ON item.category_id = category.id;

-- 5) CREATE USER WITH PERMISSIONS
CREATE USER IF NOT EXISTS 'exam_user'@'localhost' IDENTIFIED BY '1234';
GRANT SELECT, INSERT, UPDATE, DELETE ON examdb.* TO 'exam_user'@'localhost';
FLUSH PRIVILEGES;

-- 6) TEST DATA (optional for checking)
INSERT INTO category (name, email)
VALUES ('Oscar Sørensen', 'oscar@example.com'),
       ('José Vicente', 'jose@example.com');

INSERT INTO item (title, category_id, date, image, content)
VALUES ('First entry', 1, CURDATE(), 'example.jpg', 'Sample text.');
