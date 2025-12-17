import requests
from lxml import html
import mysql.connector
import time
from urllib.parse import urljoin, urlparse

URLS = ["https://www.engelvoelkers.com/es/"]

DB_HOST = "localhost"
DB_USER = "satori"
DB_PASSWORD = "Satori123$"
DB_NAME = "satori"

BASE_DOMAIN = urlparse(URLS[0]).netloc   # ← AÑADIDO
VISITADAS = set()


def sanitize_links(base_url, links):
    urls_validas = []

    for link in links:
        if not link:
            continue

        link = link.strip()

        if link.startswith(("#", "javascript:", "mailto:", "tel:")):
            continue

        full_url = urljoin(base_url, link)
        parsed = urlparse(full_url)

        if parsed.scheme not in ("http", "https"):
            continue

        if parsed.netloc != BASE_DOMAIN:   # ← AÑADIDO
            continue

        if len(full_url) > 500:
            continue

        urls_validas.append(full_url)

    return list(set(urls_validas))


def busca(URLS):
    for URL in URLS:

        if URL in VISITADAS:
            continue

        VISITADAS.add(URL)
        time.sleep(1)

        try:
            print("Procesando:", URL)

            response = requests.get(
                URL,
                timeout=10,
                headers={
                    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/120 Safari/537.36"
                }
            )
            response.raise_for_status()

            tree = html.fromstring(response.content)

            title_list = tree.xpath("//title/text()")
            web_title = title_list[0].strip() if title_list else None

            html_content = response.text[:255]

            print("WEB TITLE:")
            print(web_title or "No title found")

            conn = mysql.connector.connect(
                host=DB_HOST,
                user=DB_USER,
                password=DB_PASSWORD,
                database=DB_NAME,
                charset="utf8mb4",
                use_unicode=True
            )

            try:
                cur = conn.cursor()
                sql = """
                    INSERT INTO paginas (titulo, url, contenido)
                    VALUES (%s, %s, %s)
                """
                cur.execute(sql, (web_title, URL, html_content))
                conn.commit()
                print(f"OK MySQL → ID: {cur.lastrowid}")
            finally:
                try:
                    cur.close()
                except Exception:
                    pass
                conn.close()

            enlaces = tree.xpath("//a/@href")
            enlaces_limpios = sanitize_links(URL, enlaces)

            busca(enlaces_limpios)

        except Exception as e:
            print("Error pero continuamos:", e)


busca(URLS)
