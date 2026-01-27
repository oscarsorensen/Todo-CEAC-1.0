<?php

error_reporting(E_ALL & ~E_DEPRECATED);
$rows = array_map('str_getcsv', file('idiomas.csv'));

var_dump($rows);

?>

