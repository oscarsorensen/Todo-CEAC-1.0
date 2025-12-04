from lxml import etree

try:
    etree.parse("004-cv.xml")
    print("XML OK")
except Exception as e:
    print("FEJL:", e)
