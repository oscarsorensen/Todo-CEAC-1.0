import matplotlib.pyplot as pt

# Datos de ejemplo (promedios calculados en MySQL)
promedio_redondeado = 34
promedio_bajito = 33
promedio_alto = 35

labels = ['Promedio Redondeado', 'Promedio Bajo', 'Promedio Alto']
values = [promedio_redondeado, promedio_bajito, promedio_alto]

pt.pie(values, labels=labels, autopct='%1.1f%%')
pt.axis('equal')  # Para que la gráfica sea circular
pt.show()