'''
    Este es la aplicación principal, para ejecutar el backend se tendría que ejecutar "python app.py" y ya se abriría, ya luego cuando se hace el deploy se tendrá que generar los certificados ssl (podríamos usar certbot mismo) y tendremos que indicarle los parámetros para asignarle la clave pública y la clave privada del ssl.
    
    El "CORS" es el middleware, es lo que permite procesar las solicitudes de los navegadores sin que de problemas, si os sale el error "origin blocked by cors policy", teniendo el cors activado, es que os ha tirado un error en el backend.
'''

from flask import Flask
from flask_restful import Api
from flask_cors import CORS


app = Flask(__name__)
CORS(app)
api = Api(app)

# Ruta de la Restful API: //localhost:3900/api/rutas
route = '/api'

# Métodos de la API.
from resources.CheckStatus.CheckStatus import CheckStatus
from resources.CRUD.NewEvent.NewEvent import NewEvent
from resources.CRUD.GetEvents.GetEvents import GetEvents
from resources.CRUD.GetEventPerId.GetEventPerId import GetEventPerId
from resources.CRUD.DeleteEvent.DeleteEvent import DeleteEvent
from resources.CRUD.UpdateEvent.UpdateEvent import UpdateEvent

# Rutas `GET`
api.add_resource(CheckStatus, route+'/check-status')
api.add_resource(GetEvents, route+'/events')
api.add_resource(GetEventPerId, route+'/event/<string:id>')

# Rutas `POST`
api.add_resource(NewEvent, route+'/post-new-event')

# Rutas `DELETE`
api.add_resource(DeleteEvent, route+'/delete-event')

# Rutas `PUT`
api.add_resource(UpdateEvent, route+'/update-events')

if(__name__ == '__main__'):
    app.run(debug=True, port=3900, host='0.0.0.0')