from flask import Blueprint, jsonify, request
import pymysql
from conexion import get_db_connection

# Crea un Blueprint para el endpoint de ciclista
maillot = Blueprint('maillot', __name__)

@maillot.route('/maillot', methods=['GET'])
def get_users():
    try:
        conn = get_db_connection()  # Connect to the database
        cursor = conn.cursor(pymysql.cursors.DictCursor)  # Return results as dictionaries
        cursor.execute('SELECT * FROM maillot')  # Execute a SQL query
        users = cursor.fetchall()  # Fetch all rows from the result
        return jsonify(users)
    except Exception as e:
        print(f"Ocurrio un error: {e}")
        return jsonify('No se pudo ejecutar la consulta')
    finally:
        print('llega')
        if conn != None:
            conn.close()


@maillot.route('/maillotBycodigo', methods=['GET'])
def get_ciclista_by_id():
    try:
        codigo = request.args.get('codigo')
        conn = get_db_connection()  # Connect to the database
        cursor = conn.cursor(pymysql.cursors.DictCursor)  # Return results as dictionaries
        cursor.execute('SELECT * FROM maillot where codigo='+codigo)  # Execute a SQL query
        users = cursor.fetchall()  # Fetch all rows from the result
        conn.close()  # Close the database connection
    
    except Exception as e:
        print(f"Ocurrió un error: {e}")
    return jsonify('No se pudo ejecutar la consulta')

    return jsonify(users)

@maillot.route('/maillot', methods=['POST'])
def create_user():
    data = request.get_json()  # Obtener los datos JSON del cuerpo de la solicitud
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        # Suponiendo que los datos incluyen 'codigo' y 'color'
        sql = "INSERT INTO maillot (codigo, tipo, color, premio) VALUES (%s, %s, %s, %s)"
        cursor.execute(sql, (data['codigo'], data['tipo'], data['color'], data['premio']))
        conn.commit()  # Confirmar la transacción
        return jsonify({'message': 'Maillot modificado exitosamente'}), 201
    except Exception as e:
        print(f"Ocurrió un error: {e}")
        return jsonify('No se puede crear el maillot'), 404
    finally:
        if conn:
            conn.close()