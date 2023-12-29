#!usr/bin/env python 

import sys, subprocess, os, re # Librerias


def pause(): # Función para pausar el programa
    programPause = input('Press the <ENTER> key to continue...')

def installDependencies(): # Función para instalar las dependencias
    subprocess.call("sudo apt install python3", shell=True)
    pause()
    subprocess.call("sudo apt install pip3", shell=True)
    subprocess.call("sudo apt install git", shell=True)
    subprocess.call("git clone https://github.com/CDPS-ETSIT/practica_creativa2.git", shell=True)
    pause()
    path = '{}/practica_creativa2/bookinfo/src/productpage'.format(os.getcwd())
    os.chdir(path)
    subprocess.call("pip3 install -r requirements.txt", shell=True)
    os.environ["GRUPO_NUMERO"] = "Grupo 13" 

def modify_title(): # Modificar el código de la aplicación para incluir el nombre del grupo
    grupo_numero = os.getenv("GRUPO_NUMERO", "GrupoX")  # GrupoX es un valor de respaldo si la variable de entorno no está definida
    productpage_path = "./templates/productpage.html"
    index_path = "./templates/index.html"
    
    with open(productpage_path, "r") as file:
        content = file.read()
        content = re.sub(r'{% block title %}(.*?){% endblock %}', '{% block title %}'+grupo_numero+'{% endblock %}', content, flags=re.DOTALL)


    with open(productpage_path, "w") as file:
        file.write(content)

    with open(index_path, "r") as file:
        content = file.read()
        content = re.sub(r'{% block title %}(.*?){% endblock %}', '{% block title %}'+grupo_numero+'{% endblock %}', content, flags=re.DOTALL)

    with open(index_path, "w") as file:
        file.write(content)

    

def startApp(): # Función para iniciar la aplicación
    subprocess.call('python3 productpage_monolith.py 5000', shell=True)

installDependencies()
modify_title()
pause()
startApp()

