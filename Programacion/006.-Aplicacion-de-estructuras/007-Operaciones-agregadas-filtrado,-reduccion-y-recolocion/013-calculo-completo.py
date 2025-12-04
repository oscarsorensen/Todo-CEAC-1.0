import random
from flask import Flask, render_template

app = Flask(__name__)

PATRON = set(range(1, 10))  # {1,2,3,4,5,6,7,8,9}


def fila_valida(fila):
    """Comprueba que la fila contiene exactamente los números del 1 al 9."""
    return len(fila) == 9 and set(fila) == PATRON


def columnas_validas_parciales(sudoku):
    """
    Comprueba que, para el número de filas actual,
    ninguna columna tiene números repetidos.
    """
    num_filas = len(sudoku)
    num_columnas = 9

    for c in range(num_columnas):
        columna = [sudoku[f][c] for f in range(num_filas)]
        if len(columna) != len(set(columna)):  # hay repetidos
            return False
    return True


def sudoku_valido_completo(sudoku):
    """Validación final: todas las filas y todas las columnas son válidas."""
    # Filas
    for fila in sudoku:
        if not fila_valida(fila):
            return False

    # Columnas
    for c in range(9):
        columna = [sudoku[f][c] for f in range(9)]
        if set(columna) != PATRON:
            return False

    return True


@app.route("/")
def inicio():
    contador = 0
    sudoku = []

    # Construimos el sudoku fila a fila, probando al azar (fuerza bruta)
    while len(sudoku) < 9:
        contador += 1

        # Generamos una fila aleatoria que sea una permutación de 1..9
        fila = list(range(1, 10))
        random.shuffle(fila)

        # (opcional) evitamos repetir filas idénticas
        if fila in sudoku:
            continue

        # Comprobamos columnas con las filas que llevamos
        sudoku.append(fila)
        if not columnas_validas_parciales(sudoku):
            sudoku.pop()  # invalidamos esta fila y probamos otra

    # Comprobación final de seguridad (filas y columnas completas)
    es_valido = sudoku_valido_completo(sudoku)
    print(f"He necesitado, con fuerza bruta, {contador} intentos")
    print("¿Sudoku válido por filas y columnas?:", es_valido)

    return render_template("index.html", datos=sudoku)


if __name__ == "__main__":
    app.run(debug=True)