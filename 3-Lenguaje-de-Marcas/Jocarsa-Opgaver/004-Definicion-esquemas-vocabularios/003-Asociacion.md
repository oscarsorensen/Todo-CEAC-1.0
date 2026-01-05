En este ejercicio trabajé con dos archivos XML y XSD de clase para practicar la validación de datos. El objetivo del ejercicio era comprobar si un documento XML seguía las reglas definidas en su esquema XSD, tal y como se supone que debe hacer. Esto resulta útil en situaciones reales en las que los sistemas intercambian datos y es importante asegurarse de que la estructura es correcta.

Utilicé Python junto con la biblioteca lxml. Cargué el archivo XML y el archivo XSD utilizando etree.parse(), y luego creé un objeto de esquema con etree.XMLSchema(). Finalmente, validé el XML utilizando schema.validate(xml_doc), que devuelve True cuando el XML coincide con las reglas del esquema. Después de corregir los nombres de las etiquetas (apellido/s) y hacer coincidir el esquema, la validación devolvió True.

```
# ---------- 001 ----------
001-documento de referencia.xml
<?xml version="1.0" encoding="UTF-8"?>
<persona>
  <nombre>Oscar</nombre>
  <apellido>Sorensen</apellido>
  <telefonos>
    <telefono>12345567</telefono>
    <telefono>6534646</telefono>
  </telefonos>
</persona>

# ---------- 002 ----------
002-esquema.xsd
<?xml version="1.0" encoding="UTF-8"?>
<xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema" elementFormDefault="qualified">

  <xs:element name="persona">
    <xs:complexType>
      <xs:sequence>
        <xs:element name="nombre" type="xs:string"/>
        <xs:element name="apellido" type="xs:string"/> //Here i changed apellidos to apellido
        <xs:element name="telefonos">
          <xs:complexType>
            <xs:sequence>
              <xs:element name="telefono" type="xs:string" minOccurs="1" maxOccurs="unbounded"/>
            </xs:sequence>
          </xs:complexType>
        </xs:element>
      </xs:sequence>
    </xs:complexType>
  </xs:element>

</xs:schema>

# ---------- 003 ----------
003-validacion.py
/#pip3 install lxml --break-system-packages

from lxml import etree

xml_doc = etree.parse("001-documento de referencia.xml")
xsd_doc = etree.parse("002-esquema.xsd")

schema = etree.XMLSchema(xsd_doc)

print(schema.validate(xml_doc))

# ---------- resultado ----------
True
```

Este ejercicio me ayudó a comprender mejor cómo funciona la validación XML y por qué los esquemas son importantes para garantizar la calidad de los datos. También muestra cómo lo que aprendemos se puede utilizar en proyectos reales, por ejemplo, cuando diferentes aplicaciones comparten archivos XML y necesitan asegurarse de que la información sea correcta y esté bien estructurada. José Vicente comentó que esto es algo muy importante en el ámbito laboral y que sin duda necesitamos saberlo en la vida real, así que me aseguré de comprenderlo bien.