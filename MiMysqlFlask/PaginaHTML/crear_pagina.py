import os
import pymysql
from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/data')
def get_data():
    # Conexión a la base de datos MySQL
    conexion = pymysql.connect(
        host='mysql',
        user='root',
        password='',
        database='db',
        port=3306
    )

    # Consulta SQL para obtener los datos de la tabla "monumentos"
    consulta = "SELECT monumento, tipomonumento, clasificacion, tipoconstruccion, periodohistorico, poblacion_provincia FROM monumentos"

    # Ejecutar la consulta y obtener los datos
    with conexion.cursor() as cursor:
        cursor.execute(consulta)
        datos = cursor.fetchall()

    # Cerrar la conexión a la base de datos
    conexion.close()

    # Transformar los datos en el formato esperado por DataTables
    data = []
    for dato in datos:
        item = {
            'monumento': dato[0],
            'tipomonumento': dato[1],
            'clasificacion': dato[2],
            'tipoconstruccion': dato[3],
            'periodohistorico': dato[4],
            'poblacion_provincia': dato[5]
        }
        data.append(item)

    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
