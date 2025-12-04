
#Følgende ændrer sig fra en string til en liste af elementer ved hjælp af split-metoden. Dette er meget praktisk.
datos = "uno, dos, tres, cuatro, cinco, seis"
#Først ser vi listen
print (datos)

#Så splitter vi strengen ved hjælp af komma og mellemrum som separator
partido = datos.split(", ")
#Så ser vi den splittede liste
print (partido)