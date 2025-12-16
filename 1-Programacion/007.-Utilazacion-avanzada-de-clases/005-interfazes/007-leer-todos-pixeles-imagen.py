from PIL import Image

imagen = Image.open("billed.jpg")

anchura,altura = imagen.size	

for x in range(0,anchura):	
	for y in range(0,altura):	
		pixel = imagen.getpixel((x, y))	
		rojo = pixel[0]
		verde = pixel[1]
		azul = pixel[2]
		rojo += 20
		verde += 20
		azul += 20
		imagen.putpixel((x, y), (rojo, verde, azul)) # ESTO ES CORRECTO
    
imagen.save("modificado.jpg")								# Y lo saco por pantalla