#En este ejercicio, trabajo con clases y herencia para modelar personas en un sistema escolar. Se supone que debo crear una clase Persona principal y reutilizarla en diferentes subclases en lugar de repetir el código. Esto permite que todos los tipos utilicen atributos compartidos como el nombre, el correo electrónico y la dirección. Muestra cómo la herencia ayuda a estructurar la información en programas reales. Es mucho más eficiente que lo que he estado haciendo antes.
#Primero creo la clase Persona con atributos para nombre, apellido, correo electrónico y dirección, además de un método dameDatos que devuelve toda esta información. A continuación, creo las clases Profesor y Alumno, que heredan de Persona. Después, añado AlumnoOnline y AlumnoPresencial, ambas heredadas de Alumno. Por último, creo un objeto de cada clase e imprimo sus datos utilizando dameDatos, siguiendo los ejemplos de la clase.

# ------------ 1-5, Clases, Subclases, Metodos ------------

class Persona(): #Clase base
  def __init__(self,nombre,apellidos,email,direccion):
    self.nombre = nombre
    self.apellidos = apellidos
    self.email = email
    self.direccion = direccion

  def dameDatos(self):
    return self.nombre+" "+self.apellidos+" - "+self.email+" - "+self.direccion #Metodo que devuelve todoslos datos de la persona

class Profesor(Persona): #Clase Profesor herededa de Persona
  def __init__(self,nombre,apellidos,email,direccion):
    super().__init__(nombre, apellidos, email,direccion)
  
class Alumno(Persona): # Clase Alumno herededa de Persona
  def __init__(self,nombre,apellidos,email,direccion):
    super().__init__(nombre, apellidos, email,direccion)

class Alumno_Online(Alumno):
  def __init__(self,nombre,apellidos,email,direccion):
    super().__init__(nombre, apellidos, email,direccion)

class Alumno_Presencial(Alumno):
  def __init__(self,nombre,apellidos,email,direccion):
    super().__init__(nombre, apellidos, email,direccion)


# ------------ 6 Instanciación y uso------------

alumno1 = Alumno("Oscar","Sorensen","info@oscar.com","Direccion")
print(alumno1.dameDatos())

profesor1 = Profesor("Juan","Garcia","juan@jocarsa.com","Direccion")
print(profesor1.dameDatos())

alumno_Online1 = Alumno_Online("Ana","Lopez","ana@email.com","Direccion")
print(alumno_Online1.dameDatos())

alumno_Presencial1 = Alumno_Presencial("Luis","Martinez","luis@email.com","Direccion")
print(alumno_Presencial1.dameDatos())

#Este ejercicio muestra cómo la herencia me permite reutilizar código y mantener los programas organizados. En lugar de reescribir la misma estructura, las subclases amplían lo que ya existe. Puedo ver claramente cómo este enfoque ayuda en programas más grandes en los que muchos usuarios comparten características comunes. Se conecta bien con la unidad porque aplica conceptos orientados a objetos de una manera sencilla y práctica.