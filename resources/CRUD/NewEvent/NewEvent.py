from flask_restful import Resource, reqparse
from mysql_connection import mysql_connection

# Conexión a la base de datos
db = mysql_connection()

# Método InfoUser/<string:nick>
class NewEvent(Resource):
    
    def post(self):
        
        # Abrimos la conexión a la base de datos.
        conn = db.connection()
        query = conn.cursor()
        
        # Parseamos los parámetros que recibimos del body.
        parser = reqparse.RequestParser()
        
        # Añadimos los posibles atributos que pueda recibir por body.
        parser.add_argument("title", type=str, required=True)
        parser.add_argument("content", type=str, required=True)
        
        # Parseamos los parámetros.
        parser = parser.parse_args()
        
        # Definimos variables para manejar esos parámetros.
        title = parser['title']
        content = parser['content']
        
        # Verificamos que recibe un contenido no nulo.
        if(len(title) <= 0 or len(content) <= 0):
            
            # Cerramos la conexión
            conn.close()
            
            return {
                "status": "error",
                "message": "Los parámetros no pueden estar vacíos."
            }
            
        else:
            
            '''
                Una vez llegue a esta parte del código, significará que todo está correcto y podremos proceder a filtrar, si falta hace, los campos que recibe e insertarlos en la base de datos.
            '''
            query.execute("INSERT INTO events (title, content) VALUES (%s, %s)", (title, content,))
        
            # Para guardar los cambios en la base de datos hay que ejecutar el commit, es importante porque si no no se guardará bien los nuevos datos insertados!
            conn.commit()
            
            # Cerramos la conexión
            conn.close()
            
            return {
                "status": "success",
                "message": "Se ha insertado los datos a la base de datos."
            }