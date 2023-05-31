# Usa una imagen base con soporte para Python y Flask
FROM python:3.9-slim

# Establece el directorio de trabajo en la carpeta de la aplicación
WORKDIR /app

# Copia los archivos de la aplicación al directorio de trabajo
COPY . .

# Instala las dependencias del proyecto desde el archivo requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expone el puerto 5000, utilizado por Flask
EXPOSE 5000

# Establece las variables de entorno para Flask
ENV FLASK_APP=crear_pagina.py
ENV FLASK_RUN_HOST=0.0.0.0

# Comando para ejecutar la aplicación Flask
CMD ["flask", "run"]
