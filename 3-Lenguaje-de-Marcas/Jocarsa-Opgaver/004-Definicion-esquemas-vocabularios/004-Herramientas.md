En este ejercicio volví a trabajar con XML y XSD para describir un documento estructurado y asegurarme de que la información siguiera unas reglas claras. Utilicé mis propios datos personales para rellenar el archivo XML y luego creé (amplié el de clase) un esquema XSD para controlar su estructura. Esto es similar a situaciones reales en las que las aplicaciones necesitan intercambiar datos personales o profesionales.

 Completé el documento XML con la información de mi currículum y luego creé el archivo XSD para definir su estructura. El esquema describe el elemento principal del currículum, contiene datos personales con todos sus campos correspondientes y define el resto de las secciones del currículum a continuación. Para que la validación funcionara correctamente y para que la tarea fuera más fácil de resolver, ajusté el esquema para que las secciones opcionales no fueran obligatorias, lo que simplificó todo. Después de esto, el XML se valida correctamente con el XSD.

# ---------- 002-curriculum.xml rellenado ----------
<?xml version="1.0" encoding="UTF-8"?>
<curriculum xmlns="https://ejemplo.com/curriculum"
            version="1.0">
    <datosPersonales>
        <nombre>Oscar</nombre>
        <apellidos>Sjorensen</apellidos>
        <fechaNacimiento>2000-11-08</fechaNacimiento> <!--making sure the date is in the correct forma. This tricked me the first time.-->
        <nacionalidad>Danes</nacionalidad>
        <email>oscar@gmail.com</email>
        <telefono>12345679</telefono>
        <webPersonal>https://oscarsorensen.com</webPersonal>
        <linkedin>oscarslinkedin</linkedin>
        <direccion>
            <calle>Madrid</calle>
            <codigoPostal>46789</codigoPostal>
            <ciudad>Valencia</ciudad>
            <pais>España</pais>
        </direccion>
    </datosPersonales>
    </curriculum>


# ---------- 002-curriculum.xsd ----------

<xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema" 
           targetNamespace="https://ejemplo.com/curriculum" 
           xmlns="https://ejemplo.com/curriculum">
    <xs:element name="curriculum">
        <xs:complexType>
            <xs:sequence>
                <xs:element ref="datosPersonales"/>

                <xs:element ref="perfilProfesional" minOccurs="0"/>
                <xs:element ref="experienciaProfesional" minOccurs="0"/>
                <xs:element ref="formacionAcademica" minOccurs="0"/>
                <xs:element ref="publicaciones" minOccurs="0"/>
                <xs:element ref="proyectosDestacados" minOccurs="0"/>
                <xs:element ref="competencias" minOccurs="0"/>
                <xs:element ref="idiomas" minOccurs="0"/>
                <xs:element ref="otrosDatos" minOccurs="0"/>
            </xs:sequence>

            <xs:attribute name="version" type="xs:string" use="required"/>
        </xs:complexType>
    </xs:element>
    <xs:element name="datosPersonales">
        <xs:complexType>
            <xs:sequence>
                <xs:element name="nombre" type="xs:string"/>
                <xs:element name="apellidos" type="xs:string"/>
                <xs:element name="fechaNacimiento" type="xs:date"/>
                <xs:element name="nacionalidad" type="xs:string"/>
                <xs:element name="email" type="xs:string"/>
                <xs:element name="telefono" type="xs:string"/>
                <xs:element name="webPersonal" type="xs:string"/>
                <xs:element name="linkedin" type="xs:string"/>

                <xs:element name="direccion">
                    <xs:complexType>
                        <xs:sequence>
                            <xs:element name="calle" type="xs:string"/>
                            <xs:element name="codigoPostal" type="xs:string"/>
                            <xs:element name="ciudad" type="xs:string"/>
                            <xs:element name="pais" type="xs:string"/>
                        </xs:sequence>
                    </xs:complexType>
                </xs:element>

            </xs:sequence>
        </xs:complexType>
    </xs:element>

    <xs:element name="perfilProfesional" type="xs:string"/>
    <xs:element name="experienciaProfesional">
        <xs:complexType>
            <xs:sequence>
                <xs:element name="experiencia" type="xs:string" maxOccurs="unbounded"/>
            </xs:sequence>
        </xs:complexType>
    </xs:element>

    <xs:element name="formacionAcademica">
        <xs:complexType>
            <xs:sequence>
                <xs:element name="formacion" type="xs:string" maxOccurs="unbounded"/>
            </xs:sequence>
        </xs:complexType>
    </xs:element>

    <xs:element name="publicaciones">
        <xs:complexType>
            <xs:sequence>
                <xs:element name="publicacion" type="xs:string" maxOccurs="unbounded"/>
            </xs:sequence>
        </xs:complexType>
    </xs:element>
    <xs:element name="proyectosDestacados">
        <xs:complexType>
            <xs:sequence>
                <xs:element name="proyecto" type="xs:string" maxOccurs="unbounded"/>
            </xs:sequence>
        </xs:complexType>
    </xs:element>

    <xs:element name="competencias">
        <xs:complexType>
            <xs:sequence>
                <xs:element name="competencia" type="xs:string" maxOccurs="unbounded"/>
            </xs:sequence>
        </xs:complexType>
    </xs:element>
    <xs:element name="idiomas">
        <xs:complexType>
            <xs:sequence>
                <xs:element name="idioma" type="xs:string" maxOccurs="unbounded"/>
            </xs:sequence>
        </xs:complexType>
    </xs:element>

    <xs:element name="otrosDatos" type="xs:string"/>

</xs:schema>


# ---------- Mi XML con el XSD: ----------
    
    xmllint --noout --schema 002-curriculum.xsd 002-curriculum.xml
- no veo ningun salida.


Este ejercicio me ayudó a comprender mejor cómo los esquemas XML controlan la estructura y la calidad de los datos. También muestra cómo se utiliza esto en proyectos reales, por ejemplo, cuando los sistemas comparten CV, currículums o cualquier información estructurada.