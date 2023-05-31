import requests
import json
import mysql.connector
import time

time.sleep(20)


response = requests.get('https://analisis.datosabiertos.jcyl.es/api/records/1.0/search/?dataset=relacion-monumentos&q=&rows=1000&facet=tipomonumento&facet=clasificacion&facet=tipoconstruccion&facet=periodohistorico&facet=poblacion_provincia')
data = json.loads(response.content)

# Conectarse a la base de datos MySQL
mydb = mysql.connector.connect(
  host="mysql",
  user="root",
  database="db",
  port="3306"
)

mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE IF NOT EXISTS monumentos (id INT AUTO_INCREMENT PRIMARY KEY, nombre VARCHAR(255), tipo_monumento VARCHAR(255), clasificacion VARCHAR(255), tipo_construccion VARCHAR(255), periodo_historico VARCHAR(255), poblacion_provincia VARCHAR(255))")


for record in data['records']:
    monumento = record['fields']['nombre']
    tipo_monumento = record['fields'].get('tipomonumento')
    clasificacion = record['fields'].get('clasificacion')
    tipo_construccion = record['fields'].get('tipoconstruccion')
    periodo_historico = record['fields'].get('periodohistorico')
    poblacion_provincia = record['fields'].get('poblacion_provincia')

    # Verificar si el monumento ya existe en la base de datos
    sql = "SELECT * FROM monumentos WHERE monumento = %s AND tipomonumento = %s AND clasificacion = %s AND tipoconstruccion = %s AND periodohistorico=%s AND poblacion_provincia = %s"
    val = (monumento, tipo_monumento, clasificacion, tipo_construccion, periodo_historico, poblacion_provincia)
    mycursor.execute(sql, val)
    result = mycursor.fetchone()
    
    # Insertar el monumento si no existe en la base de datos
    if result is None:
        sql = "INSERT INTO monumentos (monumento, tipomonumento, clasificacion, tipoconstruccion, periodohistorico, poblacion_provincia) VALUES (%s, %s, %s, %s, %s, %s)"
        val = (monumento, tipo_monumento, clasificacion, tipo_construccion, periodo_historico, poblacion_provincia)
        mycursor.execute(sql, val)
        mydb.commit()


# Leer los datos insertados
mycursor.execute("SELECT * FROM monumentos")
result = mycursor.fetchall()


print(mycursor.rowcount, "filas insertadas.")