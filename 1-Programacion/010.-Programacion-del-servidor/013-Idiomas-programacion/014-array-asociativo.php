<?php

error_reporting(E_ALL & ~E_DEPRECATED); // Evitar advertencias de funciones obsoletas

$csv = array_map('str_getcsv', file('idiomas.csv'));
$header = array_shift($csv);

$idiomas = array_map(
    fn($row) => array_combine($header, $row),
    $csv
);

var_dump($idiomas);