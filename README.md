# Documentación de la práctica creativa 2 realizada por el Grupo 13.

## 1. Despliegue de la aplicación en máquina virtual pesada

### Decisiones de diseño e implementación

Para desplegar esta aplicación en una MV pesada hemos optado por usar los recursos ofrecidos en Google Cloud, ya que no hemos podido profundizar tanto en la automatización de procesos usando este tipo de recursos y creemos que aporta un nivel de abstracción mayor al estar toda la infraestructura de procesamiento y almacenamiento en la nube. 

Creamos un nuevo proyecto y dentro de este inicializamos una instancia de MV con la imagen Debian GNU/Linux 10. 

Una vez la MV está arrancada accedemos por SSH a la terminal. 

### Instalación y configuración de servicios

Primeramente, utilizamos el editor de texto Vim para editar el script de Python que ejecutará los comandos y procesos necesarios para la automatización de la implementación del servicio (appInstall.py).

Ejecutamos el script desde la terminal:

```
python3 appInstall.py
```

Una vez se ha ejecutado, si no ha habido ningún problema de incompatibilidad de dependencias y/o de ejecución debería salir lo siguiente en la terminal:

```
INFO:root:start at port 5000
 * Serving Flask app "productpage_monolith" (lazy loading)
 * Environment: production
   WARNING: Do not use the development server in a production environment.
   Use a production WSGI server instead.
 * Debug mode: on
INFO:werkzeug: * Running on http://[::]:5000/ (Press CTRL+C to quit)
INFO:werkzeug: * Restarting with stat
/usr/lib/python3/dist-packages/requests/__init__.py:91: RequestsDependencyWarning: urllib3 (1.26.5) or chardet (3.0.4) doesn't match a supported version!
  RequestsDependencyWarning)
INFO:root:start at port 5000
WARNING:werkzeug: * Debugger is active!
INFO:werkzeug: * Debugger PIN: 206-608-507
```


## 2. Despliegue de una aplicación monolítica usando docker

### Instalación de Docker

Antes de comenzar con el proceso de despliegue necesitamos instalar las herramientas necesarias. Al estar trabajando sobre una MV pesada en los servicios de Google Cloud, hace falta instalar Docker.
Para instalar la versón más reciente de Docker seguimos la documentación oficial en: https://docs.docker.com/engine/install/debian/

Una vez instalado Docker podemos comenzar con la dockerización de la aplicación.

### Implementación

El primer paso para desplegar la aplicación utilizando un contenedor en docker es definir el Dockerfile en la raíz del proyecto:

```
$ tree

.
├── bookinfo
│   ├── platform
│   └── src
├── Dockerfile
├── images
│   ├── app-microservices.png
│   ├── app-monolith.png
│   └── web-app-gui.png
└── README.md
```
El dockerfile del proyecto tendrá la siguiente estructura:

```
FROM python:3.7.7-slim

# Establece el directorio de trabajo en el contenedor
WORKDIR /app

# Copia los archivos necesarios al contenedor
COPY ./bookinfo/src/productpage /app

# Copia las dependencias
COPY ./bookinfo/src/productpage/requirements.txt /app

# Instala las dependencias

RUN pip install --no-cache-dir -r requirements.txt

# Configura la variable de entorno para el grupo
ENV GRUPO_NUMERO=13

# Expone el puerto 9080
EXPOSE 9080

# Comando de inicio
CMD ["python3", "productpage_monolith.py", "9080"]
```




