
#En este ejercicio trabajo con diccionarios y listas para almacenar información de una persona. El objetivo es practicar cómo organizar datos de forma estructurada, como hemos aprendido en clase. Es muy útil en programación real.

#Creo un diccionario llamado persona con nombre, apellidos, correo, edad y una lista de teléfonos, donde cada teléfono es otro diccionario. Después imprimo todo el diccionario para comprobar que los datos se guardan correctamente y veo al teléfono fijo y imprimelo .
persona = {
	"nombre":"Jose Vicente",
  "apellidos":"Carratalá Sanchis",
  "correo":"info@jocarsa.com",
  "edad":47,
  "telefonos":[
  	{	
      "tipo":"fijo",
    	"número":96123455
    },
    {	
      "tipo":"movil",
    	"número":65456546
    }
  ]
}

print(persona)
print(persona["telefonos"][0]["número"])

# Output:
"""{'nombre': 'Jose Vicente', 'apellidos': 'Carratalá Sanchis', 'correo': 'info@jocarsa.com', 'edad': 47, 'telefonos': [{'tipo': 'fijo', 'número': 96123455}, {'tipo': 'movil', 'número': 65456546}]}
96123455
"""

#Este ejercicio me ayuda a entender mejor cómo usar diccionarios y listas para guardar información organizada. Estas técnicas son importantes porque se usan en muchos proyectos reales.