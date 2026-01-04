En este ejercicio trabajé con XML y practiqué cómo crear un esquema utilizando XSD para controlar la estructura de un documento XML. En este caso, el documento xml se llama testing.xml. Describe a una persona con nombre, apellidos y varios números de teléfono, y luego se asegura de que el XML siga reglas claras. Esto es útil en situaciones reales en las que es necesario validar y comprobar datos estructurados.

Creé/utilicé el archivo XML que me proporcionó la tarea, que representa a una persona, y luego creé un archivo XSD para definir su estructura. El esquema requiere el elemento persona y, dentro de él, los elementos nombre, apellidos y teléfonos. Dentro de teléfonos, el esquema permite uno o más elementos teléfono. Al final, vinculé el XML al XSD para que se pudiera validar correctamente; la tarea no lo pedía, pero es un paso lógico.


testing.XML
Cambiado a mi nombre, para personalizar
<?xml version="1.0" encoding="UTF-8"?>
<persona xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:noNamespaceSchemaLocation="Archivo.xsd">
<!-- connection a el archivo.xsd-->

  <nombre>Oscar </nombre>
  <apellidos>Sorensen</apellidos>
  <telefonos>
    <telefono>12738367</telefono>
    <telefono>12738368</telefono>
  </telefonos>
</persona>


Archivo.xsd
<?xml version="1.0" encoding="UTF-8"?>
<xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema">
  <xs:element name="persona">
    <xs:complexType>
      <xs:sequence>
        <xs:element name="nombre" type="xs:string"/>
        <xs:element name="apellidos" type="xs:string"/>
        <xs:element name="telefonos">
          <xs:complexType>
            <xs:sequence>
              <xs:element name="telefono" type="xs:string" maxOccurs="unbounded"/>
            </xs:sequence>
          </xs:complexType>
        </xs:element>
      </xs:sequence>
    </xs:complexType>
  </xs:element>
</xs:schema>

Este ejercicio me ayudó a comprender mejor cómo funciona la validación XML y cómo los esquemas ayudan a controlar la integridad y la calidad de los datos. También muestra cómo se pueden aplicar estos conocimientos en proyectos reales en los que los datos estructurados deben seguir formatos estrictos, lo que hace que la información sea más coherente y fácil de entender.