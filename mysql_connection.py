import mysql.connector

class mysql_connection():
    
    def connection(self):
        
        '''
            Crear la conexión a la base de datos de mysql, retorna la conexión, pero el cursor se hará de inicializar cada vez que se ejecute una consulta.
        '''
        
        connection = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "",
            database = "basic-api"
        )
        
        connection.autocommit = True
        
        return connection