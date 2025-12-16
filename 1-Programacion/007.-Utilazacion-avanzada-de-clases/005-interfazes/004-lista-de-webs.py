import requests
from lxml import html

urls = [
  	"https://jocarsa.com",
  	"https://josevicentecarratala.com"
]

for url in urls:

    response = requests.get(url, timeout=10)
    response.raise_for_status()  # raises exception if not 200

    # Parse HTML
    tree = html.fromstring(response.content)

    # Find all <h1> elements in the document. This can be changed for A, h2, P, etc.

    h1_elements = tree.xpath("//h1")

    # Print their text content
    for i, h1 in enumerate(h1_elements, start=1):
        text = h1.text_content().strip()
        print(f"H1 #{i}: {text}")