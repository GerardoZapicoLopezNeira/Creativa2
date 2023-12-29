#!/usr/bin/env python

import sys
import subprocess
import os
import re

def pause():
    """Pausa el programa hasta que se presiona la tecla <ENTER>."""
    programPause = input('Press the <ENTER> key to continue...')

def installDependencies():
    """Instala las dependencias necesarias para el proyecto."""
    subprocess.call("sudo apt install python3", shell=True)
    pause()
    subprocess.call("sudo apt install pip3", shell=True)
    subprocess.call("sudo apt install git", shell=True)
    subprocess.call("git clone https://github.com/CDPS-ETSIT/practica_creativa2.git", shell=True)
    pause()
    # Cambia al directorio del proyecto clonado
    path = '{}/practica_creativa2/bookinfo/src/productpage'.format(os.getcwd())
    os.chdir(path)
    subprocess.call("pip3 install -r requirements.txt", shell=True)
    # Establece la variable de entorno GRUPO_NUMERO
    os.environ["GRUPO_NUMERO"] = "Grupo 13"

def modify_title():
    """Modifica el código de la aplicación para incluir el nombre del grupo."""
    grupo_numero = os.getenv("GRUPO_NUMERO", "GrupoX")
    productpage_path = "./templates/productpage.html"
    index_path = "./templates/index.html"
    
    # Modifica el contenido del archivo productpage.html
    with open(productpage_path, "r") as file:
        content = file.read()
        content = re.sub(r'{% block title %}(.*?){% endblock %}', '{% block title %}' + grupo_numero + '{% endblock %}', content, flags=re.DOTALL)

    with open(productpage_path, "w") as file:
        file.write(content)

    # Modifica el contenido del archivo index.html
    with open(index_path, "r") as file:
        content = file.read()
        content = re.sub(r'{% block title %}(.*?){% endblock %}', '{% block title %}' + grupo_numero + '{% endblock %}', content, flags=re.DOTALL)

    with open(index_path, "w") as file:
        file.write(content)

def startApp():
    """Inicia la aplicación."""
    subprocess.call('python3 productpage_monolith.py 5000', shell=True)

# Instala dependencias, modifica el título y luego inicia la aplicación
installDependencies()
modify_title()
pause()
startApp()



