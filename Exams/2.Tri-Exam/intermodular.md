# Proyecto intermodular - Examen Trimestral, 2

- Este trabajo está escrito originalmente en inglés y posteriormente traducido al español con ChatGPT.
- Oscar Sorensen, DAW, 14/1/2026

---

Este examen de Proyecto Intermodular forma parte de un examen más amplio, que incluye las siguientes asignaturas: Base de Datos, Lenguajes de Marcas, Programacion, y Proyecto Intermodular. En este examen explicaré el proyecto Chamitos Movie Club desde una perspectiva global: por qué elegimos este tema, qué necesidad resuelve, cómo funciona el proyecto pantalla por pantalla, y cómo combinamos todo lo que hemos aprendido durante el curso en una aplicación completa.

Un poco de contexto: este es el primer proyecto real en grupo que hemos desarrollado, y nuestro objetivo fue crear una mini aplicación web donde los usuarios puedan explorar películas, registrarse e iniciar sesión, escribir reseñas, y donde los administradores puedan gestionar el catálogo de películas en un panel backend separado.

Elegí estar en un grupo con Bryan y Carlos, ya que son dos de mis buenos amigos aquí en clase, y sé que ambos son buenos trabajadores y programadores. Juntos, elegimos crear una web de películas. Nuestra inspiración fue LetterBoxd, un lugar donde puedes reseñar, leer reseñas, tener un usuario y una biblioteca de películas que has reseñado. Esto resolvería nuestra necesidad de tener un LetterBoxd privado, que pueda organizar películas, reseñas y permitirnos compartirlas con nuestros amigos.


Cuando empezamos el proyecto, todavía no habíamos dividido las diferentes partes para decidir quién debía hacer qué, porque estábamos muy al inicio del proyecto. En realidad empezamos simplemente hablando sobre nuestro proyecto, qué debía incluir y qué no. Luego dibujamos una base de datos aproximada con tablas, creamos un proyecto en GitHub y poco a poco empezamos a ver qué debía ir en cada sitio. 

Ahora, incluso con las mejores intenciones, fue ahí cuando empezamos a tener algunos problemas, no por falta de ganas, sino porque seguimos siendo 3 personas diferentes en 3 etapas diferentes de convertirnos en programadores. Personalmente, ya había usado GitHub y Git bastante, y por eso entiendo GitHub. Rápidamente quedó claro que mis compañeros no. Tuvimos algunos problemas con carpetas, duplicados, y ramas que no eran compatibles. Por desgracia, esto me llevó bastantes horas de limpieza. No porque el trabajo fuera malo, sino porque no encajaba en la estructura en absoluto: la estructura que yo ya había hecho, organizado y explicado a mis compañeros.

Después de resolver esto, el resto del proyecto fue más fluido. Decidimos que yo haría la base de datos, la estructura y todo el PHP, y que Carlos y Bryan harían el HTML y el CSS, es decir, el diseño. Elegí PHP como un pequeño reto. Hemos aprendido que es lo que usan muchas páginas web (aunque aparentemente no sea lo mejor), y pensé que sería una buena práctica para el futuro.

Pasé unos días al inicio de las vacaciones haciendo que mi parte funcionara más o menos como estaba previsto. Cuando llegamos a Navidad, teníamos una web completamente funcional, aunque básica. Por desgracia, aquí volvimos a tener los mismos problemas con el flujo de Git y las versiones, lo que de nuevo terminó conmigo pasando unas horas limpiándolo antes de que fuera utilizable.

Luego decidimos repartir el trabajo restante de otra forma. Cada persona tendría ciertos archivos en los que trabajar, sin tocar nada más. Esto debía ser posible porque el proyecto ya funcionaba. Lo único que quedaba en ese momento era el diseño. Esto funcionó mucho mejor, y Bryan hizo las páginas de login y registro con un diseño muy bonito. Yo terminé haciendo el resto. Así que el trabajo final quedó dividido así:

Oscar: DB, estructura, PHP, limpieza de Git  
Bryan: diseño de login/registro  
Carlos: diseño



- El flujo del proyecto funciona de la siguiente manera:

En el centro del proyecto tenemos la página principal.
(SCREENSHOT 1)

Aquí el usuario puede ver el catálogo completo de películas de Chamitos Movie Club. Puedes hacer scroll por la página y ver alrededor de 30 películas que añadimos como prueba de concepto. Cada tarjeta de película muestra el título, el director, la categoría, la fecha de estreno y una breve descripción. En el header también hay una barra de búsqueda y botones para registro e inicio de sesión.
(SCREENSHOT 1.5)
(SCREENSHOT 2)
(SCREENSHOT 3)

Si haces clic en el botón “Registrar”, vas a la página de registro donde puedes crear una cuenta. Después de registrarse, el usuario es redirigido automáticamente a su página de perfil.
(SCREENSHOT 4)

En la página de perfil puedes ver un resumen de todas las películas que has reseñado. Desde ahí puedes volver a hacer clic en una película para ir a la página de detalle, que es la misma página a la que se puede acceder desde el catálogo principal. También puedes cerrar sesión o volver a la página principal usando la navegación del header.

Después de iniciar sesión, la interfaz cambia: en lugar de “Registrar” y “Login”, el header muestra “Perfil” y “Logout”. Esto ocurre porque usamos sesiones en PHP para comprobar si el usuario está logueado, y luego mostramos diferentes opciones dependiendo de los datos de la sesión. Usamos la misma lógica también en la página de detalle de película. Esta fue una decisión de diseño crítica y una de las cosas más importantes con las que luchamos para hacerlo bien: ¿cómo podíamos asegurarnos de que fuera fácil ver si estabas logueado o no? ¿y cómo podíamos asegurarnos de que vieras cosas diferentes y tuvieras opciones diferentes?
(SCREENSHOT 5)

En la página de detalle de película, cuando el usuario está logueado, puede escribir reseñas para la película. Si el usuario no está logueado, la página muestra un mensaje diciendo que debe iniciar sesión antes de poder publicar una reseña.

Todo lo anterior forma parte del frontend, que es lo que los usuarios normales del sitio pueden ver e interactuar. Pero el proyecto también incluye un área de administración backend, que es solo para administradores. Mantuvimos una separación muy clara entre frontend y admin, porque tienen objetivos diferentes: el frontend es para navegar e interactuar, mientras que el área admin es para gestionar el catálogo, algo que el usuario normal no debería poder hacer.

El panel de administración se accede mediante un login, y después de un inicio de sesión correcto el admin es redirigido a un dashboard donde puede ver una lista de todas las películas almacenadas en la base de datos.
(SCREENSHOT 6)
(SCREENSHOT 7)

El diseño del área admin es mucho más estricto y simple. Aquí nos enfocamos en eficiencia y claridad en lugar de estilo visual. El backend no está hecho para impresionar al usuario, está hecho para funcionar de forma fiable y hacer fácil la gestión de los datos.

Desde la lista del admin, el administrador puede hacer clic en “Edit” en una película, lo que abre una página donde la información de la película se puede actualizar. Como las acciones del admin están conectadas directamente con la base de datos, todos los cambios se guardan inmediatamente y luego se reflejan también en el catálogo del frontend.
(SCREENSHOT 8)

Finalmente, el admin también tiene la opción de añadir nuevas películas. Esto abre un formulario en blanco donde el admin puede crear una nueva película. Las nuevas películas usan automáticamente una imagen placeholder hasta que la imagen se cambie manualmente en la base de datos. Esta es una pequeña limitación de diseño en la versión actual, pero también es una de las mejoras que podríamos implementar en la siguiente iteración del proyecto.



- Technologies

En cuanto a las tecnologías, elegimos MySQL/SQL como base de datos porque necesitábamos una forma de guardar toda la información de manera permanente. En el próximo proyecto lo haremos diferente, porque técnicamente terminamos con 3 bases de datos locales, lo cual fue un poco desordenado si alguien tenía que cambiar algo. La base de datos incluía usuarios, películas, categorías y reseñas. Usar una base de datos real (aunque local) también hizo que el proyecto se sintiera mucho más realista, porque la web no son solo páginas estáticas, sino una aplicación dinámica donde el contenido viene directamente de los datos. Y al final todo terminó funcionando.

Usamos PHP como el lenguaje controlador principal, primero por el reto, pero también porque encaja muy bien con un proyecto web y porque conecta todo. PHP maneja la lógica del proyecto: selecciona películas de la base de datos, las muestra en las páginas, gestiona login/logout con sesiones, y se asegura de que solo los usuarios logueados puedan escribir reseñas (estábamos muy orgullosos de cómo terminó funcionando eso). PHP también se usa para el panel admin, donde los administradores pueden crear, editar y eliminar películas. De esa forma, PHP es el verdadero corazón del proyecto. Conecta la base de datos y la interfaz.

Para la interfaz y el estilo usamos HTML y CSS, porque es lo que hemos aprendido en Lenguajes de Marcas y es el núcleo de cómo se ve y funciona la web. HTML da la estructura de las páginas (headers, tarjetas de películas, formularios, botones) y el CSS avanzado que acabamos usando es lo que hace que el proyecto se sienta como una web moderna real en lugar de un ejercicio escolar simple. Pasamos mucho tiempo en el diseño, especialmente en el frontend, porque queríamos que el sitio fuera claro, fácil de usar y visualmente consistente. Funcionó muy bien, pero ahora que el proyecto está terminado, ya veo muchas formas de mejorarlo.

También usamos una pequeña cantidad de JavaScript, principalmente para mejorar la experiencia de usuario en la página principal. La barra de búsqueda en vivo filtra películas al instante sin recargar la página, lo que hace que el catálogo sea más rápido y fácil de navegar. También es elegante porque no necesita conectarse a la base de datos. Es una funcionalidad pequeña, pero muestra cómo podemos combinar diferentes tecnologías para hacer el proyecto más interactivo y vivo.

En general, la combinación de MySQL + PHP + HTML/CSS/JS funciona muy bien porque cada tecnología tiene un rol claro que no podría haber sido asumido por otra. No veo una forma en la que este proyecto pudiera funcionar sin una sola de ellas (excepto sin contar JS). MySQL guarda los datos, PHP controla la lógica y conecta todo, y HTML/CSS/JS es con lo que el usuario interactúa. Juntas, estas tecnologías nos permitieron construir un proyecto full-stack completo que resuelve una necesidad real: una plataforma simple donde los usuarios pueden descubrir películas y compartir sus opiniones a través de reseñas. A lo largo del proyecto he aprendido muchísimo sobre cómo se conectan las diferentes partes: cómo la base de datos se conecta con el controlador, el controlador con la UI, y cómo todo interactúa entre sí.



En general, Chamitos Movie Club ha sido el proyecto más completo y complicado en el que he trabajado hasta ahora. Me obligó a combinar todo lo que hemos aprendido en varias asignaturas diferentes durante los dos últimos trimestres en una aplicación real. Ya no es solo una web simple, sino un proyecto completo donde la base de datos, la lógica del controlador y la interfaz de usuario dependen entre sí para funcionar correctamente. Hacerlo en grupo también me enseñó lo importante que es la estructura y la coordinación, especialmente cuando varias personas trabajan en los mismos archivos y en el mismo repositorio de GitHub. Esta es una parte que será importante para mí asegurar que funcione de forma más fluida la próxima vez.

El proyecto también resuelve una necesidad clara (que tenía nuestro grupo): da a los usuarios (principalmente a nosotros) un lugar simple para explorar películas y compartir nuestras opiniones a través de reseñas, y también da a los administradores un espacio separado para gestionar el catálogo de películas. Lo más importante que aprendí de este proyecto es cómo diferentes tecnologías pueden trabajar juntas como un solo sistema, y cómo el resultado final se vuelve mucho más fuerte cuando cada parte tiene un rol claro. También aprendí lo complicado que es combinar PHP y las imágenes. Si siguiéramos mejorando el proyecto, el siguiente paso sería hacer el flujo de trabajo aún más suave (especialmente con Git), y mejorar pequeñas limitaciones como las imágenes de las películas y la seguridad del admin, pero en general estoy orgulloso del resultado y me siento mucho más preparado para construir proyectos reales en el futuro. De verdad siento que ahora puedo hacer webs funcionales básicas que además se ven bien. Disfruté mucho este proyecto.

- github repo: https://github.com/oscarsorensen/oscar-bryan-carlos


## ##################################################################################################################################


## 1.-Introducción breve y contextualización
This Intermodular Project exam is part of a broader exam, consisting of the following subjects: Base de Datos, Lenguajes de Marcas, Programacion, and Proyecto Intermodular. In this exam I will explain the Chamitos Movie Club project from a global perspective: why we chose this topic, what need it solves, how the project works screen by screen, and how we combined everything we learned during the course into one complete application.

A bit of context: This is the first real group project we have developed, and our goal was to create a mini web application where users can browse movies, register and log in, write reviews, and where admins can manage the movie catalog in a separate backend panel.

I choose to be in a group with Bryan and Carlos, since these are two of my good friends here in class, and i know that both of them are good workers and programmers. Together, we choose to create a website for movies. Our inspiration was LetterBoxd, a place where you can review, read reviews, have a user and a library of movies that you have reviewed. This would solve our need for a provate LetterBoxd, which can organise movies, reviews, and let us share these with our friends.


## 2 & 3.-Desarrollo detallado y preciso + Aplicación práctica

When we started the project we didnt actually dissect the different parts yet, to figure out what who was supposed to do when, since this was very early in the project. We actually started by just talking about our project, what it should include, and what it shouldnt. Then we draw a rough database with tables, and set up a github project and slowly started to figure out what should go where. 

Now even with the best of intentions, that is when we started to run into a bit of trouble- not because of lack of willingsness, but we are still 3 different people in 3 different stages of becoming programmers. Personally i have already used github and git extensively, and therefore I understand github. It quicly became clear that my classmates didnt. We had a few problems with folders, dublicates, branches that werent at all compatable. This unfortunately took me quite a few hours to clean up. Not because the work was bad, but becuase it didnt fit in the structure at all- the structure i had already made, organized, and explained to my classmates.

After we got this solved, it was more smooth the rest of the project. We decided that i did the database, the structure, and everything php, and that Carlos and Bryan would do the css and html, the styling. I choose PHP as a bit of a challange. We have learned that that is which most webpages uses, (even though apparently it isnt that great) and i decided that it would be good practice for the future.

 I spent a few days in the start of the holiday, making my part work more or less as intended. When we reached christmas, we had a fully functioning website, basic that it was. Unfortunately here we had again the same problems with gitflow and versions, which again ended with me spending some hours cleaning it up, before it was usuable.

Then we decided to part remaining work out in another way. Everyone would get certain files that they had to work in, while touching nothing else. This should be possible, since the project already worked. The only thing that really was left at this point was the styling. This worked much better, and Bryan made the very nice looking login and registrer pages. I ended up doing the rest. So the final work ended up being devided like this:

Oscar: DB, structure, PHP, Git cleanup
Bryan: login/register styling
Carlos: styling



- The flow of the project works as follows:

At the center of the project we have the main page.
(SCREENSHOT 1)

Here the user can see the full movie catalog of Chamitos Movie Club. You can scroll through the page and see around 30 movies that we added as a proof of concept. Each movie card shows the title, director, category, release date, and a short description. In the header there is also a search bar as well as  buttons for registration and login.
(SCREENSHOT 1.5)
(SCREENSHOT 2)
(SCREENSHOT 3)

If you click the “Registrar” button, you are taken to the registration page where you can create an account. After registering, the user is automatically redirected to their own profile page.
(SCREENSHOT 4)

On the profile page you can see an overview of all the movies they have reviewed. From here you can click a movie again to go to the movie detail page, which is the same page you can access from the main catalog. You can also log out or return to the main page using the header navigation.

After logging in, the interface changes: instead of “Registrar” and “Login”, the header shows “Perfil” and “Logout”. This happens because we use PHP sessions to check if the user is logged in, and then we show different options depending on the session data. We use the same logic on the movie detail page as well. This is a critical design decicion and one of the most important things we battled with getting right: how could we make sure that it was easy to see wether you were logged in or not? how could we make sure you saw different things and had different options?
(SCREENSHOT 5)

On the movie detail page, when the user is logged in, they can write reviews for the movie. If the user is not logged in, the page shows a message telling them that they must log in before they can post a review.

Everything above is part of the frontend, which is what normal users of the website can see and interact with. But the project also includes a backend admin area, which is only for administrators. We kept a very clear separation between frontend and admin, because they have different goals: the frontend is for browsing and interacting, while the admin area is for managing the catalog- which is not a thing the normal user is supposed to be able to do.

The admin panel is accessed through a login, and after a successful login the admin is redirected to a dashboard where they can see a list of all the movies stored in the database.
(SCREENSHOT 6)
(SCREENSHOT 7)

The design of the admin area is much more strict and simple. Here we focused on efficiency and clarity instead of visual style. The backend is not meant to impress the user, it is meant to work reliably and make it easy to manage the data.

From the admin list, the admin can click “Edit” on a movie, which opens a page where the movie information can be updated. Because the admin actions are directly connected to the database, all changes are saved immediately and then reflected on the frontend catalog as well.
(SCREENSHOT 8)

Finally, the admin also has an option to add new movies. This opens a blank form where the admin can create a new movie entry. New movies automatically use a placeholder image until the image is changed manually in the database. This is a small design limitation in the current version, but it is also one of the improvements we could implement in the next iteration of the project.



- Technologies

In regards to technologies we chose MySQL/SQL as our database, because we needed a way to store all the information permanently. When doing the next project, we will do this differently, because we technically ended up with 3 local databases, which was a bit messy if someone had to change it. The database included users, movies, categories and reviews. Using a real (although local) database also made the project feel much more realistic, because the website is not just static pages, but a dynamic application where the content comes directly from the data. And it actually ended up working all of it.

We used PHP as the main controller language, firstly because of the challange, but also because it fits very good with a web project and because it connects everything together. PHP handles the logic of the project, it selects movies from the database, shows them on the pages, manages login/logout with sessions, and makes sure that only logged in users can write reviews (we were very proud of how that ended up working). PHP is also used for the admin panel, where admins can create, edit and delete movies. In that way, PHP the real heart of the project. It connects the database and the interface.

For the interface and style we used HTML and CSS, because this is what we have learned in Lenguajes de Marcas and it is the core of how the website looks and works. HTML gives the structure of the pages (headers, movie cards, forms, buttons) and the advanced CSS we ended using is what makes the project feel like a real modern website instead of a simple school exercise. We spent a lot of time on styling, especially on the frontend, because we wanted the site to be clear, easy to use, and visually consistent. It worked very well, but now that the project is done, i see many ways to better it already.

We also used a small amount of JavaScript, mainly to improve the user experience on the main page. The live search bar filters movies instantly without reloading the page, which makes the catalog faster and easier to browse- it is also elegant in the way that it doesnt have to connect to the database. This is a small feature, but it shows how we can combine different technologies to make the project more interactive and lively.

Overall, the combination of MySQL + PHP + HTML/CSS/JS works very well because each technology has a clear role that couldnt have been taken by another. I dont see a way this project could work without just one of them (except not counting JS) MySQL stores the data, PHP controls the logic and connects everything and HTML/CSS/JS is what the user interacts with. All together these technologies allowed us to build a complete full-stack project that solves a real need: a simple platform where users can discover movies and share their opinions through reviews. Throughout the project i have learned so much about how the different parts connects. How the database connects to the controller, the controller to the UI and how everything interact with each other.


## 4.-Conclusión breve'

Overall, Chamitos Movie Club has been the most complete and complicated project I have worked on so far. It forced me to combine everything we have learned from multiple different classes, over the last two trimesters, into one real application. It is not just a simple website now, but a full project where the database, the controller logic, and the user interface all depend on each other to work correctly. Building it in a group also taught me how important structure and coordination is, especially when multiple people work on the same files and the same GitHub repository. This is a part that will be important for me to make sure works smoother next time.

The project also solves a clear need (that our group had) it gives users(us, mainly) a simple place to browse movies and share our opinions through reviews and also it gives admins a separate space to manage the movie catalog. The biggest thing I learned from this project is how different technologies can work together as one system, and how the final result becomes much stronger when each part has a clear role. I also learned how complicated php and pictures is togeter. If we continued improving the project, the next step would be to make the workflow even smoother (especially with Git), and to improve small limitations like movie images and admin security, but overall I am proud of the result and I feel much more prepared to build real projects in the future. I actually feel like i can make functional basic websites now- that even look good. I greatly enjoyed this.

- github repo: https://github.com/oscarsorensen/oscar-bryan-carlos