En este ejercicio, crea una sencilla aplicación web Flask que simule una parte de un pequeño juego en el que los personajes se mueven aleatoriamente por la pantalla. Lo hago para practicar cómo controlar la posición, la dirección y la velocidad de diferentes objetos, y cómo actualizarlos dinámicamente para que el movimiento resulte más natural. En clase estuvimos hablando de videojuegos, y por eso acabamos haciendo esto.

Empiezo creando la clase Npc con atributos para la posición, el radio, la dirección y la velocidad. También incluyo un método de movimiento que cambia ligeramente la dirección cada vez y luego actualiza las coordenadas X e Y utilizando el coseno y el seno. A continuación, genero 8 (elijo el número 8 al azar, sin ningún motivo especial) caracteres con valores aleatorios y los guardo en una lista. Con Flask creo una ruta principal para cargar la página HTML y otra ruta llamada /api que mueve todos los caracteres y devuelve su información como JSON. En la página HTML utilizo JavaScript y jQuery para solicitar los datos regularmente y dibujar los caracteres en la pantalla para que se pueda ver el movimiento.

```
# ------------ 1 Definición de la clase base ------------

class Npc():
	def __init__(self, x, y,radio,direccion,velocidad): 
		self.posx = x
		self.posy = y
		self.radio = radio
		self.direccion = direccion 
		self.velocidad = velocidad 
    
    def to_dict(self):
		return {
      "posx": self.posx, 
      "posy": self.posy,
      "radio": self.radio,
    	"direccion": self.direccion 
    }
	def mover(self):
		self.direccion += (random.random() - 0.5) * 0.2
		self.posx += math.cos(self.direccion)*self.velocidad
		self.posy += math.sin(self.direccion)*self.velocidad 

# ------------ Paso 2: Implementar el movimiento aleatorio ------------

personajes = []
numero_personajes = 8

for i in range(0, numero_personajes):
	xaleatoria = random.randint(0, 750)
	yaleatoria = random.randint(0, 750)
	radioaleatorio = random.randint(10, 30)
	direccionaleatoria = random.random()*math.pi*2 
	velocidadaleatoria = random.random()*7 
	personajes.append(
    Npc(
      xaleatoria, 
      yaleatoria,
      radioaleatorio,
      direccionaleatoria,
      velocidadaleatoria 
    ) 
  )


# ------------ Paso 3: Preparar los personajes y lanzar la web ------------

import random
import json
from flask import Flask, render_template
import math

class Npc():
    def __init__(self, x, y, radio, direccion, velocidad):
        self.posx = x
        self.posy = y
        self.radio = radio
        self.direccion = direccion 
        self.velocidad = velocidad 

    def to_dict(self):
        return {
            "posx": self.posx, 
            "posy": self.posy,
            "radio": self.radio,
            "direccion": self.direccion 
        }

    def mover(self):
        # Aplicamos variacion de la direccion con el tiempo
        self.direccion += (random.random() - 0.5) * 0.2  
        self.posx += math.cos(self.direccion)*self.velocidad
        self.posy += math.sin(self.direccion)*self.velocidad 


personajes = []
numero_personajes = 8

for i in range(0, numero_personajes):
	xaleatoria = random.randint(0, 750)
	yaleatoria = random.randint(0, 750)
	radioaleatorio = random.randint(10, 30)
	direccionaleatoria = random.random()*math.pi*2 
	velocidadaleatoria = random.random()*7 
	personajes.append(
    Npc(
      xaleatoria, 
      yaleatoria,
      radioaleatorio,
      direccionaleatoria,
      velocidadaleatoria 
    ) 
  )

app = Flask(__name__)

@app.route("/")
def inicio():
    return render_template("juego.html")

@app.route("/api")
def api():
    # Primero muevo todos los personajes
    for personaje in personajes:	
        personaje.mover()
    personajes_json = [p.to_dict() for p in personajes]
    return json.dumps(personajes_json, indent=2)
  
if __name__ == "__main__":
    app.run(debug=True)

Normalmente uso port 8080, pero Flask por defecto usa el 5000, así que lo dejo así. Tambien la tarea especifica que uso 5000 mas tarde.

# ------------ Paso 4: Crear la página HTML ------------
- juego.html

<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Juego</title>
    <style>
        body {
            margin: 0;
            padding: 0;
            overflow: hidden;
            background-color: #f5f5f5;
        }
        .personaje {
            position: absolute;
            width: 20px;
            height: 20px;
            border-radius: 50%;
            background-color: red;
        }
    </style>
</head>
<body>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script>
    <script>
        $(document).ready(function() {
            function cargarPersonajes() {
                $.getJSON('/api', function(data) {
                    $('body').empty();
                    data.forEach(personaje => {
                        let personajeElement = $('<div>', {
                            class: 'personaje',
                            css: {
                                left: personaje.posx + 'px',
                                top: personaje.posy + 'px'
                            }
                        });
                        $('body').append(personajeElement);
                    });
                });
            }

            setInterval(cargarPersonajes, 1000);
        });
    </script>
</body>
</html>


# ------------ Paso 5: Ejecutar la aplicación ------------
Todo funciona correctamente. Cuando ejecuto la aplicación Flask y abro la página en el navegador, veo los "personajes" moviéndose aleatoriamente por la pantalla, actualizándose cada segundo.
```

Este ejercicio me ayudó a practicar cómo funcionan las aplicaciones reales y las simulaciones sencillas. Era la primera vez que veía cosas que se pueden usar directamente para videojuegos. Ahora puedo ver más claramente cómo la lógica de Python, Flask y JavaScript pueden trabajar juntas para actualizar información continuamente en una página web y cómo se puede usar esto. Fue una tarea muy práctica y muy útil para entender cómo se construyen sistemas dinámicos como los juegos o las visualizaciones interactivas. Lo disfruté mucho.