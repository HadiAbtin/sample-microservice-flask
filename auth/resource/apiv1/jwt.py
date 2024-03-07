from flask_restful import Resource
from auth.controller.apiv1 import AuthController

class AuthResource(Resource):

    def get(self):
        """
        GET /jwt/tokens --> Validate the token
        """
        return AuthController.verify_jwt_token()

    def post(self):
        """
        POST /jwt/tokens --> Create a new token
        """
        return AuthController.create_jwt_token()
