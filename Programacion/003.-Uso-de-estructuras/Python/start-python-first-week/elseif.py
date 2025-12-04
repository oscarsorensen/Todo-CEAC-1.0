

edad = 24
if edad < 10:
    #esto no es menor que 10
    print("Eres un niño")
elif edad >= 10 and edad < 20:
    #se ejecuta si la edad es mayor que 10 y menor que 20
    print("Eres un adolescente")
elif edad >= 20 and edad < 30:
    #se ejecuta si la edad es mayor que 20 y menor que 30
    print("Eres un joven")
else:
    #se ejecuta en cualquier otro caso
    print("Eres un adulto")