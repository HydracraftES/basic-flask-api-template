from flask_restful import Resource, reqparse
from mysql_connection import mysql_connection

# Conexión a la base de datos.
db = mysql_connection()

# Método DeleteEvent
class DeleteEvent(Resource):
    
    def delete(self):
        
        # Abrimos conexión a la base de datos.
        conn = db.connection()
        query = conn.cursor()
        
        # Parseamos los parámetros que recibimos del body.
        parser = reqparse.RequestParser()
        
        # Añadimos los posibles atributos que pueda recibir por body.
        parser.add_argument("id", type=str, required=True)
        
        # Parseamos los parámetros.
        parser = parser.parse_args()
        
        # Definimos variables para manejar esos parámetros.
        id = parser['id']
        
        # Verificamos que reciba un contenido no nulo.
        if(len(id) <= 0):
            
            return {
                "status": "error",
                "message": "Los parámetros no pueden estar vacíos."
            }
            
        else:
            
            # Verificar primeramente que exista ese evento.
            query.execute("SELECT * FROM events WHERE id = %s", (id, ))
            result = query.fetchone()
                        
            if(result == None):
                
                # Cerramos la conexión
                conn.close()
                    
                return {
                    "status": "error",
                    "message": "Ese evento no existe"
                }
                
            else:
                
                # Ejecutamos la query para borrar
                query.execute("DELETE FROM events WHERE id = %s", (id,))
                
                # Guardamos cambios.
                conn.commit()
                
                # Cerramos la conexión
                conn.close()
                
                return {
                    "status": "success",
                    "message": "Se ha borrado el evento exitósamente."
                }