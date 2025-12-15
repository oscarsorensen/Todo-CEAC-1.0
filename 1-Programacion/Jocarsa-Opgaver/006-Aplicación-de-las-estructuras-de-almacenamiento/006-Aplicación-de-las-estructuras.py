#En este ejercicio, tengo un ejemplo sencillo relacionado con el gimnasio para practicar el manejo de excepciones. Calculo el doble de las repeticiones de ejercicios introducidas por los usuarios. Dado que los usuarios pueden introducir a veces valores no válidos, como palabras en lugar de números, el programa debe manejar estas situaciones correctamente sin bloquearse.
#Hago una lista llamada repeticiones que tiene valores numéricos y no numéricos. Defino una función llamada calculaDoble() que recorre esta lista. Para cada elemento, el programa intenta convertir el valor en un número entero utilizando un bloque try. Si la conversión se realiza correctamente, el programa imprime el doble del número. Si el valor no se puede convertir, se ejecuta el bloque except y el programa imprime el mensaje «Repetición no válida». Esto muestra el uso correcto de las listas y el manejo de excepciones con try y except.

repeticiones = [10, 20, "30", 40, "cinco"]

print(repeticiones)

def calculaDoble():
    for numero in repeticiones:
        try:
            numero = int(numero)
            print(numero * 2)
        except:
            print("Repetición no válida")

calculaDoble()

#Este ejercicio muestra cómo se puede utilizar el manejo de excepciones con listas para gestionar errores en situaciones de la vida real, como una entrada incorrecta del usuario en una aplicación de gimnasio. Al utilizar try y except, el programa sigue funcionando incluso cuando aparecen datos no válidos. Es importante comprender esto, y veo muchas situaciones de la vida real en las que resulta práctico.