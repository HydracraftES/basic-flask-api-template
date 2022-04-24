from flask_restful import Resource

# Método `CheckStatus`
class CheckStatus(Resource):
    
    def get(self):
        
        return {
            "status": "success",
            "message": "La API funciona correctamente."
        }