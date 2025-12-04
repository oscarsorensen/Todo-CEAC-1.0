


def divide(dividendo, divisor):
    try:                                 #intenta
        dividendo = int(dividendo)       #convertir dividendo a entero
        divisor = int(divisor)          #

        if divisor != 0:                            
            return dividendo / divisor            
        else:      
            return False                        
    except:
        return "Error: No se puede dividir por texto"


for dividendo in range(-100, 100):
    for divisor in range(-100, 100):
        print(divide(dividendo, divisor))

print(divide(4,"a "))
