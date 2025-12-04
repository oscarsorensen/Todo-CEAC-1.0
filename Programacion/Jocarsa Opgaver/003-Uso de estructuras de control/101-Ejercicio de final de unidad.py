#En este ejercicio desarrollo un programa en Python llamado adivina.py, cuyo objetivo es crear un juego interactivo de adivinanza.
#El programa genera un número secreto entre 1 y 50 utilizando el módulo random y permite al usuario intentar descubrirlo en un máximo de seis intentos.
#Durante el proceso se aplican estructuras condicionales (if/elif/else), bucles while, manejo de errores con try/except, control de flujo con break y continue, y el uso de aserciones para garantizar condiciones invariantes.



import random

def guess_the_number():
    print("Welcome to the Guess the Number Game! You have 6 attempts to guess the secret number between 1 and 50.")
    secret_number = random.randint(1, 50)
    max_attempts = 6
    used_attempts = 0
    print("Debug: The secret number is", secret_number)  # For testing purposes, remove in production
    assert 1 <= secret_number <= 50, "Secret number is out of bounds!"

    while used_attempts < max_attempts:
        try: 
            entry = input("Attempt " + str(used_attempts + 1) + ": Enter your guess: ")
            guess = int(entry)
            
            if guess < 1 or guess > 50:
                print("Your guess must be between 1 and 50. Please try again.")
                continue

            used_attempts += 1

            if guess == secret_number:
                print("Congratulations! You've guessed the secret number:", secret_number)
                break   
            elif guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            
            if used_attempts == 3 and guess != secret_number:
                print("Hint: The secret number is", "even." if secret_number % 2 == 0 else "odd.")
                
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
    if used_attempts == max_attempts:
        print("Sorry, you've used all your attempts. The secret number was:", secret_number)

if __name__ == "__main__":
    guess_the_number()


#Este programa demuestra cómo combinar estructuras de control, validación de datos y manejo de excepciones en un contexto práctico y lúdico.
#Las aserciones garantizan que el número secreto y el contador de intentos se mantengan dentro de los límites establecidos, mientras que el uso de try/except evita errores por entradas no numéricas.
#Gracias a esta implementación, se cumple el objetivo de crear un juego funcional que refuerza los fundamentos de la programación estructurada en Python.