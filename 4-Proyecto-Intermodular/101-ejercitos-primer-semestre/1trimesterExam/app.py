# ==============================================================
# HOW TO USE THIS TEMPLATE (EXAM INSTRUCTIONS)
# ==============================================================
# 1) This Flask app connects to MySQL and displays table data.
#    It completes the integration between Bases de Datos,
#    Programación, and Lenguajes de Marcas.
#
# 2) Change only names to match the exam theme:
#       examdb    →  your database (e.g. blog, journal, ads)
#       category  →  main table (e.g. autores, usuarios)
#       item      →  secondary table (e.g. entradas, anuncios)
#
# 3) What’s already included:
#    - Flask setup with one route ('/')
#    - MySQL connection
#    - SELECT query using LEFT JOIN
#    - HTML rendering through Jinja template
#
# 4) Folder structure expected:
#       app.py
#       /templates
#           index.html
#
# 5) To test:
#    - Make sure MySQL service is running
#    - Run:  python app.py
#    - Open browser at:  http://localhost:5000
#
# 6) Adapt fast in exam:
#    a) Change DB/table names
#    b) Edit SQL query fields if needed
#    c) Adjust HTML template wording
#
# 7) Works with Flask and mysql-connector-python
# ==============================================================

from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)

# ---------- 1) DATABASE CONNECTION ----------
config = {
    "host": "localhost",
    "user": "exam_user",
    "password": "1234",
    "database": "examdb"
}

# ---------- 2) ROUTE ----------
@app.route("/")
def index():
    db = mysql.connector.connect(**config)
    cursor = db.cursor(dictionary=True)

    query = """
        SELECT item.title, item.date, item.image, item.content, category.name AS author
        FROM item
        LEFT JOIN category ON item.category_id = category.id
        ORDER BY item.id DESC
    """
    cursor.execute(query)
    entries = cursor.fetchall()

    cursor.close()
    db.close()

    return render_template("index.html", entries=entries)

# ---------- 3) MAIN ----------
if __name__ == "__main__":
    app.run(debug=True)
