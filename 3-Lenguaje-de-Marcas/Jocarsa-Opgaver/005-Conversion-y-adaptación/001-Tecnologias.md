En este ejercicio utilicé Python para practicar cómo crear un archivo PDF a partir de texto. Lo hago para simular una situación real en la que podría necesitar convertir contenido a un formato de documento que se pueda compartir fácilmente, como un CV, un informe o cualquier información que deba imprimirse o almacenarse de manera formal. Josevicente dijo que los programadores suelen tener esta tarea, así que quiero asegurarme de que la entiendo correctamente.

Utilicé la biblioteca FPDF y creé una función que recibe una cadena de texto y la convierte en un archivo PDF llamado "salida.pdf". El código crea un nuevo PDF, añade una página, establece la fuente y, a continuación, lee el texto línea por línea utilizando split(«\n»). Cada línea se escribe en el PDF como una nueva fila utilizando pdf.cell(). Por último, el programa exporta el documento a un archivo.

from fpdf import FPDF

def text_to_pdf(texto, filename="salida.pdf"):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    for linea in texto.split("\n"):
        pdf.cell(0, 10, txt=linea, ln=True)

    pdf.output(filename)

# Texto 
texto = """Hola, este es un documento PDF que he hecho para testear.
Cada línea aparece como una línea nueva en el PDFe.
Espero."""

text_to_pdf(texto)

Esta actividad me ayudó a comprender mejor cómo Python puede trabajar con bibliotecas externas para crear documentos reales y útiles. También muestra cómo lo que aprendemos se puede utilizar en proyectos reales, como generar documentos automatizados, informes o archivos formateados de una manera sencilla.