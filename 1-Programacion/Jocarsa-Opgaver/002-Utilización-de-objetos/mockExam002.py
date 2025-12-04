#En este ejercicio desarrollo un pequeño programa en Python llamado planificador de cuadras, que calcula cuántas cuadras son necesarias para alojar a un número determinado de caballos.
#El programa solicita al usuario los datos principales (número de caballos, capacidad de cada cuadra y fecha), utiliza el módulo math para redondear al alza con ceil() y el módulo datetime para obtener propiedades de la fecha actual, como el mes, el año y el día de la semana.

import math
import datetime

horses = input("Enter the number of horses you have: ")  # input devuelve un string
if horses == "0":  # comparamos con string
    print("You have no horses, so you don't need any stables. Enter a valid number of horses next time.")
    exit()

today = datetime.date.today()
is_weekend = today.isoweekday() in (6, 7)  # 6=Saturday, 7=Sunday

todays_date = input("Enter today's date (YYYY-MM-DD) or leave blank for today: ")

capacity_per_stable = input("Enter the capacity of each stable (number of horses it can hold): ")  # input devuelve un string
stables_needed = math.ceil(int(horses) / int(capacity_per_stable))  # convertimos a int para hacer la division

print("Today's date is:", today, ".")
print("We are in month number", today.month, "of the year", today.year, ".")
print("Is today a weekend?", is_weekend)
print("You will need", stables_needed, "stables to accommodate all your horses.")
print("Each stable can hold up to", capacity_per_stable, "horses.", "You have", horses, "horses in total.")

#Este programa demuestra cómo combinar la entrada de datos con operaciones matemáticas y el manejo de fechas mediante módulos estándar de Python.
#El uso de math.ceil() permite calcular las cuadras necesarias de forma precisa, mientras que datetime.date facilita mostrar información temporal relevante.
#Gracias a estas funciones, se obtiene un informe claro y automatizado que cumple con los objetivos del ejercicio.