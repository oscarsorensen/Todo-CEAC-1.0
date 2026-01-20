<?php
$db = new PDO(
  "mysql:host=localhost;dbname=empresa2026;charset=utf8mb4",
  "empresa2026",
  "Empresa2026$"
);

$sql = "SELECT * FROM clientes";
$stmt = $db->query($sql);

foreach ($stmt as $row) {
  print_r($row);
}

$db = null;
