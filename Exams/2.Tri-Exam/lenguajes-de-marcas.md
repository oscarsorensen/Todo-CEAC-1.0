Esta tarea está escrita originalmente en inglés y luego traducida al español. El texto original se encuentra debajo.
## 1.-Introducción breve y contextualización
Este examen de Lenguajes de Marcas forma parte de un examen más amplio, que incluye las asignaturas: Base de Datos, Lenguajes de Marcas, Programación y Proyecto Intermodular. En este examen voy a explicar cómo utilicé los lenguajes de marcas HTML, CSS y JavaScript, y qué papel tuvo cada uno dentro del proyecto general.

Un poco de contexto: este proyecto se basa en una base de datos como fundamento, y después se conecta con PHP, JavaScript, HTML y CSS. Es el primer proyecto que hemos hecho desarrollado como un proyecto de grupo real. Decidimos crear una mini aplicación donde se pueden reseñar películas, iniciar y cerrar sesión, y donde los administradores tienen la opción de crear y eliminar películas en un panel separado.

## 2 & 3.-Desarrollo detallado y preciso + Aplicación práctica
- Vistas, información y flujo del proyecto.
En el centro del proyecto está la página principal
(SCREENSHOT 1)

Aquí se pueden ver todas las películas que tenemos en el sitio de Chamitos Movie Club. Se puede hacer scroll hacia arriba y hacia abajo y ver aproximadamente las 30 películas que añadimos como prueba de concepto. Cada película muestra el título de la película, el director, la categoría, la fecha de estreno y una descripción básica. En el encabezado hay una barra de búsqueda, un botón de registro y un botón de inicio de sesión.
(SCREENSHOT 1.5)
(SCREENSHOT 2)
(SCREENSHOT 3)

Al hacer clic en el botón “Registrar”, se accede a una página de registro, donde se puede crear un usuario para el sitio web. Después de hacerlo, se redirige directamente a la página de perfil del usuario.

(SCREENSHOT 4)
Aquí se tiene una vista general de todas las películas que has reseñado. Estas películas se pueden volver a clicar para ir a la información de la película, que es la misma página a la que se puede acceder desde la página principal. También se puede cerrar sesión o volver a la página principal mediante la barra superior.

Al volver a la página principal, se puede ver que la barra superior ahora muestra “Perfil” y “Logout” en lugar de “Registrar” y “Login”. Esto ocurre porque usamos sesiones de PHP para comprobar si el usuario ha iniciado sesión y cambiar la interfaz según esos datos. Usamos la misma lógica cuando el usuario hace clic en una película y entra en la página de información de la película.

(SCREENSHOT 5)
Ahora que estás en la página de información de la película y has iniciado sesión, se puede ver que ya es posible escribir reseñas para las películas. Si no se hubiera iniciado sesión, aparecería un pequeño comentario indicando que hay que iniciar sesión para poder escribir reseñas.

Todo lo anterior está enfocado en el área frontend, es decir, lo que puede ver el usuario del sitio web, pero también tenemos un área backend, que es solo para administradores. Tenemos una separación muy clara entre las dos partes. El panel de administración se accede mediante un login y, si el inicio de sesión es correcto, se redirige a esta página, donde hay una lista de todas las películas del sitio.

(SCREENSHOT 6)
(SCREENSHOT 7)
Es fácil ver que el diseño de esta página es mucho más estricto. Aquí buscamos eficiencia, colores más neutros y un diseño que simplemente funcione. El backend no está hecho para impresionar, sino para funcionar. Al hacer clic en “Edit” en una película, se accede a una página donde se puede editar la película y cambiar lo que se quiera. Esto está conectado directamente con la base de datos, así que todos los cambios se guardan inmediatamente y después se muestran también en la página principal.

(SCREENSHOT 8)
Si se hace clic en el botón de la esquina inferior derecha en la página principal del panel de administración, se accede a una página similar a la de edición, pero completamente en blanco. Ahí es donde se pueden añadir nuevas películas. Todas las películas nuevas usan automáticamente una foto genérica elegida, hasta que se cambie manualmente en la base de datos. Esto es un pequeño fallo de diseño, pero es una forma en la que el proyecto podría mejorarse la próxima vez.

- Uso de HTML, CSS y JS, diferencias entre el primer y el segundo trimestre

Durante todo el proyecto utilizamos mucho HTML y CSS. El uso de JavaScript fue mucho menor en comparación, así que empiezo por ahí.

Usamos JavaScript solo en esta ocasión:

Aquí utilizamos JavaScript para hacer la función de búsqueda de películas en la primera página. Esto es bastante más avanzado que lo que hicimos en el primer trimestre. En el primer trimestre usamos `const`, pero `querySelector` es algo más del segundo trimestre. De esta forma usamos JavaScript como un lenguaje de scripting, como se supone que debe ser.

```
<script>
document.addEventListener("DOMContentLoaded", function () {


  // Live søgning (frontend filter)
  const buscador = document.getElementById("buscador");
  const peliculas = document.querySelectorAll(".movie-grid article");

  buscador.addEventListener("input", function () {
    const texto = this.value.toLowerCase().trim();

    peliculas.forEach(pelicula => {
      const tituloEl = pelicula.querySelector("h3 a") || pelicula.querySelector("h3");
      const titulo = (tituloEl ? tituloEl.innerText : "").toLowerCase();

      pelicula.style.display = titulo.includes(texto) ? "" : "none";
    });
  });

});
</script>

```

En cuanto a HTML y CSS, mientras lo hacíamos no pensábamos en si algo era “primer o segundo trimestre”. Gran parte del HTML es algo que podríamos haber hecho en el primer trimestre (al menos al final).

Por ejemplo, usando clases:

  <div class="centro">
    <input type="text" placeholder="Buscar" class="buscador" id="buscador">
  </div>

y luego estilizando esas clases:
.centro{
  flex: 1;
  display: flex;
  justify-content: center;
}

Pero algo claramente del segundo trimestre es el nivel de CSS que usamos para estilizar el frontend, que es con lo que interactúan los usuarios.

Este fragmento de CSS me llevó casi una hora conseguir que funcionara correctamente:
   :root{
    --bg: #111214;
    --surface: #17181b;
    --surface-2: #1e1f23;
    --text: rgba(255,255,255,0.92);
    --muted: rgba(255,255,255,0.68);
    --muted-2: rgba(255,255,255,0.55);
    --border: rgba(255,255,255,0.08);
    --shadow: 0 10px 30px rgba(0,0,0,0.45);
    --accent: #e50914;
    --accent-dark: #b20710;
    --radius: 14px;
  }


Ese es el “gradient” en la parte superior e inferior de la página principal. Eso no es algo que yo hubiera podido hacer en el primer trimestre. Antes de este proyecto ni siquiera había usado `:root`.

Otro ejemplo de CSS más avanzado es este:

/* link (todos los estados, sin morado/azul) */
.movie-grid article h3 a:link,
.movie-grid article h3 a:visited,
.movie-grid article h3 a:hover,
.movie-grid article h3 a:active{
  color: var(--text);
  text-decoration: none;
  display: inline-block;
  transition: transform 0.15s ease, color 0.15s ease;
}

La cuadrícula de películas actuaba de forma diferente cuando alguien hacía clic en una película: el enlace cambiaba a morado porque ya había sido visitado. Eso se desactivó con este fragmento de CSS.

Otro ejemplo de HTML simple que probablemente podríamos haber hecho en el primer trimestre es este:

<header>
  <div class="topbar">
    <h1>Chamitos Movie Club</h1>

    <div class="mainpa">
  <button class="inicio" type="button" id="btnBack">Main Page</button>
</div>

    <div class="estado-usuario">
      <?php if (isset($_SESSION['frontend_user'])): ?>
        Conectado como <strong><?= htmlspecialchars($_SESSION['frontend_user']) ?></strong>
      <?php else: ?>
        No has iniciado sesión
      <?php endif; ?>
    </div>
  </div>
</header>

Esto muestra una estructura de header muy estándar. Esto es de la parte `movie.php`. Se puede ver que es bastante estándar, y lo único que lo hace un poco más avanzado es que tiene tanto `class` como `id`.

## 4.-Conclusión breve

- Estilizar este proyecto ha sido el proceso de diseño más completo y complicado en el que he participado hasta ahora. Tener que pensar en la importancia de cada color y forma en relación con todo el sitio web, cómo se veía, si combinaba y si tenía sentido temáticamente, fue mucho más complicado de lo que pensaba al principio. A lo largo del proyecto aprendí a respetar más a los diseñadores gráficos, y también aprendí CSS más avanzado conforme se iba complicando y yo seguía pensando “también podría hacerlo así”. En general fue muy disfrutable.

- También me di cuenta de lo diferente que puede ser el frontend y el backend, porque tienen dos funciones completamente distintas que resolver. Aprendí que el CSS se puede usar para ocultar cosas y cambiar comportamientos, y aprendí qué funciona y qué no. También he llegado a apreciar mucho más el uso de `class` e `id`. La próxima vez me aseguraré de usarlos mejor desde el principio. En resumen, fue un proyecto muy bueno y me voy con la sensación de que esto es algo que puedo usar en mi trabajo futuro.


# #########################################################################################################################################

## 1.-Introducción breve y contextualización
This markup languages exam is a part of a broader exam, consisting of the subjects: Base de Datos, Lenguajes de Marcas, Programacion and Proyecto intermodular. In this exam i will explain how i used the markup languages HTML, CSS and JS and what role the different languages played in the overall assignment.

 A bit of contect: This project consists of a database as the groundwork, and then php, js, html and css. It is the first project that we have made that is developed as a proper group project. We choose to make a mini application where you can review movies, log in / out, and where the admins have the options to create and delete movies in a seperate panel


## 2 & 3.-Desarrollo detallado y preciso + Aplicación práctica
- views, information, flow of the project.
At the heart of the project you have the main page 
(SCREENSHOT 1)

here you can see all of the movies that we have on the Chamitos Movie Club site. You can scrool up and down the page and see the roughly 30 movies that we put there as a proof of concept. Each movie shows the title of the movie, the director, the category, the release date, and a basic description. In the header you have a seach bar, a registration button and a login button. 
(SCREENSHOT 1.5)
(SCREENSHOT 2)
(SCREENSHOT 3)

Clicking the registrear button you will be taken to a registration page, where you can make a user for the website. After you have done that you will be directly directed to your own profile page. 

(SCREENSHOT 4)
Here you have an overview of all movies that you have reviewed. These movies you can click again, to go the movie info, which is the same that can be accessed from the front page. You can also log out or go to the frontpage via the header bar. 
Going to the main page you will now notice that the header bar displays "Perfil" and "Logout" instead of registrar and login. This is because we use php sessions to check wether you are logged in, and change the interface depending on the data. We use the same logic when you now click a movie and goes to the movieinfo page. 

(SCREENSHOT 5)
Now that you are on the movieinfo page and logged in, you will notice that you can now write reviews for the movies. If you werent logged in there would be a little comment that about you having to log in to write reviews.


Now all of the above is focused on the frontend area, what the user of the website can see, but we also have a backend area, which is just for admins. We have a very clear seperation of the two. The admin panel is accessed with a login, and if the login are successfull, you are directed to this page- where you have a list of all of the movies on the site. 

(SCREENSHOT 6)
(SCREENSHOT 7)
It is easy to see that the design of this page is much more start. Here, we went for efficiency, colours that didnt allow a lot of play, and just worked. The backend isnt made to impress anyone, it is just supposed to work. Clicking edit on a movie, we wil be directed to a site where we can edit the movies and change what we want. This is of course dorectlyt connected to the database, so all changes are saved immedetely, and then displayed back on the main page.

(SCREENSHOT 8)
If you click on the botton in the bottom right corner on the main page of the admin panel, you will be directed to the same kind of site as the editing site, except this will be compltetely blank. This is where you can then add new movies. All new movies autimatically use specifically chosen stand-in foto, untill this is changed manually in the database, This is a bit of a design flaw, but is one way in which this project can be made better next time.

- Use of html, css and js, differences between first and second trimester

Throughout the project we used a lot of both html, and css. The use of Javascript was much smaller in comparison, so i will start with that. 

We used javascript only on this occasion:

Here,  we used javascript to make the seach function for the movies on the first page. This is quite a bit more advanced than what we did on our first trimester. In the first trimester we used const, but querySelector is a second trimester thing. In that way we used js as a scripting language, like it is supposed to be.

```
<script>
document.addEventListener("DOMContentLoaded", function () {


  // Live søgning (frontend filter)
  const buscador = document.getElementById("buscador");
  const peliculas = document.querySelectorAll(".movie-grid article");

  buscador.addEventListener("input", function () {
    const texto = this.value.toLowerCase().trim();

    peliculas.forEach(pelicula => {
      const tituloEl = pelicula.querySelector("h3 a") || pelicula.querySelector("h3");
      const titulo = (tituloEl ? tituloEl.innerText : "").toLowerCase();

      pelicula.style.display = titulo.includes(texto) ? "" : "none";
    });
  });

});
</script>

```

In regards to html and css, while we were doing it, we didnt think about if a thing was "first or second trimester". A lot of the html was something we could have done in first trimester (at least at the end of it).

Like using classes:

  <div class="centro">
    <input type="text" placeholder="Buscar" class="buscador" id="buscador">
  </div>

and then styling those classe:
.centro{
  flex: 1;
  display: flex;
  justify-content: center;
}

But a clear second trimester thing is the level of css we used to style the frontend, that the users interact with:

This piece of css took me almost an hour to get working correct:
   :root{
    --bg: #111214;
    --surface: #17181b;
    --surface-2: #1e1f23;
    --text: rgba(255,255,255,0.92);
    --muted: rgba(255,255,255,0.68);
    --muted-2: rgba(255,255,255,0.55);
    --border: rgba(255,255,255,0.08);
    --shadow: 0 10px 30px rgba(0,0,0,0.45);
    --accent: #e50914;
    --accent-dark: #b20710;
    --radius: 14px;
  }


That the is the gradient on the top and bottom of the front page. That is very much not something i could have done in the first trimester. Before this assignment i hadnt evener used :root before.

Another example of more advanced css is this:

/* link (alle states, ingen lilla/blå) */
.movie-grid article h3 a:link,
.movie-grid article h3 a:visited,
.movie-grid article h3 a:hover,
.movie-grid article h3 a:active{
  color: var(--text);
  text-decoration: none;
  display: inline-block;
  transition: transform 0.15s ease, color 0.15s ease;
}

The movie grid acted differently when someone has clicked one of the movies: the link changed to purple becuase it had been visited. That was also dissabled iwth this piece of css.

Another example of simple html that we probably could have done in the first trimester is this:

<header>
  <div class="topbar">
    <h1>Chamitos Movie Club</h1>

    <div class="mainpa">
  <button class="inicio" type="button" id="btnBack">Main Page</button>
</div>

    <div class="estado-usuario">
      <?php if (isset($_SESSION['frontend_user'])): ?>
        Conectado como <strong><?= htmlspecialchars($_SESSION['frontend_user']) ?></strong>
      <?php else: ?>
        No has iniciado sesión
      <?php endif; ?>
    </div>
  </div>
</header>

This shows a very standart header structure. This is from the movie.php part. You can see its very standart, with the only thing marking it as a bit more advanced is that it has both class and id. 


## 4.-Conclusión breve


- Styling this assignment was the most comprehensive and complicated design processes i have taken part of yet. Having to think about the significance of every colour and shape in regard to the whole website, how it looked, if it matched, if it made tematically sense, was much more complicated than i originally thought it would be. Thoughout the project i learned to more respect graphic designers, while i also learned more advanced css as it got gradually more advanced and i kept thinking "i could do it like this too". It was all very enjoyable.

- I also relized how different front and back can actually be, since they have two fundamentally different things to do and solve. I learned that css can be used to hide and change behaviour and i learned what works and what dont. I have also come to apprecitate classes and id´s much more. Next time i will be sure to use those better, from the start.  All in all it was a very good project and i walk away feeling like this is something i can use in my future work.