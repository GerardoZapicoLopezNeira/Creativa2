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

