const inicio = Date.now();

let numero = 1.0000000432;

for (let contador = 0; contador <= 235324543; contador++) {
    numero = numero * 1.00000000645;
}

const fin = Date.now();

console.log(`El resultado es: ${numero}`);
console.log(`Tiempo de ejecucion: ${((fin - inicio) / 1000).toFixed(6)} segundos`);
