En este ejercicio utilicé GitHub Pages para publicar algunas páginas web personales sencillas en línea. La idea es simular o prepararme para situaciones reales en las que necesite tener un portafolio público o un CV que cualquiera pueda visitar en Internet. Por suerte, ya tenía estas cosas hechas y en línea, lo que acortó la tarea.

Creé dos repositorios en GitHub: uno para mi «currículum» y otro para mi «portafolio». Dentro de cada repositorio, añadí los archivos HTML necesarios y utilicé el CSS proporcionado para dar estilo a las páginas. A continuación, configuré GitHub Pages en los ajustes del repositorio para que las páginas se publicaran desde la rama principal. Solo utilicé HTML, CSS y un poco de JavaScript, según era necesario.

Mi CV en GitHub, en CSS y HTML.

```
<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>Curriculum · Oscar Sørensen</title>

    
    <link href="https://fonts.googleapis.com/css2?family=Fira+Code:wght@300;400;500&display=swap" rel="stylesheet">

    <style>
        html {
            background: #111;
            font-family: "Fira Code", monospace;
            font-size: 14px;
            color: #DDD;
        }

        body {
            background: #1E1E1E;
            width: 900px;
            margin: 40px auto;
            display: flex;
            border-radius: 6px;
            overflow: auto;
            box-shadow: 0 0 25px rgba(0,0,0,0.8);
        }

        /* LEFT PANEL */
        #left {
            width: 32%;
            background: #252526;
            padding: 25px;
            border-right: 1px solid #333;
        }

        #left img {
            width: 140px;
            border-radius: 6px;
            display: block;
            margin: 0 auto 20px auto;
            border: 1px solid #444;
        }

        #left h3 {
            font-size: 15px;
            margin-bottom: 8px;
            font-weight: 500;
            color: #569CD6; /* VS Code blue */
            border-bottom: 1px solid #333;
            padding-bottom: 3px;
        }

        #left ul {
            list-style: none;
            padding-left: 0;
            margin: 0 0 22px 0;
        }

        #left ul li {
            margin-bottom: 6px;
            color: #CCC;
        }

        /* RIGHT PANEL */
        #right {
            width: 68%;
            padding: 35px;
        }

        #right h1 {
            font-size: 30px;
            font-weight: 500;
            margin-bottom: 6px;
            color: #DCDCAA; 
        }

        #right h2 {
            color: #C586C0; 
            font-size: 18px;
            font-weight: 400;
            margin-bottom: 20px;
        }

        #right section {
            margin-bottom: 35px;
        }

        #right h3 {
            color: #569CD6;
            font-size: 16px;
            margin-bottom: 10px;
            border-bottom: 1px solid #333;
            padding-bottom: 4px;
        }

        .job {
            margin-bottom: 23px;
        }

        .job-title {
            color: #DCDCAA;
            font-weight: 400;
        }

        .job-date {
            font-size: 12px;
            color: #888;
            margin-bottom: 6px;
        }

        .job ul {
            list-style: none;
            padding-left: 0;
        }

        .job li {
            margin-bottom: 6px;
        }
    </style>

</head>


<body>

    <!-- LEFT -->
    <section id="left">

        <img src="oscarbillede.png">

        <h3>Education</h3>
        <ul>
            <li>CEAC — Higher Technician in Web App Development</li>
            <li>Midtsjællands Gymnasium — Upper Secondary</li>
            <li>Haslev Midtskolen — Primary & Secondary School</li>
        </ul>

        <h3>Skills</h3>
        <ul>
            <li>Digital marketing</li>
            <li>Negotiation</li>
            <li>Communication</li>
            <li>Critical thinking</li>
            <li>Team leadership</li>
        </ul>

        <h3>Additional</h3>
        <ul>
            <li>Driving licence B + vehicle</li>
            <li>On-site & hybrid availability</li>
            <li>Experience with AI tools</li>
        </ul>

        <h3>Languages</h3>
        <ul>
            <li>Danish — Native</li>
            <li>English — C2</li>
            <li>Spanish — B2</li>
            <li>Norwegian — B1</li>
        </ul>

        <h3>Contact</h3>
        <ul>
            <li>+34 698 xxx xxx</li>
            <li>oscar081100@gmail.com</li>
            <li>Valencia, Spain</li>
        </ul>

    </section>


    <!-- RIGHT -->
    <section id="right">

        <h1>Oscar Sørensen</h1>
        <h2>Upcoming Fullstack Developer</h2>

        <section>
            <h3>Profile</h3>
            <p>
                Enthusiastic and fast-learning candidate with strong analytical and organizational skills.
                Experience in digital documentation, file management, website maintenance, and general IT operations.
                Motivated to expand technical competencies through training and hands-on projects.
                Committed to a long-term IT career based on reliability, adaptability, and continuous learning.
            </p>
        </section>

        <section>
            <h3>Work Experience</h3>

            <!-- MEDITER -->
            <div class="job">
                <div class="job-title">Mediter Real Estate — Administration & Real Estate Agent</div>
                <div class="job-date">Dec 2021 – Jun 2024</div>
                <ul>
                    <li>Managed company website and all digital marketing platforms (Instagram, Facebook, real estate portals).</li>
                    <li>Produced, edited, and managed content for the corporate YouTube channel.</li>
                    <li>Primary point of contact with construction firms: negotiated prices, projects, and timelines.</li>
                    <li>Coordinated communication between clients, external agents, and legal professionals.</li>
                    <li>Accompanied clients to property visits, providing operational support and negotiations.</li>
                    <li>Handled all real estate processes except contract drafting.</li>
                </ul>
            </div>

            <!-- SCANSPAN -->
            <div class="job">
                <div class="job-title">ScanSpan — Junior IT Assistant</div>
                <div class="job-date">Jan 2023 – May 2023</div>
                <ul>
                    <li>Worked on basic programming tasks and small software automations.</li>
                    <li>Updated internal wikis, digital documentation, and knowledge systems.</li>
                    <li>Maintained and updated websites for internal and external use.</li>
                    <li>Led digital organization projects, file restructuring, and system cleanup.</li>
                    <li>Gained practical real-world IT experience supporting the technical team.</li>
                </ul>
            </div>

            <!-- SERVICE & OPERATIONS -->
            <div class="job">
                <div class="job-title">Service & Operations — Various Centers (Denmark)</div>
                <div class="job-date">2015 – 2021</div>
                <ul>
                    <li>Ensured safety, access control, water testing, logbook management, and opening/closing routines as a lifeguard.</li>
                    <li>Provided customer service, handled cash and transactions, managed reservations, and supported daily operations.</li>
                    <li>Operated activity stations such as shooting ranges and mechanical bull attractions.</li>
                    <li>Assisted with technical tasks, event setup, repairs, and general logistics.</li>
                </ul>
            </div>

        </section>

        <section>
            <h3>Personal Interests</h3>
            <ul>
                <li>Fitness and strength training</li>
                <li>Cooking</li>
                <li>Playing guitar</li>
                <li>Weekend activities with friends</li>
            </ul>
        </section>

    </section>

</body>
</html>


Mi Github Portafolio Pagina

<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Portfolio · Oscar Sørensen</title>

    <link href="https://fonts.googleapis.com/css2?family=Fira+Code:wght@300;400;500&display=swap" rel="stylesheet">

    <style>
        html {
            background: #111;
            font-family: "Fira Code", monospace;
            font-size: 14px;
            color: #DDD;
        }

        body {
            background: #1E1E1E;
            width: 900px;
            margin: 40px auto;
            display: flex;
            border-radius: 6px;
            overflow: auto;
            box-shadow: 0 0 25px rgba(0,0,0,0.8);
        }

        /* LEFT PANEL */
        #left {
            width: 25%;
            background: #252526;
            padding: 25px;
            border-right: 1px solid #333;
        }

        #left h3 {
            font-size: 18px;
            margin-bottom: 10px;
            font-weight: 500;
            color: #569CD6;
            border-bottom: 1px solid #333;
            padding-bottom: 3px;
        }

        #left ul {
            list-style: none;
            padding-left: 0;
            margin: 0 0 22px 0;
        }

        #left ul li {
            margin-bottom: 10px;
            color: #CCC;
        }

        #left a {
            color: #CCC;
            text-decoration: none;
        }

        #left a:hover {
            color: #4FC1FF;
        }

        /* RIGHT PANEL */
        #right {
            width: 75%;
            padding: 35px;
        }

        #right h1 {
            font-size: 30px;
            font-weight: 500;
            margin-bottom: 6px;
            color: #DCDCAA;
        }

        #right h2 {
            color: #C586C0;
            font-size: 18px;
            font-weight: 400;
            margin-bottom: 20px;
        }

        #right section {
            margin-bottom: 35px;
        }

        #right h3 {
            color: #569CD6;
            font-size: 16px;
            margin-bottom: 12px;
            border-bottom: 1px solid #333;
            padding-bottom: 4px;
        }

        #right p {
            line-height: 1.4;
            margin-bottom: 10px;
        }

        .project {
            padding-bottom: 15px;
            border-bottom: 1px solid #333;
            margin-bottom: 20px;
        }

        .project-title {
            color: #DCDCAA;
            font-size: 15px;
            margin-bottom: 3px;
        }

        .project a {
            color: #4FC1FF;
            text-decoration: none;
            font-weight: 400;
        }

        .project a:hover {
            text-decoration: underline;
        }
    </style>
</head>



<body>

    <!-- LEFT PANEL -->
    <section id="left">

        <h3>Navigation</h3>
        <ul>
            <li><a href="https://oscarsorensen.github.io/OscarsCV/">Curriculum Vitae</a></li>
            <li><a href="https://oscarsorensen.github.io/Portafolio/">Portfolio</a></li>
            <li><a href="https://github.com/oscarsorensen/">GitHub</a></li>
        </ul>

        <h3>Contact</h3>
        <ul>
            <li>oscar081100@gmail.com</li>
            <li>Valencia, Spain</li>
        </ul>

    </section>



    <!-- RIGHT PANEL -->
    <section id="right">

        <h1>Oscar Sørensen</h1>
        <h2>Portfolio Projects</h2>

        <section>
            <h3>Featured Projects</h3>

            <div class="project">
                <div class="project-title">Localhost Dashboard</div>
                <p>
                    Local PHP dashboard that scans and organizes all my CEAC coursework, with file metadata, search and GitHub sync<br>
                    <a href="https://github.com/oscarsorensen/localhost-dashboard" target="_blank">
                        View on GitHub
                    </a>
                </p>
            </div>

            <div class="project">
                <div class="project-title">Python CRUD Application (MySQL)</div>
                <p>
                    Menu-based console program that performs CRUD operations directly on a MySQL database using Python.<br>
                    <a href="https://github.com/oscarsorensen/Todo-CEAC/blob/main/z.Exams/1.Tri-Exam/2Prog/examprog.py" target="_blank">
                        View on GitHub
                    </a>
                </p>
            </div>

            <div class="project">
                <div class="project-title">SQL Blog / Portfolio Database</div>
                <p>
                    Relational MySQL database with normalized tables, foreign keys, sample data, JOIN operations, and a reusable SQL view.<br>
                    <a href="https://github.com/oscarsorensen/Todo-CEAC/blob/main/z.Exams/1.Tri-Exam/1BDD/examfixed.sql" target="_blank">
                        View on GitHub
                    </a>
                </p>
            </div>

            <div class="project">
                <div class="project-title">HTML/CSS Blog Template</div>
                <p>
                    Clean responsive blog layout using semantic HTML and structured CSS.<br>
                    <a href="https://github.com/oscarsorensen/Todo-CEAC/blob/main/z.Exams/1.Tri-Exam/3LDM/EXAM.LDM.html" target="_blank">
                        View on GitHub
                    </a>
                </p>
            </div>

            <div class="project">
                <div class="project-title">JavaScript DOM + Fetch</div>
                <p>
                    Dynamic webpage that loads external JSON files and updates the interface using DOM manipulation.<br>
                    <a href="https://github.com/oscarsorensen/Todo-CEAC/blob/main/Proyecto%20Intermodular/102-%20ejercicios%20practicos%20segundo%20trimestre/102%20Leer%20JSON/004%20modelo%20mas%20completo/002%20platilla%20fetch.html" target="_blank">
                        View on GitHub
                    </a>
                </p>
            </div>

            <div class="project">
                <div class="project-title">Flask Application (Python + MySQL)</div>
                <p>
                    Small Flask-based backoffice app that uses Jinja templates and real SQL interactions with a MySQL database.<br>
                    <a href="https://github.com/oscarsorensen/Todo-CEAC/blob/main/Proyecto%20Intermodular/102-%20ejercicios%20practicos%20segundo%20trimestre/103%20Jinja/006%20backoffice%20con%20mysql.py" target="_blank">
                        View on GitHub
                    </a>
                </p>
            </div>

        </section>

    </section>

</body>
</html>

Mi README.md de Github que funciona en mi página principal de Github.

# Oscar Sørensen



<div align="center">
  <p>
    Web Applications Development student (DAW/DAM) in Valencia. <br>
    Focused on fullstack development, databases, Python, and modern web technologies. <br>
    Currently building projects with Python, MySQL, Flask, and JavaScript. <br>
    Interested in backend logic, clean architecture, and practical real-world applications.
  </p>

<br>

![Oscar's Contribution Graph](https://github-readme-activity-graph.vercel.app/graph?username=oscarsorensen&theme=tokyo-night) 

</div>

---



## Stack

<table align="center">
  <tr>
    <td align="center" width="100"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" width="40"/><br>Python</td>
    <td align="center" width="100"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/javascript/javascript-original.svg" width="40"/><br>JavaScript</td>
    <td align="center" width="100"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/mysql/mysql-original.svg" width="40"/><br>MySQL</td>
    <td align="center" width="100"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/sqlite/sqlite-original.svg" width="40"/><br>SQL</td>
    <td align="center" width="100"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/html5/html5-original.svg" width="40"/><br>HTML5</td>
  </tr>
  <tr>
    <td align="center" width="100"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/css3/css3-original.svg" width="40"/><br>CSS3</td>
    <td align="center" width="100"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/flask/flask-original.svg" width="40"/><br>Flask</td>
    <td align="center" width="100"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/git/git-original.svg" width="40"/><br>Git</td>
    <td align="center" width="100"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/github/github-original.svg" width="40"/><br>GitHub</td>
    <td align="center" width="100"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/vscode/vscode-original.svg" width="40"/><br>VS Code</td>
  </tr>
</table>

---

<h2 style="pointer-events:none;">Curriculum Vitae & Portafolio</h2>

<div align="center">
  <a href="https://oscarsorensen.github.io/OscarsCV/" target="_blank">
    <img src="noname3.png" height="80" style="margin-right: 20px;">
  </a><!--
  --><a href="https://oscarsorensen.github.io/Portafolio/" target="_blank">
    <img src="buttonportafolio.png" height="80">
  </a>
</div>

---
<p align="center"> 
  <img
    src="https://github-readme-stats-oscar.vercel.app/api/top-langs/?username=oscarsorensen&layout=compact&theme=tokyonight&card_width=380"
    width="380"
  />
  <img
    src="https://github-readme-stats-oscar.vercel.app/api?username=oscarsorensen&show_icons=true&theme=tokyonight&hide_rank=false&include_all_commits=true"
    width="395"
  />
</p>

---

<div align="center">
<img src="https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExc2xpZDlkYjI4Y2tzdXA2M3o4OHg1dm5rbWNhaXhsN2diajZrdG5odCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/GghGKaZ8JeHJx0apQC/giphy.gif" width="260"> <br>
<br>
</div>

---
```

Esta actividad me ayudó a reforzar mis conocimientos sobre cómo publicar páginas web utilizando GitHub Pages y cómo gestionar contenido web real de forma organizada. También muestra cómo se pueden aplicar estos conocimientos en proyectos reales, por ejemplo, para compartir información personal, portfolios o cualquier tipo de sitio web público de forma sencilla y profesional.