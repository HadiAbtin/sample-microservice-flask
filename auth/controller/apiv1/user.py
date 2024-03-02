from auth.util import jsonify
from auth.model import User
from auth.schema.apiv1 import UserSchema

class UserController:
    
    def get_user():
        return jsonify(status=501, code=107)

    def get_users(user_id):
        return jsonify(status=501, code=107)

