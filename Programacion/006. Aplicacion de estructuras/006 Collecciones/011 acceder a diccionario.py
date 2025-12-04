persona = {
    "nombre": "Oscar Sorensen",
    "apellido": "Sjorman",
    "correo": "oscar@gmail.com",
    "edad": 25,
    "telefono": [
        {
        "tipo":"fijo",
        "numero":12345678
        },
        {
        "tipo":"mobil",
        "numero":87654321
        }
    ]
}

print(persona)
print(persona["telefono"][0]["numero"])  
