# --------------------------------------------------------------------------------
# FOR UBUNTO
En terminal:

sudo apt install apache2

De ahi en adelante, todos los archivos que hagáis tendrán que estar en:
/var/www/html

Liberación de permisos:

cd /var/www
sudo chmod 777 -R html

sudo = El super usuario va a hacer algo
chmod = cambiamos permisos de archivo y carpeta
777 = los tres grupos pueden hacer de todo
-R = recursivo (se aplica a todo lo contenido)
html = la carpeta de destino
# --------------------------------------------------------------------------------

# Apache en macOS (equivalente a /var/www/html en Ubuntu)

# 1. Apache ya viene instalado en macOS
apachectl -v

# 2. Iniciar Apache
sudo apachectl start

# 3. Carpeta raíz web en macOS (equivalente a /var/www/html)
#    Aquí van todos los archivos .html, .css, .js, etc.
cd /Library/WebServer/Documents

# 4. Dar permisos completos (equivalente a "sudo chmod 777 -R html")
cd /Library/WebServer
sudo chmod 777 -R Documents

# 5. Acceso por navegador
#    http://localhost/archivo.html

# --------------------------------------------------------------------------------

# PHP EN MACOS (con Apache ya instalado)

# 1. Instalar PHP con Homebrew
brew install php

# ACTIVAR PHP EN APACHE (MACOS)

# 1. Editar el archivo de configuración de Apache
sudo nano /etc/apache2/httpd.conf

# 2. Añadir o descomentar esta línea (úsala tal cual):
LoadModule php_module /opt/homebrew/opt/php/lib/httpd/modules/libphp.so

# 3. Guardar y salir (CTRL + O, ENTER, CTRL + X)

# 4. Reiniciar Apache para activar PHP
sudo apachectl restart

# 5. Crear un archivo de prueba
echo "<?php phpinfo(); ?>" > /Library/WebServer/Documents/info.php

# 6. Probar en navegador:
# http://localhost/info.php

