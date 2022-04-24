import json
from flask_restful import Resource
from mysql_connection import mysql_connection

# Conexión a la base de datos
db = mysql_connection()

# Método GetEvents
class GetEvents(Resource):
    
    def get(self):
        
        # Abrimos la conexión a la base de datos.
        conn = db.connection()
        query = conn.cursor()
        
        query.execute("SELECT * FROM events")
        result = query.fetchall()
        
        # Cerramos la conexión
        conn.close()

        return json.loads(json.dumps(result))