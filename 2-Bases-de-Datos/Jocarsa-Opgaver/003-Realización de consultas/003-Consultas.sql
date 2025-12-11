
--Las funciones de redondeo en SQL permiten modificar los resultados numéricos directamente dentro de una consulta, lo que resulta útil para el análisis de datos y la generación de informes. En este ejercicio, utilizo la base de datos de mis clientes para calcular la edad media utilizando tres métodos de redondeo: ROUND(), FLOOR() y CEIL(). El objetivo es comparar cómo cada función transforma el mismo valor y, a continuación, visualizar los resultados con un sencillo gráfico circular de Python.
--La consulta SQL aplica las funciones ROUND(), FLOOR() y CEIL() a la media de la columna de edad. ROUND() devuelve el entero más cercano, FLOOR() redondea el valor hacia abajo y CEIL() lo redondea hacia arriba. Estas operaciones solo afectan al resultado. A continuación, utilizo los valores en un script de Python con matplotlib para generar un gráfico circular, en el que cada sección representa uno de los métodos de redondeo. Esto proporciona una comparación visual clara de cómo cada función modifica el mismo cálculo.

sudo mysql -u root -p

-- Realiza consultas con redondeo:
+---------------------+-----------------+---------------+
| promedio_redondeado | promedio_bajito | promedio_alto |
+---------------------+-----------------+---------------+
|                  33 |              33 |            34 |
+---------------------+-----------------+---------------+


--El gráfico circular muestra tres secciones que representan la edad media redondeada de tres formas diferentes. La media redondeada y la media mínima dan como resultado el valor 33, por lo que sus secciones parecen tener el mismo tamaño. La media máxima da como resultado 34, que es ligeramente mayor, por lo que esa porción ocupa una parte ligeramente mayor del gráfico. Esta visualización confirma que las funciones ROUND() y FLOOR() dan el mismo resultado (como debería ser), mientras que CEIL() aumenta el valor en uno.
--Utilicé el mismo proceso en una columna numérica de otra base de datos. Al calcular la media y luego aplicar ROUND(), FLOOR() y CEIL(), las diferencias entre cada método de redondeo se hacen visibles tanto en la salida SQL como en el gráfico.


--En este ejercicio muestro cómo utilizar las funciones de redondeo SQL para obtener resultados diferentes a partir del mismo valor numérico y cómo estas diferencias se hacen más evidentes cuando se visualizan. El uso de ROUND(), FLOOR() y CEIL() ayuda a comprender cómo se comporta el redondeo en el análisis práctico de datos. El mismo método se puede repetir con otros campos numéricos para explorar los efectos del redondeo en diferentes contextos. Puedo ver fácilmente cómo se puede utilizar esto en un escenario real, para mostrar datos.