


import pickle
archivo = open("datos.bin","rb")
cadena = "Oscar Sorensen"

pickle.dump(cadena,archivo)

archivo.close()