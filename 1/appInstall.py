#!/usr/bin/env python

import sys
import subprocess
import os
import re

def pause() -> None:
    programPause = input('Press the <ENTER> key to continue...')

def installDependencies() -> None:
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

def modify_title() -> None:
    grupo_numero = os.getenv("GRUPO_NUMERO", "GrupoX")
    productpage_path = "./templates/productpage.html"
    index_path = "./templates/index.html"
    
    with open(productpage_path, "r") as file:
        content = file.read()
        content = re.sub(r'{% block title %}(.*?){% endblock %}', '{% block title %}' + grupo_numero + '{% endblock %}', content, flags=re.DOTALL)

    with open(productpage_path, "w") as file:
        file.write(content)

    with open(index_path, "r") as file:
        content = file.read()
        content = re.sub(r'{% block title %}(.*?){% endblock %}', '{% block title %}' + grupo_numero + '{% endblock %}', content, flags=re.DOTALL)

    with open(index_path, "w") as file:
        file.write(content)

def startApp() -> None:
    subprocess.call('python3 productpage_monolith.py 5000', shell=True)

installDependencies()
modify_title()
pause()
startApp()

if __name__ == "__main__":
    pass


