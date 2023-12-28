#!usr/bin/env python 

import sys, subprocess, os


def pause():
    programPause = input('Press the <ENTER> key to continue...')

def installDependencies():
    subprocess.call("sudo apt install python3", shell=True)
    pause()
    subprocess.call("sudo apt install pip3", shell=True)
    subprocess.call("sudo apt install git", shell=True)
    subprocess.call("git clone https://github.com/CDPS-ETSIT/practica_creativa2.git", shell=True)
    pause()
    path = '{}/practica_creativa2/bookinfo/src/productpage'.format(os.getcwd())
    os.chdir(path)
    subprocess.call("pip3 install -r requirements.txt", shell=True)
    

def modify_title():
    # Modificar el código de la aplicación para incluir el nombre del grupo
    grupo_numero = os.getenv("GRUPO_NUMERO", "GrupoX")  # GrupoX es un valor de respaldo si la variable de entorno no está definida
    productpage_path = "./templates/index.html"
    
    with open(productpage_path, "r") as file:
        content = file.read()
        content = content.replace("{% block title %}Simple Bookstore App{% endblock %}", "{% block title %}{grupo_numero}{% endblock %}")

    with open(productpage_path, "w") as file:
        file.write(content)

def startApp():
    subprocess.call('python3 productpage_monolith.py 9080', shell=True)

installDependencies()
modify_title()
pause()
startApp()

