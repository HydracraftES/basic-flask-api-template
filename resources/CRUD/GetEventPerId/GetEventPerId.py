import json
from flask_restful import Resource
from mysql_connection import mysql_connection

# Conexión a la base de datos.
db = mysql_connection()

# Método GetEventPerId
class GetEventPerId(Resource):
    
    def get(self, id):
        
        # Añadimos valores al parámetro que recogerá de la url.
        self.id = id
        
        conn = db.connection()
        query = conn.cursor()
        
        query.execute("SELECT * FROM events WHERE id = %s", (id,))
        result = query.fetchone()
        
        # Verificamos que exista ese id, en caso de error devolverá un estado de error.
        if(result == None): 
            
            # Cerramos la conexión
            conn.close()
            
            return {
                "status": "error",
                "message": "No existe ningún evento con esa id."
            }
        
        else:
            
            # Cerramos la conexión
            conn.close()
            
            return json.loads(json.dumps(result))