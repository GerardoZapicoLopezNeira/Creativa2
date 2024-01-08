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

La imagen creada a partir de esta aplicación se ha subido a DockerHub mediante los comandos:

```
sudo docker image tag g13-product-page:1.0 gerardozapico/creativa2g13:g13-product-page
sudo docker push gerardozapico/creativa2g13:g13-product-page
```
Primeramente ha sido probado en una máquina local, y luego se ha bajado del repositorio para probar la imagen en la MV pesada desplegada en Google Cloud.

```
docker pull gerardozapico/creativa2g13:g13-product-page
docker run -p 9080:9080 gerardozapico/creativa2g13:g13-product-page
```

## 3. Segmentación de una aplicación monolítica en microservicios utilizando docker-compose

La implementación de esta solución dividida en microservicios ha sido implementada en nuestra máquina local, empezando por la definición del Dockerfile de cada servicio.
Cada fichero ha sido creado en la carpeta correspondiente al servicio, de la siguiente manera:

```
.
├── bookinfo
    ├── docker-compose.yml
    └── src
        ├── details
        │   └── Dockerfile
        ├── productpage
        │   ├── Dockerfile
        │     
        ├── ratings
        │   ├── Dockerfile
        │   
        └── reviews
            ├── reviews-application
            └── reviews-wlpcfg
                ├── Dockerfile
```

Después de crear las imágenes respectivas a cada servicio, creamos el fichero docker-compose.yml.

### Problemas de implementación encontrados
 
Uno de los cambios estructurales más importantes durante la implementación fue la asignación y mapeo de puertos de la máquina física (ordenador personal) al contenedor, para que de esta forma hubiese 3 servicios funcionando sobre "el mismo" puerto 9080. 

Adicionalmente, en el fichero de configuración docker-compose.yml introducimos un segundo volumen dedicado al servicio ratings:
```
ratings:
    image: g13/ratings
    container_name: g13-ratings
    build:
      context: ./src/ratings
    ports:
      - "9082:9080"
    volumes:
      - ./src/ratings:/opt/microservices
      - /opt/microservices/node_modules 
    environment:
      - SERVICE_VERSION=v1
```

De esta forma el contenedor podrá manejar las librerias instaladas con el comando ```npm install```.


### Diferencias con la versión de un único contenedor

- **Arquitectura de la Aplicación:**
En la implementación original de un único contenedor, la aplicación estaba compuesta como un monolito, donde los servicios estaban integrados en un solo contenedor. En contraste, en la versión basada en microservicios, cada servicio se ha segmentado en un contenedor independiente.

- **Independencia de Desarrollo y Despliegue:**
Con la arquitectura de microservicios, cada equipo/máquina puede desarrollar, probar y desplegar su propio servicio de manera independiente. Esto permite una mayor flexibilidad y agilidad en el ciclo de desarrollo en comparación con la versión monolítica, donde cualquier cambio afectaba a toda la aplicación.

- **Escalabilidad Granular:**
En el enfoque de microservicios, cada servicio puede ser escalado de manera independiente según sus requisitos de carga. En el caso de la versión monolítica, la escalabilidad era única para toda la aplicación, lo que podía llevar a subutilización de recursos.

- **Manejo de Versiones de Servicios:**
Con la introducción de microservicios, se implementaron tres versiones diferentes del servicio Reviews, cada una mostrando estrellas de manera distinta. La variable de entorno SERVICE_VERSION controla qué versión está activa. Esto proporciona una mayor flexibilidad y capacidad para gestionar múltiples versiones de servicios, algo que no era posible en la versión monolítica.

- **Comunicación entre Microservicios:**
La comunicación entre los microservicios se realiza mediante llamadas de red, lo que establece una clara interfaz de comunicación entre ellos. En comparación, la versión monolítica tenía una comunicación interna más directa, ya que todos los componentes estaban en el mismo contenedor.

- **Despliegue y Actualización Continuos:**
La arquitectura de microservicios permite la implementación y actualización continua de servicios individuales, lo que minimiza el impacto en otros servicios. Esto contrasta con la versión monolítica, donde las actualizaciones podrían afectar a toda la aplicación y requerir un despliegue completo.

### Resultado del despliegue de la aplicación

En las imágenes se documenta el proceso de despliegue a través de las diferentes versiones de la aplicación.

## 4. Despliegue de una aplicación basada en microservicios utilizando Kubernetes

Para este despliegue se ha hecho uso de la herramienta gcloud CLI, para poder desplegar y administrar el clúster en GKE desde la terminal de nuestro equipo local.

### Instalación
```
curl -O https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-cloud-cli-458.0.1-linux-x86_64.tar.gz
tar -xf google-cloud-cli-458.0.1-linux-x86_64.tar.gz
./google-cloud-sdk/install.sh
./google-cloud-sdk/bin/gcloud init
```
### Despliegue del clúster
Primero nos autenticamos en gcloud con ```gcloud auth login```, nos situamos en el proyecto creado anteriormente ```gcloud config set project pcreativa2g13``` y elegimos la zona de facturación adecuada (Madrid) ```gcloud config set compute/zone europe-southwest1-a```. 
Creamos el clúster con la configuración requerida ```gcloud container clusters create cluster-pcreativa --num-nodes=5 --no-enable-autoscaling``` y configuramos kubctl para que apunte al clúster creado ```gcloud container clusters get-credentials cluster-pcreativa```. 
Aplicamos todos los ficheros de despliegue y servicios en el clúster ```kubectl apply -f [NOMBRE_FICHERO].yaml```.

Con esta configuración el clúster bajará las imágenes creadas en el apartado anterior desde el repositorio de Docker Hub y las montará sobre los pods creados en los 5 nodos. En total hay 9 pods corriendo (3 réplicas del servicio **details**, 1 réplica del servicio **productpage**, 2 réplicas del servicio **ratings** y 1 réplica de cada versión del servicio **reviews**). Esta monitorización puede hacerse con los comandos siguientes:
```
# Muestra los pods corriendo en el clúster
kubectl get pods
NAME                             READY   STATUS    RESTARTS   AGE
details-v1-594b48c9c7-84c84      1/1     Running   0          15m
details-v1-594b48c9c7-pzxcr      1/1     Running   0          15m
details-v1-594b48c9c7-x8lf7      1/1     Running   0          15m
productpage-v1-fcbcfd8dd-sj22h   1/1     Running   0          16m
ratings-v1-f59877749-j4sw4       1/1     Running   0          16m
ratings-v1-f59877749-x2sbt       1/1     Running   0          16m
reviews-v1-69b7f64449-hdb6g      1/1     Running   0          18m
reviews-v2-58b979c4d6-wv4q5      1/1     Running   0          17m
reviews-v3-57d65dc979-q6pf2      1/1     Running   0          16m

# Muestra los servicios y los puertos que está utilizando cada uno, junto a su IP interna y externa
kubectl get services
NAME                   TYPE           CLUSTER-IP     EXTERNAL-IP     PORT(S)        AGE
details                ClusterIP      10.16.4.64     <none>          9080/TCP       36m
kubernetes             ClusterIP      10.16.0.1      <none>          443/TCP        45m
productpage            ClusterIP      10.16.5.54     <none>          9080/TCP       36m
productpage-external   LoadBalancer   10.16.11.154   34.175.81.177   80:32593/TCP   35m
ratings                ClusterIP      10.16.7.121    <none>          9080/TCP       36m
reviews                ClusterIP      10.16.4.48     <none>          9080/TCP       36m

# Muestra los servicios desplegados. Desplegamos la versión de reviews que queremos mostrar en la aplicación.
kubectl get deployments
NAME             READY   UP-TO-DATE   AVAILABLE   AGE
details-v1       3/3     3            3           53m
productpage-v1   1/1     1            1           53m
ratings-v1       2/2     2            2           53m
reviews-v2       1/1     1            1           52m

```
### Diferencias al crear Pods y Escalabilidad

- Al crear Pods individualmente, puedes utilizar el comando kubectl apply -f NOMBRE_DEL_ARCHIVO.yaml para cada archivo de configuración de los Pods.

- Si utilizas archivos separados para cada microservicio, puedes actualizar o aplicar cambios específicos a un microservicio sin afectar a otros, lo que facilita la administración.

- En cuanto a la escalabilidad, al utilizar la configuración de réplicas en los Deployments, puedes escalar horizontalmente tus aplicaciones. Por ejemplo, puedes aumentar o disminuir el número de réplicas de un microservicio según la demanda de tráfico.

- Con una solución de orquestación de contenedores como Kubernetes, la escalabilidad puede manejarse automáticamente a través de la autoescalabilidad (si está habilitada, en nuestro caso no) o manualmente ajustando el número de réplicas en la configuración del Deployment.
