# Documentación de la práctica creativa 2 realizada por el Grupo 13.

## 1. Despliegue de la aplicación en máquina virtual pesada

### Decisiones de diseño e implementación

Para desplegar esta aplicación en una MV pesada hemos optado por usar los recursos ofrecidos en Google Cloud, ya que no hemos podido profundizar tanto en la automatización de procesos usando este tipo de recursos y creemos que aporta un nivel de abstracción mayor al estar toda la infraestructura de procesamiento y almacenamiento en la nube. 

Creamos un nuevo proyecto y dentro de este inicializamos una instancia de MV con la imagen Debian GNU/Linux 10. 

Una vez la MV está arrancada accedemos por SSH a la terminal. 

### Instalación y configuración de servicios

Primeramente, utilizamos el editor de texto Vim para editar el script de Python que ejecutará los comandos y procesos necesarios para la automatización de la implementación del servicio (appInstall.py).


