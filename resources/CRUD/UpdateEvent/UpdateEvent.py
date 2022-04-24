from flask_restful import Resource, reqparse
from mysql_connection import mysql_connection

# Conexión a la base de datos
db = mysql_connection()

# Método UpdateEvent
class UpdateEvent(Resource):
    
    def put(self):
        
        # Abrimos la conexión a la base de datos.
        conn = db.connection()
        query = conn.cursor()
        
        # Parseamos los parámetros del body.
        parser = reqparse.RequestParser()
        
        parser.add_argument('id', type=str, required=True)
        parser.add_argument('title', type=str, required=True)
        parser.add_argument('content', type=str, required=True)
        
        parser = parser.parse_args()
        
        id = parser['id']
        title = parser['title']
        content = parser['content']

        if(len(id) <= 0 or len(title) <= 0 or len(content) <= 0):
            return {
                "status": "error",
                "message": "Tienes que colocar todos los campos"
            }
        else:
            
            query.execute("SELECT * FROM events WHERE id = %s", (id,))
            result = query.fetchone()
            
            if(result == None):
                return {
                    "status": "error",
                    "message": "Ese evento no existe."
                }
            else:
                query.execute("UPDATE events SET title=%s, content=%s WHERE id=%s", (title, content, id,))
            
                # Guardamos cambios.
                conn.commit()
                
                # Cerramos la conexión.
                conn.close()
                
                return {
                    "status": "success",
                    "message": "Se han guardado los cambios con éxito."
                }