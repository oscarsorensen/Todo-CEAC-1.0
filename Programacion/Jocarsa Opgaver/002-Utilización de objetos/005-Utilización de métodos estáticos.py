#En mi tiempo libre, disfruto mucho entrenando en el gimnasio y cocinando comidas saludables.
#Para combinar estos intereses, imagino desarrollar una pequeña aplicación de fitness que ayude a los usuarios a realizar un seguimiento de sus rutinas de entrenamiento.
#En este ejercicio, crearé un método estático que calcule la puntuación de un entrenamiento en función del número de series y repeticiones realizadas.
#Este ejemplo conecta con mis actividades personales en el gimnasio y muestra cómo se puede utilizar la programación para organizar y analizar los datos de entrenamiento de manera eficiente.

#El siguiente código define una clase llamada Entrenamiento que incluye dos propiedades estáticas:

#max_repeticiones: almacena el número máximo de repeticiones permitidas.

#factor_calidad: almacena un factor de calidad que aumenta la puntuación si las repeticiones superan el límite.

#La clase también contiene un método estático llamado calcular_calificacion, que recibe dos parámetros (series y repeticiones) y devuelve una puntuación calculada en función de los criterios dados.


class Entrenamiento:
    max_repeticiones = 18
    factor_calidad = 1.5

    @staticmethod
    def calcular_calificacion(series, repeticiones):
        if repeticiones < Entrenamiento.max_repeticiones:
            return series * repeticiones
        else:
            return (series * repeticiones) + Entrenamiento.factor_calidad

if __name__ == "__main__":
    calificacion = Entrenamiento.calcular_calificacion(4, 20)
    print("Calificación del entrenamiento:", calificacion)  # Output: Calificación del entrenamiento: 81.5

#Este ejercicio muestra cómo se pueden utilizar los métodos estáticos para agrupar operaciones lógicas dentro de una clase sin necesidad de crear objetos.
#Comprender este concepto es fundamental en la programación orientada a objetos, ya que los miembros estáticos nos permiten almacenar datos compartidos o métodos de utilidad que pertenecen a la propia clase.
#En proyectos reales, este mismo enfoque podría utilizarse para tareas como el cálculo de calorías, la puntuación de la intensidad del entrenamiento o el seguimiento del progreso, aspectos esenciales de una aplicación de seguimiento del estado físico.

