# Examen Intermodular — Mecánica y Preguntas

---

## ESPAÑOL

---

### Qué se evalúa

En todo momento se habla de vuestro **proyecto intermodular**:

- **Bases de datos** — cómo vuestro proyecto ha guardado los datos
- **Lenguajes de marcas** — cómo habéis construido las interfaces de vuestras aplicaciones
- **Programación** — los controladores que unen las interfaces de usuario con los datos
- **Proyecto intermodular** — el sentido que tiene todo y cómo lo habéis unido

---

### Cómo funciona

Cada alumno creará un documento de Google Drive con una plantilla proporcionada por el profesor (la plantilla tendrá preguntas). Se comparte la plantilla en tiempo real y el profesor la descarga progresivamente.

---

### Metodología

- No se pueden traer los textos preparados; deben redactarse durante el examen
- Sí se permite traer una **escaleta**
- Se puede tener el proyecto y el código a la vista
- La extensión de las respuestas debe ser proporcional a la duración del examen
  - *Ejemplo: 5 preguntas en 90 minutos = máximo 18 minutos por pregunta*
- Cada pregunta incluye una **minirúbrica** con cuatro puntos:
  1. Introducción
  2. El código
  3. El global
  4. Conclusión

> En todo momento hay que hablar de **vuestro proyecto**, no del sexo de los ángeles.

---

## Preguntas — Lenguajes de Marcas

---

### Pregunta 1 — Análisis estructural del proyecto

En tu proyecto, identifica qué lenguajes de marcas utilizas o podrías utilizar (por ejemplo HTML, XML, JSON u otros) y explica:

- qué función cumple cada uno
- qué ventajas aporta frente a otros formatos
- cómo está estructurado uno de tus documentos
- qué normas sintácticas deben cumplirse para que sea correcto
- por qué es importante que esté bien formado

> El alumno debe hablar de estructura, sintaxis, etiquetas, jerarquía y posibles espacios de nombres si aparecen.

---

### Pregunta 2 — Publicación web y presentación de información

Describe cómo se presenta la información en la parte web de tu proyecto:

- estructura general del documento HTML
- etiquetas principales utilizadas
- organización semántica de la página
- hojas de estilo aplicadas
- ventajas de separar contenido y presentación
- cómo validarías técnicamente el resultado

> Deben relacionar HTML + CSS con su propio proyecto real.

---

### Pregunta 3 — Manipulación dinámica en cliente

Explica qué operaciones dinámicas realiza tu proyecto en el navegador mediante JavaScript o lenguaje de script de cliente:

- selección de elementos del DOM
- modificación de contenido
- creación o eliminación de nodos
- respuesta a eventos
- cambios visuales aplicados dinámicamente

> Deben hablar de comportamiento real del proyecto, no de teoría abstracta.

---

### Pregunta 4 — Validación de documentos e intercambio estructurado

Si tu proyecto necesitara intercambiar información estructurada con otro sistema, explica:

- qué formato elegirías
- cómo definirías sus reglas de validación
- qué tecnología usarías para describir su estructura
- cómo garantizarías que los documentos generados sean válidos

> Aquí pueden aparecer XML Schema, DTD, JSON Schema, etc.

---

### Pregunta 5 — Conversión de documentos

Describe una conversión de información que exista o pueda existir en tu proyecto:

- origen de los datos
- formato de entrada
- formato de salida
- necesidad de la transformación
- herramienta o lenguaje usado
- ventajas obtenidas

> Ejemplos: CSV → JSON, XML → HTML, base de datos → informe.

---

### Pregunta 6 — Gestión de datos en formatos de intercambio

Explica cómo se almacenan y se intercambian los datos en tu proyecto:

- si utilizas JSON, XML, CSV u otros formatos
- ventajas e inconvenientes del formato elegido
- relación con bases de datos
- consultas realizadas
- generación de documentos a partir de datos almacenados

> Deben conectar base de datos + exportación + APIs.

---

### Pregunta 7 — Integración con sistemas empresariales o externos

Indica si tu proyecto se comunica con otros sistemas o podría hacerlo, explicando:

- importación o exportación de información
- integración con plataformas externas
- mecanismos de autenticación o seguridad
- generación de informes
- utilidad empresarial de esa integración

> Muy útil para proyectos que usan APIs, Moodle, ERP, CRM, etc.

---

## Preguntas — Bases de Datos

---

### Pregunta 1 — Elección del sistema de base de datos en tu proyecto

Analiza qué sistema de almacenamiento de información utiliza tu proyecto y justifica por qué has elegido ese modelo:

- qué tipo de base de datos utilizas (relacional, documental, otra)
- qué sistema gestor empleas
- qué ventajas ofrece frente a otras alternativas
- qué papel cumple cada elemento principal del gestor
- qué implicaciones tendría usar una base distribuida o un sistema orientado a Big Data en tu caso

> El alumno debe conectar teoría con una decisión real del proyecto.

---

### Pregunta 2 — Diseño físico de la base de datos

Describe cómo has construido la estructura de la base de datos de tu proyecto:

- tablas creadas
- relaciones entre ellas
- tipos de datos elegidos
- claves primarias y foráneas
- restricciones de integridad
- vistas si existen
- gestión de usuarios o permisos si procede

> Deben justificar diseño técnico real.

---

### Pregunta 3 — Consultas SQL en el proyecto

Explica qué consultas realizas en tu proyecto para recuperar información y muestra ejemplos de distintos niveles de complejidad:

- consultas simples
- consultas con varias tablas
- consultas resumen
- subconsultas si existen
- medidas adoptadas para optimizar rendimiento

> Muy importante que hablen de consultas reales de su aplicación.

---

### Pregunta 4 — Modificación de datos y mantenimiento de integridad

Describe cómo se insertan, actualizan y eliminan datos en tu proyecto:

- operaciones habituales de alta, modificación y borrado
- validaciones realizadas
- uso de transacciones si existen
- problemas de concurrencia posibles
- medidas para mantener consistencia

> Aquí se evalúa madurez en operaciones CRUD.

---

### Pregunta 5 — Automatización dentro del gestor de base de datos

Indica si en tu proyecto has automatizado tareas dentro de la base de datos o cómo lo harías:

- procedimientos almacenados
- funciones
- triggers
- eventos programados
- cursores
- automatizaciones equivalentes

Debes justificar qué utilidad aportan.

> Aunque no lo tengan implementado, deben saber plantearlo.

---

### Pregunta 6 — Modelo relacional y normalización

Explica el modelo relacional de tu proyecto partiendo de sus entidades principales:

- tablas derivadas del análisis
- relaciones entre ellas
- claves
- normalización aplicada
- dependencias eliminadas
- restricciones que no pueden resolverse solo con el diseño lógico

> Muy importante aquí que razonen diseño.

---

### Pregunta 7 — Uso o posible integración de bases de datos no relacionales

Valora si alguna parte de tu proyecto podría beneficiarse de una base de datos no relacional:

- qué tipo de base NoSQL sería adecuada
- qué información almacenarías ahí
- ventajas e inconvenientes frente al modelo actual
- ejemplos de uso real

> Esto obliga a pensamiento arquitectónico moderno.

---

## Preguntas — Programación

---

### Pregunta 1 — Estructura general del programa

Describe la estructura general de tu programa y explica cómo está organizado el código fuente:

- bloques principales del programa
- variables utilizadas y su tipado
- constantes definidas
- operadores más empleados
- conversiones de tipo necesarias
- criterios de organización del código

> Aquí se evalúa si comprenden la arquitectura básica de su propio código.

---

### Pregunta 2 — Primer nivel de orientación a objetos

Explica qué clases y objetos básicos aparecen en tu proyecto y cómo utilizas la programación orientada a objetos:

- clases utilizadas
- objetos instanciados
- métodos invocados
- constructores
- librerías empleadas
- relación entre objetos

> Deben conectar teoría OOP con código real.

---

### Pregunta 3 — Estructuras de control y depuración

Analiza qué estructuras de control aparecen en tu proyecto y justifica su uso:

- decisiones condicionales
- bucles
- control de errores
- excepciones
- depuración realizada
- problemas encontrados durante el desarrollo

> Muy útil para detectar comprensión real del flujo del programa.

---

### Pregunta 4 — Diseño completo en clases

Explica cómo has organizado tu proyecto en clases:

- clases creadas
- propiedades
- métodos
- encapsulación
- visibilidad
- herencia si existe
- reutilización de código

> Aquí se evalúa diseño orientado a objetos maduro.

---

### Pregunta 5 — Entrada y salida de información

Describe cómo entra y sale la información en tu aplicación:

- entrada por consola, formulario o interfaz
- salida mostrada al usuario
- lectura o escritura de ficheros
- eventos de interfaz si existen
- formatos utilizados

> Muy aplicable a cualquier proyecto real.

---

### Pregunta 6 — Uso de estructuras de datos avanzadas

Explica qué estructuras de datos utilizas en tu proyecto para manejar información:

- arrays o listas
- colecciones
- recorridos
- almacenamiento temporal
- uso de expresiones regulares si procede
- ventajas de la estructura elegida

> Aquí se detecta madurez algorítmica.

---

### Pregunta 7 — Características avanzadas de orientación a objetos

Indica si en tu proyecto existen relaciones de herencia, composición o uso de interfaces:

- jerarquías de clases
- sobrescritura de métodos
- composición entre objetos
- ventajas frente a otras soluciones
- criterio de diseño utilizado

> Muy importante para evaluar arquitectura real.

---

### Pregunta 8 — Persistencia de objetos

Explica cómo mantienes persistente la información de tu proyecto:

- serialización
- almacenamiento de objetos
- transformación a JSON/XML
- uso de bases de datos orientadas a objetos o equivalentes
- recuperación posterior de datos

> Aunque no usen BDOO pura, permite evaluar persistencia moderna.

---

### Pregunta 9 — Programación con bases de datos

Describe cómo se conecta tu aplicación con una base de datos y qué operaciones realiza:

- tipo de conexión utilizada
- consultas realizadas
- inserciones
- modificaciones
- borrados
- medidas de integridad aplicadas

> Esta pregunta conecta programación + persistencia real.

---

## Preguntas — Proyecto Intermodular

---

### Pregunta 1 — Relación del proyecto con una empresa real del sector

Sitúa tu proyecto dentro de una empresa tipo del sector tecnológico o digital y explica:

- qué tipo de empresa podría desarrollar o comercializar una solución como la tuya
- qué productos o servicios ofrecería esa empresa
- qué departamentos tendría
- qué recursos humanos y materiales serían necesarios
- con qué Objetivos de Desarrollo Sostenible se relaciona tu propuesta

> Aquí deben demostrar visión empresarial, no solo técnica.

---

### Pregunta 2 — Necesidad real que resuelve el proyecto

Explica qué necesidad real intenta resolver tu proyecto y por qué tendría sentido en el mercado actual:

- problema detectado
- usuario o cliente objetivo
- comparación con soluciones existentes
- elemento innovador aportado
- viabilidad técnica general

> Muy útil para medir si comprenden el valor real de lo que han construido.

---

### Pregunta 3 — Proyecto como posible spin-off o iniciativa emprendedora

Imagina que tu proyecto se convierte en una pequeña empresa propia. Describe:

- nombre y actividad de esa empresa
- organización interna
- propuesta diferencial frente a otras empresas
- tecnologías empleadas
- posibles mejoras futuras para hacerlo competitivo

> Esto obliga a pensar como desarrollador-emprendedor.

---

### Pregunta 4 — Planificación real del desarrollo realizado

Explica cómo has organizado el desarrollo de tu proyecto desde el inicio hasta el estado actual:

- fases de trabajo
- orden seguido
- recursos utilizados
- dificultades encontradas
- riesgos detectados
- cómo los has resuelto

> Aquí aparece planificación real, no teórica.

---

### Pregunta 5 — Presentación profesional y seguimiento del proyecto

Explica cómo presentarías tu proyecto ante un posible cliente o responsable técnico:

- idea principal en pocos minutos
- partes fundamentales
- resultados obtenidos
- estado actual
- mejoras pendientes
- cómo comprobarías que el proyecto cumple sus objetivos

> Esta pregunta mide madurez comunicativa y capacidad profesional.

---
---

## ENGLISH #######################################################################################################################

---

### What is being assessed

At all times you are talking about **your intermodular project**:

- **Databases** — how your project stores data
- **Markup languages** — how you built the interfaces of your applications
- **Programming** — the controllers connecting the user interfaces with the data
- **Intermodular project** — the overall purpose and how you brought it all together

---

### How it works

Each student creates a Google Drive document using a template provided by the teacher (the template contains the questions). The document is shared in real time and the teacher downloads it progressively.

---

### Methodology

- You cannot bring prepared texts to the exam; they must be written during the exam
- You are allowed to bring an **outline/escaleta**
- You may have your project and code visible
- The length of answers must be proportional to the duration of the exam
  - *Example: 5 questions in 90 minutes = maximum 18 minutes per question*
- Each question includes a **mini-rubric** with four points:
  1. Introduction
  2. The code
  3. The global picture
  4. Conclusion

> At all times you must talk about **your project**, not abstract theory.

---

## Questions — Markup Languages

---

### Question 1 — Structural analysis of the project

In your project, identify which markup languages you use or could use (e.g. HTML, XML, JSON or others) and explain:

- what function each one serves
- what advantages it offers over other formats
- how one of your documents is structured
- what syntactic rules must be followed for it to be correct
- why it is important that it is well-formed

> Students should discuss structure, syntax, tags, hierarchy, and possible namespaces if present.

---

### Question 2 — Web publishing and information presentation

Describe how information is presented in the web-facing part of your project:

- general structure of the HTML document
- main tags used
- semantic organisation of the page
- stylesheets applied
- advantages of separating content from presentation
- how you would technically validate the result

> Students must connect HTML + CSS to their own real project.

---

### Question 3 — Dynamic client-side manipulation

Explain what dynamic operations your project performs in the browser using JavaScript or a client-side scripting language:

- selecting DOM elements
- modifying content
- creating or removing nodes
- responding to events
- visual changes applied dynamically

> Students must talk about real behaviour in the project, not abstract theory.

---

### Question 4 — Document validation and structured data exchange

If your project needed to exchange structured information with another system, explain:

- which format you would choose
- how you would define its validation rules
- which technology you would use to describe its structure
- how you would guarantee that the generated documents are valid

> This is where XML Schema, DTD, JSON Schema, etc. may appear.

---

### Question 5 — Document conversion

Describe a data conversion that exists or could exist in your project:

- origin of the data
- input format
- output format
- reason for the transformation
- tool or language used
- advantages gained

> Examples: CSV → JSON, XML → HTML, database → report.

---

### Question 6 — Data management in interchange formats

Explain how data is stored and exchanged in your project:

- whether you use JSON, XML, CSV or other formats
- advantages and disadvantages of the chosen format
- relationship with databases
- queries performed
- generation of documents from stored data

> Students must connect database + export + APIs.

---

### Question 7 — Integration with enterprise or external systems

State whether your project communicates with other systems or could do so, explaining:

- import or export of information
- integration with external platforms
- authentication or security mechanisms
- report generation
- business value of that integration

> Particularly relevant for projects using APIs, Moodle, ERP, CRM, etc.

---

## Questions — Databases

---

### Question 1 — Choice of database system in your project

Analyse what information storage system your project uses and justify why you chose that model:

- what type of database you use (relational, document-based, other)
- which database management system you use
- what advantages it offers over other alternatives
- what role each main component of the system plays
- what the implications would be of using a distributed database or Big Data system in your case

> Students must connect theory to a real decision made in the project.

---

### Question 2 — Physical database design

Describe how you built the structure of your project's database:

- tables created
- relationships between them
- data types chosen
- primary and foreign keys
- integrity constraints
- views if any exist
- user management or permissions if applicable

> Students must justify real technical design decisions.

---

### Question 3 — SQL queries in the project

Explain what queries your project uses to retrieve information, and show examples at different levels of complexity:

- simple queries
- multi-table queries
- aggregate queries
- subqueries if any exist
- measures taken to optimise performance

> It is very important that students talk about real queries from their application.

---

### Question 4 — Data modification and integrity maintenance

Describe how data is inserted, updated, and deleted in your project:

- common create, update, and delete operations
- validations performed
- use of transactions if any
- possible concurrency issues
- measures taken to maintain consistency

> This question assesses maturity in CRUD operations.

---

### Question 5 — Automation within the database management system

State whether you have automated tasks inside the database in your project, or explain how you would do so:

- stored procedures
- functions
- triggers
- scheduled events
- cursors
- equivalent automations

You must justify what value each brings.

> Even if not implemented, students must be able to reason through it.

---

### Question 6 — Relational model and normalisation

Explain the relational model of your project starting from its main entities:

- tables derived from analysis
- relationships between them
- keys
- normalisation applied
- dependencies eliminated
- constraints that cannot be resolved through logical design alone

> It is very important that students reason through the design here.

---

### Question 7 — Use or possible integration of non-relational databases

Assess whether any part of your project could benefit from a non-relational database:

- what type of NoSQL database would be appropriate
- what information you would store there
- advantages and disadvantages compared to the current model
- real-world usage examples

> This requires modern architectural thinking.

---

## Questions — Programming

---

### Question 1 — General program structure

Describe the general structure of your program and explain how the source code is organised:

- main blocks of the program
- variables used and their types
- constants defined
- most commonly used operators
- type conversions needed
- criteria used to organise the code

> This assesses whether students understand the basic architecture of their own code.

---

### Question 2 — First level of object-oriented programming

Explain what basic classes and objects appear in your project and how you apply object-oriented programming:

- classes used
- objects instantiated
- methods invoked
- constructors
- libraries used
- relationships between objects

> Students must connect OOP theory to real code.

---

### Question 3 — Control structures and debugging

Analyse what control structures appear in your project and justify their use:

- conditional decisions
- loops
- error handling
- exceptions
- debugging performed
- problems encountered during development

> Very useful for detecting real understanding of program flow.

---

### Question 4 — Full class-based design

Explain how you have organised your project into classes:

- classes created
- properties
- methods
- encapsulation
- visibility
- inheritance if present
- code reuse

> This assesses mature object-oriented design.

---

### Question 5 — Input and output of information

Describe how information enters and exits your application:

- input via console, form, or interface
- output shown to the user
- reading or writing of files
- interface events if any
- formats used

> Applicable to any real project.

---

### Question 6 — Use of advanced data structures

Explain what data structures you use in your project to handle information:

- arrays or lists
- collections
- traversal operations
- temporary storage
- use of regular expressions if applicable
- advantages of the chosen structure

> This detects algorithmic maturity.

---

### Question 7 — Advanced object-oriented features

State whether your project includes inheritance, composition, or the use of interfaces:

- class hierarchies
- method overriding
- composition between objects
- advantages over other solutions
- design criteria used

> Very important for evaluating real architecture.

---

### Question 8 — Object persistence

Explain how you keep the information in your project persistent:

- serialisation
- object storage
- transformation to JSON/XML
- use of object-oriented databases or equivalents
- subsequent data retrieval

> Even without pure OODBMS, this allows evaluation of modern persistence.

---

### Question 9 — Programming with databases

Describe how your application connects to a database and what operations it performs:

- type of connection used
- queries performed
- insertions
- updates
- deletions
- integrity measures applied

> This question connects programming + real persistence.

---

## Questions — Intermodular Project

---

### Question 1 — Relation of the project to a real company in the sector

Place your project within a typical company in the technology or digital sector and explain:

- what type of company could develop or commercialise a solution like yours
- what products or services that company would offer
- what departments it would have
- what human and material resources would be needed
- which Sustainable Development Goals your proposal relates to

> Students must demonstrate business vision, not just technical knowledge.

---

### Question 2 — Real need the project addresses

Explain what real need your project tries to solve and why it would make sense in today's market:

- problem identified
- target user or customer
- comparison with existing solutions
- innovative element introduced
- general technical feasibility

> Very useful for assessing whether students understand the real value of what they have built.

---

### Question 3 — Project as a possible spin-off or entrepreneurial initiative

Imagine your project becomes a small company of your own. Describe:

- name and activity of that company
- internal organisation
- differentiating proposition compared to other companies
- technologies used
- possible future improvements to make it competitive

> This requires thinking as a developer-entrepreneur.

---

### Question 4 — Real planning of the development carried out

Explain how you organised the development of your project from start to its current state:

- phases of work
- order followed
- resources used
- difficulties encountered
- risks identified
- how you resolved them

> This reveals real planning, not theoretical.

---

### Question 5 — Professional presentation and project follow-up

Explain how you would present your project to a potential client or technical manager:

- main idea in a few minutes
- core components
- results obtained
- current state
- pending improvements
- how you would verify that the project meets its objectives

> This question measures communicative maturity and professional capability.
