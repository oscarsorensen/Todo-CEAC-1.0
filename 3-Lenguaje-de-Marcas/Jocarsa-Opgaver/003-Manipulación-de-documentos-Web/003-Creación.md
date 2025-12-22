En esta tarea, practico cómo crear y modificar elementos HTML utilizando JavaScript. Practico trabajar con archivos JSON para generar botones y tablas, aplicar estilos básicos y gestionar eventos de clic, todo ello como parte de la creación de una interfaz web sencilla.

Cargo datos desde archivos JSON utilizando fetch y los convierto en objetos JavaScript. Desde botones.json, creo botones dinámicamente y los añado al menú de navegación. Desde tabla.json, genero una tabla HTML en la que cada fila y celda proviene de los datos JSON. También he añadido eventos al hacer clic en los botones para que aparezca un mensaje en la consola cuando se pulsan, y aplico estilos a la tabla para mostrar mejor los datos.

<!---1 Crea varios botones: -->
<!doctype html>
<html>
   <head>
   </head>
   <body>
       <nav></nav>
       <script>
           let botones = ['clientes','productos','pedidos'];
           let contenedor = document.querySelector("nav");
           botones.forEach(function(texto_boton){
           		let boton = document.createElement("button");
           		boton.textContent = texto_boton;
           		contenedor.appendChild(boton);
           })
       </script>
   </body>
</html>
Todo los botones funcionan igual, solo cambia el texto que aparece en ellos.

<!--- 2 Consumo de JSON:: -->

<!doctype html>
<html>
   <head>
   </head>
   <body>
       <nav></nav>
       <script>
           fetch("botones.json")
           .then(function(respuesta){
               return respuesta.json(); 
           })
           .then(function(datos){
           		let contenedor = document.querySelector("nav")
                datos.forEach(function(texto_boton){
                	let boton = document.createElement("button")
                    boton.textContent = texto_boton;
                    contenedor.appendChild(boton);
                })
           })
       </script>
   </body>
</html>

Carga el archivo JSON y crea dinámicamente los botones en el menú a partir de los datos contenidos en ese archivo.

<!--- 3 Recuperamos JSON y tabla: -->

<!doctype html>
<html>
   <head>
   </head>
   <body>
       <nav></nav>
       <script>
           fetch("tabla.json")
           .then(function(respuesta){
               return respuesta.json(); 
           })
           .then(function(datos){
               let contenedor = document.querySelector("body");
               let tabla = document.createElement("table");
               contenedor.appendChild(tabla); 
               datos.forEach(function(linea){
                   let fila = document.createElement("tr");
                   linea.forEach(function(celda){
                   		let data = document.createElement("td");
                       	data.textContent = celda
                       	fila.appendChild(data);
                   })
                   tabla.appendChild(fila)
               })
           })
       </script>
   </body>
</html>

Aqui cargamos el archivo JSON y crea una tabla HTML con los datos contenidos en ese archivo.

<!--- 4 Manejo de evento click: -->

<!doctype html>
<html>
   <head>
   </head>
   <body>
       <nav></nav>
       <script>
           let botones = ['clientes','productos','pedidos'];
           let contenedor = document.querySelector("nav");
           botones.forEach(function(texto_boton){
           		let boton = document.createElement("button");
           		boton.textContent = texto_boton;
           		contenedor.appendChild(boton);
               	boton.onclick = function(){
                	console.log("Has hecho click en el botón");
                }
           })
       </script>
   </body>
</html>

Asegurando que cada botón responde a un evento click, mostrando un mensaje en la consola cuando se hace clic en cualquiera de ellos.

<!--5 Estilo en la tabla:-->
<!-- 
<!doctype html>
<html>
   <head>
       <style>
           table{border:3px solid darkorange;border-collapse:collapse;background:white;}
           table tr:first-child{background:darkorange;color:white;}
           table tr td{padding:10px;border-right:1px solid goldenrod;}
       </style>
   </head>
   <body>
       <nav></nav>
       <script>
     
           fetch("tabla.json")
           .then(function(respuesta){
               return respuesta.json(); 
           })
           .then(function(datos){
               let contenedor = document.querySelector("body");       
               let tabla = document.createElement("table");         
               contenedor.appendChild(tabla);             
               datos.forEach(function(linea){
                   let fila = document.createElement("tr");        
                   linea.forEach(function(celda){                    
                   		let data = document.createElement("td");
    
                       	data.textContent = celda
                       	fila.appendChild(data);
                   })
                   tabla.appendChild(fila)
               })
           })
       </script>
   </body>
</html>
-->
Usando una tabla con estilos aplicados.

<!-- 6 & 7 Creación de interfaz base:-->

<!doctype html>
<html>
   <head>
       <meta charset="utf-8">
       <title>Panel de administración</title>
   </head>
   <body>
       <nav>Oscar Sorensen | panel</nav>
       <style>
           nav{display:flex;flex-direction:column;gap:20px;}
           nav button{border:none;background:white;color:indigo;padding:20px;
           text-transform:uppercase;}
       </style>
       <script>
           fetch("botones.json")
           .then(function(respuesta){
               return respuesta.json(); 
           })
           .then(function(datos){
           		let contenedor = document.querySelector("nav")
                datos.forEach(function(texto_boton){
                	let boton = document.createElement("button")
                    boton.textContent = texto_boton;
                    contenedor.appendChild(boton);
                })
           })
       </script>
       <main>Contenido de la tabla de clientes</main>
       <style>
        table{border:3px solid darkorange;border-collapse:collapse;background:white;}
        table tr:first-child{background:darkorange;color:white;}
        table tr td{padding:10px;border-right:1px solid goldenrod;}
    </style>
       <script>
           fetch("tabla.json")
           .then(function(respuesta){
               return respuesta.json(); 
           })
           .then(function(datos){

               let contenedor = document.querySelector("main");
               let tabla = document.createElement("table");
               contenedor.appendChild(tabla); 
               datos.forEach(function(linea){
                   let fila = document.createElement("tr");
                   linea.forEach(function(celda){
                   		let data = document.createElement("td");
                       	data.textContent = celda
                       	fila.appendChild(data);
                   })
                   tabla.appendChild(fila)
               })
           })
       </script>
   </body>
</html>
El código funcione correctamente y muestre el menú como parte de la interfaz.

<!-- Resumen: -->
En este ejercicio, practico cómo usar archivos JSON, crear elementos HTML dinámicamente, manejar eventos de clic y, al final, combino todas estas partes en una interfaz web básica pero funcional con un menú, botones y una tabla con estilo.