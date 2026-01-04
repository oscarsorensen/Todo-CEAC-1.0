XML es un lenguaje de marcado que se utiliza para almacenar y organizar datos. Se creó para facilitar el intercambio de información entre sistemas. XML es similar al HTML porque ambos utilizan etiquetas, pero mientras que el HTML se utiliza para mostrar contenido en una página web, el XML se utiliza para describir y guardar datos. Por ello, el XML es útil para describir texto y documentos estructurados en lenguajes de marcas.


--Varius telefonos:
<?xml version="1.0" encoding="UTF-8"?>
<persona>
  <nombre>Oscar Sorensen</nombre>
  <apellidos>Sjorman</apellidos>
  <telefonos>
    <telefono>12345567</telefono>
    <telefono>6534646</telefono>
    
  </telefonos>
</persona>
--

--Subetiquetas:
<?xml version="1.0" encoding="UTF-8"?>
<persona>
  <nombre>Oscar Sorensen</nombre>
  <apellidos>Sjorman</apellidos>
</persona>
--

--Etiqueta raiz:
<?xml version="1.0" encoding="UTF-8"?>
<persona>
  
</persona>
--
-- Case sensitive:
<?xml version="1.0" encoding="UTF-8"?>
<persona>
  
</Persona>
Esto está mal
--



<?xml version="1.0" encoding="UTF-8"?>
<persona id="1">
  <nombre>Oscar</nombre>
  <apellidos>Sorensen</apellidos>
  <edad>25</edad>
  <telefonos>
    <telefono tipo="movil">12345678</telefono>
    <telefono tipo="trabajo">87654321</telefono>
  </telefonos>
</persona>



Esta práctica me ayudó a comprender cómo funciona XML y por qué sus reglas son importantes. Al crear diferentes ejemplos, aprendí a estructurar datos correctamente utilizando elementos, subelementos y atributos. Este conocimiento me será útil en futuros proyectos en los que necesite definir datos estructurados, esquemas o vocabularios en lenguajes de marcado.