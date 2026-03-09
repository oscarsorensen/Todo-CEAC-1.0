crontab -e

crontab -e

0 * * * * /usr/bin/python3 /var/www/html/generadorapuntesv3/apuntes.py "/var/www/html/dam/Segundo/Acceso a datos" >/dev/null 2>&1

0 * * * * = en el min 0 de cada hora de cada dia de cada dia de la semana de cada mes

* * * * *
│ │ │ │ │
│ │ │ │ └── día de la semana (0-7)
│ │ │ └──── mes (1-12)
│ │ └────── día del mes (1-31)
│ └──────── hora (0-23)
└────────── minuto (0-59)