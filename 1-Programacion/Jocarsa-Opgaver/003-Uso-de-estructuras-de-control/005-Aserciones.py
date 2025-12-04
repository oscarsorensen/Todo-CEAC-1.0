

En esta tarea, practico el uso de aserciones en Python como una forma de validar condiciones lógicas dentro de un programa.
Las aserciones actúan como puntos de control automáticos que verifican si ciertas reglas son ciertas antes de que el programa continúe ejecutándose.
Si una condición falla, Python detiene inmediatamente el programa y muestra un mensaje de error, lo que ayuda al desarrollador a detectar errores de forma temprana.
Con pequeños ejemplos relacionados con la edad, el peso y los niveles de experiencia de los jugadores, esta actividad demuestra cómo se pueden utilizar las aserciones para garantizar que los valores de los datos cumplan requisitos específicos.
Al aprender a utilizar assert, refuerzo mi comprensión de los mecanismos de control y validación en Python, mejorando tanto la fiabilidad como la calidad de mi código.


edad_usuario = 23; # Edad del usuario
assert edad_usuario >= 18, ("Debes ser mayor de edad para entrar") # Aserción: verifica si la edad es mayor o igual a 18
print("Puedes entrar al club") # Mensaje si la aserción es verdadera


peso_usuario = 70; # Peso del usuario en kg
assert peso_usuario >= 50, ("Debes pesar al menos 50 kg para cocinar conmigo") # Aserción: verifica si el peso es mayor o igual a 50
print("Puedes participar en la competencia") # Mensaje si la aserción es verdadera



nivel_jugador = 88; # Nivel del jugador en el juego
assert nivel_jugador >= 10, "No tienes suficiente nivel para continuar" # Aserción: verifica si el nivel es mayor o igual a 10
print("Puedes continuar el juego.") # Mensaje si la aserción es verdadera

En esta tarea, practiqué la validación de diferentes condiciones en Python, como la edad, el peso y el nivel de experiencia.
Estos pequeños programas me ayudaron a comprender cómo detener la ejecución cuando no se cumplen ciertos requisitos.
En la vida real, se puede utilizar una lógica similar para comprobar la información introducida por el usuario en las aplicaciones, por ejemplo, verificando la edad antes de crear una cuenta o confirmando la elegibilidad en un juego o una aplicación de fitness.