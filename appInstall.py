#!usr/bin/env python 

import sys, subprocess, os


def pause():
    programPause = input('Press the <ENTER> key to continue...')

def main():
    subprocess.call("sudo apt install python3", shell=True)
    pause()
    subprocess.call("sudo apt install pip3", shell=True)
    subprocess.call("sudo apt install git", shell=True)
    subprocess.call("git clone https://github.com/CDPS-ETSIT/practica_creativa2.git", shell=True)
    pause()
    path = '{}/practica_creativa2/bookinfo/src/productpage'.format(os.getcwd())
    os.chdir(path)
    subprocess.call("pip3 install -r requirements.txt", shell=True)
    pause()
    subprocess.call('python3 productpage_monolith.py 9080', shell=True)

main()
