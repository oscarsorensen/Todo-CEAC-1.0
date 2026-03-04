<?php

$inicio = microtime(true);

$numero = 1.0000000432;

for ($contador = 0; $contador <= 235324543; $contador++) {
    $numero = $numero * 1.00000000645;
}

$fin = microtime(true);

echo "El resultado es: $numero\n";
echo "Tiempo de ejecucion: " . number_format($fin - $inicio, 6) . " segundos\n";
