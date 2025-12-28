
#En este ejercicio, vuelvo a trabajar con la herencia y el polimorfismo en Python. Utilizo un ejemplo de gimnasio. Tengo una clase principal Persona y luego creo otra clase que la extiende, para no repetir código. Ambas comparten nombre y apellidos, pero el socio del gimnasio también tiene edad, por lo que la herencia ayuda a estructurar esto mejor. Esto es exactamente lo que aprendimos en clase sobre cómo reutilizar el código de una manera más inteligente.
#Primero, creo la clase Persona con los atributos nombre y apellidos, y un método dameDatos() que devuelve el nombre completo. Luego creo la clase MiembroGimnasio, que hereda de Persona y añade un nuevo atributo: edad. Sobrescribo el método dameDatos() para que ahora muestre el nombre completo y la edad juntos. Esto funciona porque Python elige el dameDatos() más reciente. A continuación, creo los objetos (en este caso, yo y Juan) e imprimo sus datos utilizando dameDatos.

# ------------ 1 Definición de la clase base ------------

class Persona():
  def __init__(self,nombre,apellidos):
    self.nombre = nombre
    self.apellidos = apellidos

  def dameDatos(self):
    return self.nombre+" "+self.apellidos


# ------------ 2 Herencia y polimorfismo ------------

class MiembroGimnasio(Persona):
  def __init__(self,nombre,apellidos,edad):
    super().__init__(nombre, apellidos)
    self.edad = edad

  def dameDatos(self):
    return "Miembro de gimnasio:"+self.nombre+" "+self.apellidos+"; Edad:"+str(self.edad) # Sobrescribo el otro dameDatos


# ------------ 3 Instanciación y uso ------------

persona1 = Persona("Oscar","Sorensen")
print(persona1.dameDatos())

miembro1 = MiembroGimnasio("Juan","Garcia",30)
print(miembro1.dameDatos())

#Este ejercicio me ayudó a practicar cómo la herencia me permite reutilizar código en lugar de escribir lo mismo otra vez. Al sobrescribir el método, puedo cambiar el comportamiento de una nueva clase sin romper la original. Puedo ver cómo esto es útil en sistemas reales, como la gestión de muchos miembros de un gimnasio con información compartida y diferente.