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






Modificacion dependencias, Click da error al ejecutar pip install -r requirements.txt

Click == 7.0 ---> Click >= 7.0

itsdangerous==1.1.0 ---> itsdangerous>=2.1.2

Jinja2==2.11.3 ---> Jinja2>=3.1.2

Werkzeug==0.15.5 ---> Werkzeug>=2.3.7 

urllib3==1.26.5 ---> urllib3>=1.21.1,<1.25

MarkupSafe==0.23 ---> MarkupSafe>=2.0

gevent==1.4.0 ---> gevent>=1.4.0

greenlet==0.4.15 ---> greenlet>=0.4.15

requirements.txt utilizado con python 3.9:

certifi==2019.3.9
chardet==3.0.4
Click>=7.0
contextlib2==0.5.5
dominate==2.3.5
Flask==2.3.3
Flask-Bootstrap==3.3.7.1
Flask-JSON==0.3.3
future==0.17.1
futures==3.1.1
gevent>=1.4.0
greenlet>=0.4.15
idna==2.8
itsdangerous>=2.1.2
jaeger-client==3.13.0
Jinja2>=3.1.2
json2html==1.2.1
MarkupSafe>=2.0
nose==1.3.7
opentracing==1.2.2
opentracing-instrumentation==2.4.3
requests==2.21.0
simplejson==3.16.0
six==1.12.0
threadloop==1.0.2
thrift==0.11.0
tornado==4.5.3
urllib3>=1.21.1,<1.25
visitor==0.1.3
Werkzeug>=2.3.7
wrapt==1.11.1



