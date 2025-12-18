<!doctype>
<html>
	<head>
  	<meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
    	article{background:white;}
    	@media (max-width: 500px) {
        body{
        	background:red;font-size:48px;
          display:flex;
          flex-direction:column;
          gap:20px;
          }
      }
      @media (min-width: 500px) and (max-width: 1000px ) {
        body{background:green;}
      }
      @media (min-width: 1000px) {
        body{
        	background:blue;font-size:12px;
          display:grid;
          grid-template-columns:repeat(4,100fr);
          gap:20px;
          }
      }
    </style>
  </head>
  <body>
  	<article>Hola</article>
    <article>Hola</article>
    <article>Hola</article>
    <article>Hola</article>
    <article>Hola</article>
    <article>Hola</article>
    <article>Hola</article>
    <article>Hola</article>
    <article>Hola</article>
    <article>Hola</article>
    <article>Hola</article>
    <article>Hola</article>
    
  </body>
</html>